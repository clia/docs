#!/usr/bin/env python

# Copyright (c) 2016 The Polymer Project Authors. All rights reserved.
# This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
# The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
# The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
# Code distributed by Google as part of the polymer project is also
# subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt

__author__ = 'ericbidelman@chromium.org (Eric Bidelman)'

import sys
sys.path.insert(0, 'lib')

import logging
import os
import jinja2
import webapp2
import yaml
import re
import json

from google.appengine.api import memcache
import http2push.http2push as http2push


jinja_loader = jinja2.FileSystemLoader(os.path.dirname(__file__))

# include the _escaped_ contents of a file
def include_file(name):
  try:
    return jinja2.Markup.escape(jinja_loader.get_source(env, name)[0])
  except Exception as e:
    logging.exception(e)

# include the literal (unescaped) contents of a file
def include_file_raw(name):
  try:
    return jinja2.Markup(jinja_loader.get_source(env, name)[0])
  except Exception as e:
    logging.exception(e)

env = jinja2.Environment(
  loader=jinja_loader,
  extensions=['jinja2.ext.autoescape'],
  autoescape=True,
  trim_blocks=True,
  variable_start_string='{{{',
  variable_end_string='}}}')
env.globals['include_file'] = include_file
env.globals['include_file_raw'] = include_file_raw

# memcache logic: maintain a separate cache for each explicit
# app version, so staged versions of the docs can have new nav
# structures, redirects without affecting other deployed docs.

# CURRENT_VERSION_ID format is version.hash, where version is the
# app version passed to the deploy script.
MEMCACHE_PREFIX = 'no_version/'
if 'CURRENT_VERSION_ID' in os.environ:
  MEMCACHE_PREFIX = os.environ.get('CURRENT_VERSION_ID').split('.')[0] + '/'

REDIRECTS_FILE = 'redirects.yaml'
NAV_FILE = '%s/nav.yaml'
ARTICLES_FILE = 'blog.yaml'
AUTHORS_FILE = 'authors.yaml'
IS_DEV = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

def render(out, template, data={}):
  try:
    t = env.get_template(template)
    out.write(t.render(data).encode('utf-8'))
  except jinja2.exceptions.TemplateNotFound as e:
    handle_404(None, out, data, e)
  except Exception as e:
    handle_500(None, out, data, e)

def read_redirects_file(filename):
  with open(filename, 'r') as f:
    redirects = yaml.load(f)
    literals = {}
    wildcards = {}
    # Break lines into dict.
    # e.g. "/0.5/page.html /1.0/page" -> {"/0.5/page.html": "/1.0/page")
    # If the redirect path ends with *, treat it as a wildcard.
    # e.g. "/0.5/* /1.0/" redirects "/0.5/foo/bar" to "/1.0/foo/bar"
    for r in redirects:
      parts = r.split()
      if parts[0].endswith('*'):
        wildcards[parts[0][:-1]] = parts[1]
      else:
        literals[parts[0]] = parts[1]
  return {'literal': literals, 'wildcard': wildcards}

def read_nav_file(filename, version):
  with open(filename, 'r') as f:
    nav = yaml.load(f)
  for one_section in nav:
    one_section['version'] = version
    base_path = '/%s/%s/' % (version, one_section['shortpath'])
    if 'items' in one_section:
        for link in one_section['items']:
          if 'path' in link:
            # turn boolean flag into an additional CSS class.
            if 'indent' in link and link['indent']:
              link['indent'] = 'indent'
            else:
              link['indent'] = ''
            if not 'name' in link:
              if link['path'].startswith(base_path):
                link['name'] = link['path'].replace(base_path, '')
              else:
                link['name'] = 'index'
  return nav

def read_articles_file(filename, authors):
  with open(filename, 'r') as f:
    articles = yaml.load(f)

  # For each article, smoosh in the author details.
  for article in articles:
    article['author'] = authors[article['author']];
  return articles

def read_authors_file(filename):
  with open(filename, 'r') as f:
    authors = yaml.load(f)
  return authors

def handle_404(req, resp, data, e):
  resp.set_status(404)
  render(resp, '/404.html', data)

def handle_500(req, resp, data, e):
  logging.exception(e)
  resp.set_status(500)
  render(resp, '/500.html', data);


# class VersionHandler(http2push.PushHandler):

#   def get(self, version):
#     render(self.response, '/%s/index.html' % version)


class Site(http2push.PushHandler):

  def redirect_if_needed(self, path):
    redirect_cache = MEMCACHE_PREFIX + REDIRECTS_FILE
    redirects = memcache.get(redirect_cache)
    if redirects is None or IS_DEV:
      redirects = read_redirects_file(REDIRECTS_FILE)
      memcache.add(redirect_cache, redirects)

    literals = redirects.get('literal')
    if path in literals:
      self.redirect(literals.get(path), permanent=True)
      return True

    wildcards = redirects.get('wildcard')
    for prefix in wildcards:
      if path.startswith(prefix):
        self.redirect(path.replace(prefix, wildcards.get(prefix)), permanent=True)
        return True

    return False

  def get_site_nav(self, version):
    nav_file_for_version = NAV_FILE % version
    nav_cache = MEMCACHE_PREFIX + nav_file_for_version
    site_nav = memcache.get(nav_cache)
    if site_nav is None or IS_DEV:
      site_nav = read_nav_file(nav_file_for_version, version)
      memcache.add(nav_cache, site_nav)
    return site_nav

  def nav_for_section(self, version, section):
    nav = self.get_site_nav(version)
    versioned_section = '%s/%s' % (version, section)
    if nav:
      for one_section in nav:
        if one_section['shortpath'] == section or one_section['shortpath'] == versioned_section:
          if 'items' in one_section:
            return one_section['items']
    return None

  def versions_for_section(self, section):
    nav_1 = self.get_site_nav('1.0')
    nav_2 = self.get_site_nav('2.0')

    versioned_section_1 = '%s/%s' % ('1.0', section)
    versioned_section_2 = '%s/%s' % ('2.0', section)

    versions = ['','']
    if nav_1:
      for one_section in nav_1:
        if one_section['shortpath'] == section or one_section['shortpath'] == versioned_section_1:
          versions[0] = one_section['path'];
    if nav_2:
      for one_section in nav_2:
        if one_section['shortpath'] == section or one_section['shortpath'] == versioned_section_2:
          versions[1] = one_section['path'];
    return versions

  def get_articles(self):
    articles_cache = MEMCACHE_PREFIX + ARTICLES_FILE
    articles = memcache.get(articles_cache)

    authors_cache = MEMCACHE_PREFIX + AUTHORS_FILE
    authors = memcache.get(authors_cache)

    if authors is None or IS_DEV:
      authors = read_authors_file(AUTHORS_FILE)
      memcache.add(authors_cache, authors)

    if articles is None or IS_DEV:
      articles = read_articles_file(ARTICLES_FILE, authors)
      memcache.add(articles_cache, articles)

    return articles

  def get_active_article_data(self, articles, path):
    # Find the article that matches this path
    fixed_path = '/' + path
    for article in articles:
      if article['path'] == fixed_path:
        return article
    return None

  @http2push.push()
  def get(self, path):
    if self.redirect_if_needed(self.request.path):
      return

    # Root / serves index.html.
    # Folders server the index file (e.g. /docs/index.html -> /docs/).
    if not path or path.endswith('/'):
      path += 'index.html'
    # Remove index.html from URL.
    elif path.endswith('index'):
      path = path[:path.rfind('/') + 1]
      # TODO: preserve URL parameters and hash.
      return self.redirect('/' + path, permanent=True)
    # Make URLs pretty (e.g. /page.html -> /page)
    elif path.endswith('.html'):
      path = path[:-len('.html')]
      return self.redirect('/' + path, permanent=True)

    version = 'bad_version'
    nav = None
    articles = None
    active_article = None
    full_nav = None
    versions = ['','']
    match = re.match('([0-9]+\.[0-9]+)/([^/]+)', path)

    if match:
      version = match.group(1)
      section = match.group(2)
      full_nav = self.get_site_nav(version)
      nav = self.nav_for_section(version, section)
      versions = self.versions_for_section(section)

      data = {
        'nav': nav,
        'full_nav': full_nav,
        'versions': versions
      }
    else:
      if path.startswith('blog') or path == 'index.html':
        articles = self.get_articles()
        active_article = self.get_active_article_data(articles, path)

      data = {
        'full_nav': self.get_site_nav('1.0') + self.get_site_nav('2.0'),
        'articles': articles,
        'active_article': active_article
      }

    # Add .html to construct template path.
    if not path.endswith('.html'):
      path += '.html'

    render(self.response, path, data)

routes = [
  # ('/(\d\.\d)/$', VersionHandler),
  ('/(.*)', Site),
]

app = webapp2.WSGIApplication(routes, debug=IS_DEV)
app.error_handlers[404] = handle_404
app.error_handlers[500] = handle_500
