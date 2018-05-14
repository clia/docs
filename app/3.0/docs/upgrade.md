---
title: Polymer 3.0 upgrade guide
---

<!-- toc -->


<<<<<<< HEAD
The Polymer modulizer tool automates most of the changes you need to make to upgrade a project from 2.x to 3.x.

Polymer modulizer is still in pre-release, but has been fairly well-tested converting the Polymer library and elements. See the [README](https://github.com/Polymer/polymer-modulizer/blob/master/README.md) for the latest updates.

**Start with a clean repo.** Before upgrading an element, make sure that any changes in your repo are committed, so you don't lose any previous changes, and can roll back to a previous state if you run into trouble. 
{.alert .alert-info}
=======
Polymer 2.0 包括一些破坏性的改变。不过，Polymer 团队一直致力于一条增量地将 Polymer 1.x 元素更新到 2.0 的路径。

Polymer 2.0 支持多种类型的元素：

*   2.x 基于类的元素，使用受自定义元素 v1 规范支持的 ES6 基于类的语法。推荐用于 Polymer 2.0 的新开发。
*   2.x 遗留元素，使用 `Polymer` 工厂方法，拥有大多数的 1.0 API 对于它们是可用的，以及任何新的 2.x API。
*   2.x 混合元素是使用遗留的 `Polymer` 工厂方法定义的元素，有额外的代码来提供 1.x 向后兼容性。
    它们可以在 Polymer 1.8+ 以及 Polymer 2.x 上运行。
    尽可能地，混合元素应该只使用 1.x 和 2.x 都支持的 API 的公共子集。
    在某些情况下，他们可能需要条件化的代码来运行在 1.x 或 2.x 中。
    维护混合元素比维护基于类的元素或遗留元素更复杂，因为它们需要在 1.x 和 2.x 上都进行测试。

移植大型项目时，您可以一次性地更新到 Polymer 1.8 并将元素升级为 2.0 混合形式。
当所有元素都升级完后，您可以针对 Polymer 2.0 来测试您的项目。

Polymer 团队计划发布一个 Polymer 升级工具，以自动执行将 1.x 元素升级为混合的或基于类的形式所需的一些更改。
剩下的更改需要手动对代码进行修改、测试，或者两者都有，以确保您的元素在 2.0 中的表现与 1.x 中的相同。
**升级工具目前还不可用。**


有关安装的说明，请参阅 [安装 Polymer 2.0](about_20#installing)。

此升级指南目前还在完善中。请
[在 GitHub 上报告问题](https://github.com/Polymer/docs/issues/new)。

## 升级策略

When upgrading an element or app, there are several possible scenarios:

-   Upgrading an individual element.
-   Upgrading a small application.
-   Upgrading a large application that uses many custom, reusable elements.

When upgrading individual elements, you can choose to upgrade to either hybrid mode (if supporting
both 1.x and 2.x simultaneously is important), or to upgrade directly to legacy mode or class-based
mode. For simple elements, just updating the DOM template and styling may be enough to get the
element running in 2.x legacy mode.

For a small application, converting your own elements to hybrid mode is probably not useful.
The simplest incremental approach is to convert each element's DOM template first and get it running
in legacy mode. Then you can port elements to class-based mode as desired.

For large applications, where you have written many of your own reusable elements, you may want to
upgrade elements individually to hybrid mode.

### 在您开始之前

Before you start the upgrade, there's a couple of things you need to do.

*   Update the Polymer CLI.
*   Create a new branch or workspace.
*   Update bower dependencies.

Update the Polymer CLI:

```
npm update polymer-cli
```

#### 创建一个新的分支或工作区

You'll want to work in a new branch or workarea so you don't
break the existing, 1.x version of your element or app.

#### 更新 bower 依赖项

Follow these steps to update your bower dependencies:

1.  Remove the existing `bower_components` folder.

    ```bash
    rm -rf bower_components
    ```

2.  Update the Polymer version in `bower.json` to the latest versions.

    | Component | Version |
    |-----------|---------|
    | Polymer   | `^2.0.0` |
    | webcomponentsjs | `^1.0.0` |
    | web-component-tester | `^6.0.0` |
    | Polymer elements | `^2.0.0` |
>>>>>>> 20_zh

## Upgrade a project using modulizer

To upgrade a project:

1.  Install the latest version of the Polymer CLI. 

    ```
    npm install -g polymer-cli
    ```

1.  Install Polymer modulizer.

    ```
    npm install -g polymer-modulizer
    ```

<<<<<<< HEAD
1.  Make sure your bower dependencies are up to date. 
 
    `bower cache clean && bower install`
=======
If you are upgrading the element to hybrid mode, you can add extra sets of bower dependencies
so you can test against multiple versions of Polymer easily. For details, see
[Manage dependencies for hybrid elements](devguide/hybrid-elements#dependency-variants).

### 升级元素

When upgrading an individual element, start by updating the DOM template and styling. For simple
elements, this may be the only change you need to make to run in hybrid or legacy mode.

## 阴影 DOM 模板和样式 {#shadow-dom-changes}

Polymer 2.0 elements create shadow DOM v1 shadow trees.  As such, user code related to scoped
styling, distribution, and events must be adapted to the native v1 API.


*   ***All elements*** need to update their shadow DOM template and styling as described in
    [DOM template](#dom-template) and [Shadow DOM styles](#shadow-dom-styles).


### DOM 模板 {#dom-template}

**All elements** need to update their shadow DOM templates and styling as described in this section.

Quick summary:

*   Remove deprecated patterns in the DOM module (`<dom-module>` using `is` or `name`; styles
    outside of the template).
*   Update your element's DOM template to use the new `<slot>` element instead of `<content>`.
*   Update styles to use the `::slotted()` selector  in place of ::content.
*   Remove any `/deep/` and `::shadow` CSS rules.
*   Update any URLs inside the template.

These changes are detailed in the following sections.

#### 移除 DOM 模块中过时的模式 {#remove-deprecated-patterns-in-dom-module}

Your `<dom-module>` **must set** the `id` property to specify the element name. Polymer 1.x accepted
the deprecated  `is` or `name` as alternatives.

Make sure your element's styles are defined *inside the template*. Defining styles outside the
template was deprecated in Polymer 1.x and is no longer supported.

Before {.caption}


```html
<dom-module name="blue-element">
  <template>
    <div>I am blue!</div>
  </template>
  <style>
    :host { color: blue; }
  </style>
</dom-module>
```

After {.caption}


```html
<dom-module id="blue-element">
  <template>
    <style>
      :host { color: blue; }
    </style>
    <div>I am blue!</div>
  </template>
</dom-module>
```

#### 替换内容元素 {#replace-content-elements}

*   Change `<content>` insertion points to `<slot>` elements.

*   Change `<content select="...">` to named slots: `<slot name="...">`.

Before {.caption}

```html
<!-- element template -->
<dom-module id="my-el">
  <template>
    ...
    <h2>
      <content select=".title"></content>
    </h2>
    <div>
      <content></content>
    </div>
  </template>
</dom-module>

  ...
<!-- usage -->
<my-el>
  <span class="title">Mr. Darcy</span>
  <span>Fun at parties.</span>
</my-el>
```


After {.caption}


```html
<!-- element template -->
<dom-module id="my-el">
  <template>
    ...
    <h2>
      <slot name="title"></slot>
    </h2>
    <div>
      <slot></slot>
    </div>
  </template>
</dom-module>

 ...
<!-- usage -->
<my-el>
  <span slot="title">Mr. Darcy</span>
  <span>Fun at parties.</span>
</my-el>
```

Note that if you're using `<content select="...">` anywhere in your code, ***this means a change to
your element's contract***, and everyone using your element will need to update to use slot names.

**Limitation.** Slots can only be selected explicitly, by *slot name*. It's impossible to select
content implicitly, based on a tag name or an arbitrary selector like `:not(.header)`.
{.alert .alert-info}

Before: implicit selection {.caption}

```html
<!-- element template -->
<dom-module id="my-el">
  <template>
    ...
    <div class="header">
      <!-- Selection by tag name isn't supported.
           This element must be redesigned to work with
           Shadow DOM v1. -->
      <content select="h2"></content>
    </div>
    <div class="body">
      <content></content>
     </div>
    </template>
</dom-module>

<!-- usage -->
<my-el>
  <h2>Mr. Darcy</h2>
  <span>Not so fun at parties.</span>
</my-el>
```

After: explicit selection {.caption}


```html
<!-- element template -->
<dom-module id="my-el">
  <template>
    ...
    <div class="header">
      <!-- Shadow DOM v1 version uses explicit slot name -->
      <slot name="header"></slot>
    </div>
    <div class="body">
      <slot></slot>
     </div>
    </template>
</dom-module>

<!-- usage -->
<my-el>
  <h2 slot="header">Mr. Darcy</h2>
  <span>Not so fun at parties.</span>
</my-el>
```

Although these examples show only a single element being assigned to a slot, any number of elements
can be assigned to the same slot. For example:

```html
<my-el>
  <h2 slot="header">Mr. Darcy</h2>
  <p>Not so fun at parties.</p>
  <p>Improves on further acquaintance.</p>
</my-el>
```

Here, both paragraphs are assigned to the default slot.

#### 默认插槽 VS 默认插入点

In shadow DOM v0, a default insertion point (one without a
`select` attribute) consumes all nodes **not matched by a previous insertion point**.  In v1, a
default slot (one without a `name` attribute) **only matches content with no slot attribute**. In
other words, **a node with a slot attribute is never distributed to the default slot**.


```html
<!-- shadow DOM v0 template -->
<template>
  <!-- this insertion point gets everything -->
  <content></content>
  <!-- the following insertion point never matches anything; the default
         Insertion point is greedy. -->
  <content select=".special"></content>
</template>

<!-- shadow DOM v1 template -->
<template>
  <!-- this slot gets any top-level nodes that don't have slot
       attributes. -->
  <slot></slot>
  <!-- the following insertion point gets any top-level nodes that have
       slot="special". -->
  <slot name="special"></slot>
  <!-- top-level nodes that have slot attributes with other values
       don't get distributed at all. -->
</template>
```

If you have complex distributions, and you're trying to upgrade to hybrid elements, you may need
to place **both** `<content>` and `<slot>` elements in the template.

#### 多层分布 {#multilevel-distribution}

Multilevel distribution works differently in shadow DOM v1. In v0, content was redistributed at each
level. For example, an element with `class="title"` can be distributed through several insertion
points and eventually selected by a `<content select=".title">`.

Document content {.caption}

```
<!-- v0 redistribution example -->
<parent-el>
  <span class="title">My Title</span>
</parent-el>
```

Shadow DOM of `<parent-el>` {.caption}
>>>>>>> 20_zh

1.  Run modulizer.

	  `modulizer --import-style name --out .` 

    The `--import-style name` option tells modulizer to write imports using package names instead of paths. You might want to omit this option when converting an application project. 

    The `--out .` option tells modulizer to write its output to the current directory, overwriting its current contents.

1.  Test the project. 

    You may need to perform some manual fixes at this point. See [Post-conversion cleanup](#post-conversion-cleanup) for details.

### Post-conversion cleanup

There are a few manual steps that may be required after converting a project using modulizer.

1.  Fix strict mode and module errors.

    Modules always run in strict mode, and with various other restrictions. A few examples include: 

    *   Variables must be declared.
    *   `this` is undefined at the top level.
    *   `document.write` doesn't work.
    *   `document.currentScript` doesn't work.

    Modulizer can't make these changes for you.

1.  Convert `importHref` to dynamic `import`()

    For example, this:

    ```js
    const resolvedPageUrl = this.resolveUrl('my-page.html');
    Polymer.importHref(
        resolvedPageUrl,
        null,
        this._showPage404.bind(this),
        true);
    ```

    Becomes: 

    `import('my-page.js').then(null, this._showPage404.bind(this));`

<<<<<<< HEAD
    Note that `resolveUrl` is not required. Imports are always resolved relative to the current module.
=======
#### 所有元素：在模板中更新 URL {#urls-in-templates}
>>>>>>> 20_zh

1.  Fix imports that load polyfills.

    In the past some elements have provided HTML imports for loading polyfills. For example, the neon-animation element provided an HTML import to load the web animations polyfill. 

    In the ES6 module world, the extra file is no longer required. Any required polyfills should be loaded at the application level. 
    
    For example, given a `some-polyfill.html` file that loads a polyfill script:

    ```html
    <script src="./bower_components/some_polyfill/some_polyfill.js"></script>
    ```

    Move the script into the main document.

## Steps automated by modulizer

This section lists the changes made by Polymer modulizer. They may be helpful as an overview of what the Polymer modulizer is doing to convert your code. 

<<<<<<< HEAD
Before upgrading an element, make sure that any changes in your repo are committed, so you don't lose any previous changes, and can roll back to a previous state if you run into trouble. 
=======
### 阴影 DOM 样式 {#shadow-dom-styles}
>>>>>>> 20_zh

1.  Rename the file from `.html` to `.js`.

    `mv my-el.html my-el.js`

1.  Convert HTML imports for ES6 module imports.

<<<<<<< HEAD
	  `<link rel=import href="foo.html">`
=======
#### 替换内容选择器
>>>>>>> 20_zh

    Becomes:

    ```js
    import './foo.js';
    ```

    For importing resources _that are part of the same project_ (for example, app-specific elements), use an absolute path (starting with `/`) or a relative path (starting with `./` or `../`) .

    For importing resources installed using npm, use a module specifier starting with the package name. For example, for Polymer imports, you'll usually replace a path like `/bower_components/polymer` with `@polymer/polymer`.

    In many cases, you'll need to import specific symbols. For example, the standard Polymer element import:

    ```html
    <link rel="import" href="../bower_components/polymer/polymer-element.html">
    ```

    Becomes:

    ```js
    import {PolymerElement, html} from '@polymer/polymer/polymer-element.js'
    ```

1.  Move the template from HTML into a static `template` getter.

    ```html
    <html>
      <dom-module>
        <template>foo</dom-module>
      </dom-module>
      <script>
        class A extends Polymer.Element { … }
      </script>
    </html>
    ```
    Becomes:

    ```js
    import {PolymerElement, html} from '@polymer/polymer';

    class A extends PolymerElement {
      static get template() {
        return html`foo`;
      }
<<<<<<< HEAD
    }
    ```
=======
      #container ::slotted(.warning) {
        color: red;
      }
    </style>
    <div id="container">
      <slot></slot>
    </div>
  </template>
</dom-module>

<!-- usage -->
<slotted-el>
  <div>
    I'm colored blue.
  </div>
  <div class="warning">
    I'm colored red.
  </div>
  <div>
    <span class="warning">Surprise! Not red.</span>
  </div>
</slotted-el>
```

In shadow DOM v1, **you cannot select a descendant of a top-level distributed child**. For example,
you can't select the span in the previous example like this:

`#container ::slotted(*) span { ... }`

No selectors can follow the  `::slotted()` selector.

For more information, see [Styling distributed nodes](https://developers.google.com/web/fundamentals/getting-started/primers/shadowdom#stylinglightdom) in the Web Fundamentals article on shadow DOM.

#### 移除深度和阴影选择器

If you still have any `/deep/` or `::shadow` selectors in your project, it's time to remove them.
They don't work at all in shadow DOM v1.

There's no direct substitute for shadow-piercing selectors.To let users customize your element,
[custom CSS properties](/{{{polymer_version_dir}}}/docs/devguide/custom-css-properties) are probably the best option.

#### 替换根选择器 {#replace-root-selectors}

If you're using the `:root` selector inside an element's template, replace it with:

```css
:host > * { ... }
```

(If you're using `:root` selection inside a `custom-style`, replace it with the `html` selector.)

In 1.x, you can use either of these selectors to override custom properties set at a higher level.
For example, the following rule in the main document:


```css
style-me {
  --my-theme-color: blue;
}
```


Overrides a `:host` rule in `style-me`'s shadow root, because they match the same element, but the
main document styles comes earlier in the cascade order. `:host > *` applies a ruleset to all of the
top-level children in the host's shadow tree, which doesn't conflict with the rule in the main
document.

Before {.caption}


```html
<style>
  :root {
    --my-theme-color: red;
  }
</style>
```


After {.caption}


```html
<style>
  :host > * {
    --my-theme-color: red;
  }
</style>
```

#### 更新自定义属物语法 {#update-custom-property-syntax}

When applying custom properties, Polymer 1.x accepted this incorrect syntax for specifying a default
value to a `var()` function:

Before {.caption}

```css
color: var(--special-color,--default-color);
```

By specification, the default (or fallback) is a CSS value, not a custom property name. To use a
custom property as a default, add a nested `var()` function.

After {.caption}

```css
color: var(--special-color, var(--default-color));
```

In addition, you must update the syntax of any `@apply` rules to match the proposal, which doesn't
use parentheses.

Before {.caption}

```css
@apply(--my-mixin);
```

After {.caption}

```css
@apply --my-mixin;
```

#### 封装自定义样式元素 {#wrap-custom-style-elements}

While custom elements v1 supports customized built-in elements, Polymer 2.0 does not currently use
them. Instead, it introduces a new `<custom-style>` element that wraps a `<style>` element.

*   **Hybrid projects.** Wrap your existing `<style is="custom-style">` elements with
    `<custom-style>` elements.
*   **2.0-only projects.** Replace your existing  `<style is="custom-style">` elements with
    `<custom-style>` elements.
*   **All projects.** Ensure the `<custom-style>` element is placed in the document's body,
    or as the last element in the `<head>`.
*   **All projects.** Replace any `:root` selectors with `html`, and update custom property syntax
    as described in [Update custom property syntax](#update-custom-property-syntax).

**Custom-style placement**. The `<custom-style>` element should be placed in the document's
`<body>`, or just before the closing tag for the `<head>` element. Why? Only certain elements 
can appear inisde a document's `<head>`  element. `<style>` elements are allowed, but custom 
elements like `<custom-style>` are not. If the browser encounters a `<custom-style>` tag inside 
`<head>`, it will close the `<head>` element and move the `<custom-style>` and any following 
tags to the body.
{.alert .alert-info}

Before {.caption}

```html
<style is="custom-style">
  /* In a 1.x custom-style, :root can be used to set global defaults */
  :root {
    --my-theme-color: #9C27B0;
  }
</style>
```


After (hybrid code) {.caption}

```html
<custom-style>
  <style is="custom-style">
    /* In a 2.x custom-style use the html selector to set global defaults */
    html {
      --my-theme-color: #9C27B0;
    }
  </style>
</custom-style>
```

After (2.x-only code) {.caption}

```html
<custom-style>
  <style>
    html {
      --my-theme-color: #9C27B0;
    }
  </style>
</custom-style>
```

## DOM API {#polymer-dom-apis}

**Hybrid elements** must continue to use existing Polymer DOM APIs, but may require some
changes. **Class-based elements** should use native DOM APIs.
>>>>>>> 20_zh

1.  Replace namespaced references with imports.

    ```html
    <link rel="import" href="/bower_components/polymer/lib/utils/render-status.html">
    ```

    And: 

<<<<<<< HEAD
    ```js 
    Polymer.RenderStatus.afterNextRender(callback);
    ```
=======
#### 混合元素：更新 Polymer.dom 用法 {#hybrid-elements-update-polymer-dom-usage}
>>>>>>> 20_zh

    Becomes:

    ```js
    import {afterNextRender} from '@polymer/polymer/lib/utils/render-status.js;
      ...
    afterNextRender(callback);
    ```

    The 3.x modules correspond to the 2.x HTML imports. See the [3.0 API docs](/3.0/docs/api/) for a list of exports from each module.

1.  Remove any top-level IIFE wrappers.

    Modules automatically encapsulate their contents.

    ```js
    (() => {
      let foo;
    })();
    ```

    Becomes:

    ```js
    let foo;
    ```

<<<<<<< HEAD
1.  Add `importMeta` static getter, if necessary.
=======
#### 基于类的和遗留的元素：使用原生的 DOM 方法 {#class-based-and-legacy-elements-use-native-dom-methods}
>>>>>>> 20_zh

    If you use the `importPath` property in you element's template, you must add a static `importMeta` getter:

    ```js
    class extends PolymerElement {
      static get importMeta() { return import.meta; }
    }
    ```

1.  Convert `polymer.json`

    Replace the `.html` filenames with their `.js` equivalent.

    If you're using the polyfill loader (`webcomponents-loader.js`), update the `extraDependencies` array to include the new webcomponents bundles:

    ```js
    "extraDependencies": [
      "node_modules/@webcomponents/webcomponentsjs/bundles/**"
    ],
    ```

1.  Convert `bower.json` to `package.json`.

    Add all of your dependencies here. Note that `package.json` can only have one main file.

1.  Update to newer polyfills

	  Make sure you're depending on the v2 versions of the polyfills in `package.json`.

    ```js
        "@webcomponents/webcomponentsjs": "^2.0.0",
    ```

    If you were using `webcomponents-lite.js`, replace it with `webcomponents-bundle.js`.

1.  Update top-level `.html` files.

    Certain HTML files stay as HTML—things like an index.html with content, or test documents. They usually just need to update` <link rel=import>` to `<script type=module>`

Some projects may also need the steps described in [Less common upgrade tasks](#less-common-upgrade-tasks), which are typically performed by modulizer.

If you are converting by hand, see [Post-conversion cleanup](#post-conversion-cleanup) for the final steps.

### Less common upgrade tasks

This section describes a few tasks which aren't required for every element, but which may be required for some elements or modules.

#### Move any non-template DOM into imperative code

If your module contains any DOM that's _not_ part of the element template, you'll need to add imperative code to insert it into the main document. For example, if your 2.x HTML import includes a `<custom-style>` tag, you could replace it with code like this:

```js
const $_documentContainer = document.createElement('template');

<<<<<<< HEAD
$_documentContainer.innerHTML = `<custom-style>
=======
```html
<link rel="import" href="/bower_components/polymer/lib/utils/flattened-nodes-observer.html">
```



## CSS 自定义属物垫片 {#css-custom-property-shim}

Polymer 2.0 continues to use a shim to provide limited support for CSS custom properties on browsers
that do not yet natively support custom properties (currently only Microsoft Edge and IE). This lets
an element expose a custom styling API. The shim is now included as part of the shady CSS polyfill,
not in the Polymer library itself.

**For class-based elements**, support for custom CSS mixins has been moved to a second, optional
shim.

The following changes have been made in the shims that Polymer 2.0 uses:

*   The shim always uses native CSS custom properties on browsers that support them. This was
    optional in 1.x, and it introduces some limitations on the use of mixins.
*   CSS mixin support has been separated into an optional shim.
*   The `customStyle` instance property has been removed. Use `updateStyles` instead.
*   Invalid custom properties syntax is no longer supported. These changes are described in
    [Shadow DOM styles](#shadow-dom-styles).

### 基于类的元素：导入 CSS 混入垫片

If you are using **class-based elements** and you are using **CSS mixins**, import the CSS mixin
shim.

CSS custom properties are becoming widely supported, CSS mixins remain a proposal. So support for
CSS mixins has been moved to a separate shim that is optional for 2.0 class-style elements. For
backwards compatibility, the `polymer.html` import includes the CSS mixin shim. Class-style elements
must explicitly import the mixin shim.

The shim performs a one-time transformation of stylesheets  containing CSS custom property mixins.
Where possible, mixins are transformed into individual  native CSS properties for better performance.

This introduces some limitations to be aware of, which are documented in the
[shady CSS polyfill README](https://github.com/webcomponents/shadycss#custom-properties-and-apply).

The following examples show how to load the CSS mixin shim.

Example: importing CSS mixin shim to top-level file {.caption}

```
<!-- load polyfills -->
<script src="/bower_components/webcomponentsjs/webcomponents-lite.js"></script>
<!-- import CSS mixin shim -->
<link rel="import" href="/bower_components/shadycss/apply-shim.html">
<!-- import custom-style -->
<link rel="import" href="/bower_components/polymer/lib/elements/custom-style.html">

<custom-style>
>>>>>>> 20_zh
  <style>
    html { 
      --theme-color: #eee;
    }
<<<<<<< HEAD
   </style>
  </custom-style>`
document.head.appendChild($_documentContainer.content);
```

#### Replace namespace declarations with exports
=======

    customElements.define(XCustom.is, XCustom);
  </script>
</dom-module>
```

### 所有元素：使用 updateStyles 而不是 customStyle {#use-updatestyles-instead-of-customstyle}

**All elements**. Instead of using the `customStyle` object, pass new style properties to the `updateStyles` method.
This use of `updateStyles` was already supported in 1.x. The `customStyle` object is removed in 2.0.

Before {.caption}

```js
this.customStyle['--my-dynamic-property'] = 'red';
this.updateStyles();
```

After {.caption}


```js
this.updateStyles({'--my-dynamic-property': 'red'});
```

To handle cases in which `getComputedStyleValue` was previously used, use the custom ShadyCSS API when the polyfill is loaded:

Before {.caption}

```
style = this.getComputedStyleValue('--something');
```

After {.caption}

```
if (window.ShadyCSS) {
  style = ShadyCSS.getComputedStyleValue(el, '--something');
} else {
  style = getComputedStyle(el).getPropertyValue('--something');
}
```

## 自定义元素 API {#custom-elements-apis}

Polymer 2.0 elements target the custom elements v1 API.


*   **All elements.** The contracts have changed for several of the lifecycle callbacks. Check and
    test your code to make sure this doesn't cause problems with your elements.
*   **All elements.** Refactor type-extension elements as wrapper elements. Wrap existing
    type-extension elements.

### 回调合约已变更 {#callback-contracts-have-changed}

Polymer 2.0 introduces several changes to the contracts of the various lifecycle callbacks. Some of
these are required by the custom elements v1 specification, while others are designed to improve
performance.

For more information on the lifecycle callbacks, see [Lifecycle changes](about_20#lifecycle-changes).

#### 创建时间 (created/constructor) {#creation-time-created-constructor}
>>>>>>> 20_zh

If you have a module that added properties or functions to a global namespace, use exports to make the APIs available, instead. 

<<<<<<< HEAD
For example: 
=======
*   Defer work until after the constructor completes using `setTimeout` or `requestAnimationFrame`.
*   Move work to a different callback,such as `attached`/`connectedCallback` or `ready`.
*   Use an observer, `slotchange` event listener, or mutation observer to react to runtime changes.

#### 准备好的时间 {#ready-time}

The `ready` callback, for one-time initialization, signals the creation of the element's shadow DOM.
In the case of class-based elements, you need to call `super.ready()` before accessing the shadow
tree.

The major difference between 1.x and 2.0 has to do with the timing of initial light DOM distribution.
In the v1 shady DOM polyfill, initial distribution of children into `<slot>` is asynchronous
(microtask) to creating the `shadowRoot`, meaning distribution occurs after observers are run and
`ready`  is called. In the Polymer 1.0 shim, initial distribution occurred before `ready`.

To check the initial distribution, use `setTimeout` or `requestAnimationFrame` from `ready`. The
callback should fire after initial distribution is complete.

Class-based element: check distributed nodes {.caption}
>>>>>>> 20_zh

```js
const MyStuff = MyStuff || {}; 
MyStuff.MyMixin = (base) =>  class extends base { ... }; 
``` 

Instead of appending to the `MyStuff` namespace, the module can simply export `MyMixin`:

```js
export const MyMixin = (base) => class extends base { ... };
```

<<<<<<< HEAD
Generally remove `this` references that refer to the namespace object.
=======
For more details on `observeNodes`, see
[Observe added and removed children](../../1.0/docs/devguide/local-dom#observe-nodes) in the Polymer 1
documentation.

In order to force distribution synchronously, call `Polymer.dom.flush`. This can be useful for
unit tests.

In 2.x, `Polymer.dom.flush` does not flush the `observeNodes` callbacks. To force the `observeNodes`
callbacks to be invoked, call the `flush` method on the observer object returned from `observeNodes`.


 #### 附加时间 (attached/connectedCallback) {#attach-time-attached-connectedcallback}

If you have any code that relies on the element being layed out when the `attached` callback runs
(for example, measuring the element or its children), it must wait until the layout is complete.

Use the `Polymer.RenderStatus.beforeNextRender` function to register a one-time callback after
layout is complete, but before the page is rendered (or "painted").

Before {.caption}
>>>>>>> 20_zh

```js
Foo.Bar = {
  one() {
    return this.two();
  },
  two() {
    return 2;
  }
}
```

Becomes:

```js
export function one() {
  return two();
}
<<<<<<< HEAD

export function two() {
  return 2;
}
```

Likewise you don't need to bind functions where the `this` value should be the namespace object.
=======
```

For work that can be deferred until after first paint (such as adding event listeners), you can use
`Polymer.RenderStatus.afterNextRender`, which takes the same arguments as `beforeNextRender`.

These examples show the hybrid callbacks, but the `Polymer.RenderStatus` API can be used in
class-based elements as well. If you're loading the `polymer-element.html`
import, you need to import `Polymer.RenderStatus` separately.

```html
<link rel="import" href="/bower_components/polymer/lib/utils/render-status.html">
```

### 移除扩展类型的元素 {#remove-type-extension-elements}

Polymer doesn't support type-extension elements (such as `<input is="iron-input">`). For a discussion
of this change, see [Type-extension elements](about_20#type-extension)

*   **All projects.** Refactor your own type-extension elements.
*   **All projects.** Replace any top-level template extension elements with the 2.0 wrapper
    equivalents.

#### 重构扩展类型的元素 {#refactor-type-extension-elements}

Type extension elements need to be refactored into standard custom elements (for example, instead of
an element that extends an `<a>` element, an element that takes an `<a>` element in its light DOM).

#### 在文档级别转换模板扩展元素 {#convert-template-extension-elements-at-the-document-level}


If you have any template extension elements—`dom-bind`, `dom-if`, or `dom-repeat`—*in the main
document*, convert them to the wrapped form.

Before {.caption}

```
<template is="dom-bind">
  <ul>
  <template is="dom-repeat" items="{{people}}">
    <li>{{item.name}}
  </template>
  </ul>
</template>
<script>
var domBind = document.querySelector('template[is=dom-bind]');
domBind.people = [
 ...
];
</script>
```


After {.caption}


```
<dom-bind>
  <!-- Hybrid code must keep the is="dom-bind" for backwards
       compatibility. For 2.0-only projects, use a plain template. -->
  <template is="dom-bind">
    <ul>
    <!-- inner template doesn't need to be wrapped -->
    <template is="dom-repeat" items="{{people}}">
      <li>{{item.name}}
    </template>
    </ul>
  </template>
</dom-bind>
<script>
var domBind = document.querySelector('dom-bind');
domBind.people = [
 ...
];
</script>
```

Polymer automatically wraps template extensions used in Polymer element templates during template
processing. This means you can and should continue using `<template is="">` in templates nested
inside a Polymer element template. As shown above, nested templates inside a top-level `dom-bind`,
`dom-if`, or `dom-repeat` are also automatically wrapped.


**Templates used in the main document must be manually wrapped.**


## 数据系统 {#data-system}

Polymer 2.0 includes several important changes to the data system, detailed in
[Data system improvements](about_20#data-system).

### 移除键路径和 Polymer.Collection {#remove-key-paths-and-polymer-collection}

Code that interacts with key paths, or uses `Polymer.Collection` directly won't run in hybrid mode.
If upgrading to hybrid mode, you can conditionalize 1.0 code:


```
if (Polymer.Element) {
  // 2.0 code
} else {
  // 1.0 code
}
```


If upgrading to legacy or class-based elements, you can eliminate this code. Array change
notifications for specific items use index paths. Changing the entire array results in a change
notification for the entire array.

### 更新观察者 {#update-observers}

Observers need to check for `undefined` arguments, which was not an issue in 1.x. If all of your
observer's dependencies have default values, the observer should not be called with `undefined`
arguments. But if your code relies on the observer to wait until all dependencies are defined, you
need to add `undefined` checks.

If your observer relies on hidden dependencies being initialized, you may need to update your code.

Before {.caption}

>>>>>>> 20_zh

```js
Foo.Bar = {
  one() {
    el.addEventListener('click', this.onclick.bind(this));
  },
  onclick() {...}
}
```

Becomes:

```js
export function one() {
  el.addEventListener('click', onclick);
}
<<<<<<< HEAD
=======
```

### 自定义属物序列化和反序列化

If your element overrides the `serialize` or `deserialize` methods, these override points have been
renamed to `_serializeValue` and `_deserializeValue`, respectively.

### 数据系统杂项 {#data-system-miscellany}

A few more changes that you may need to take into account.

Only properties listed explicitly in `properties` can be configured from an attribute. You need to
explicitly declare your property if both of the following are true:

*   You have a property that's declared *implicitly* (used in a binding or observer, but not in the
    `properties` object).
*   You rely on configuring that property from an attribute (not a data binding).

Because several aspects of timing change in 2.0, you'll need to test your code to ensure that it
doesn't rely on any 1.x timing. In particular:

*   Element initialization (including template stamping and data system initialization) is deferred
    until the element is connected to the main document. (This is a result of the custom element
    v1 changes.)

In order for a property to be deserialized from its attribute, it must be declared in the
`properties` metadata object

Binding a default value of `false` using an *attribute binding* to a boolean property will not
override a default `true` property of the target, due to the semantics of boolean attributes.
In general, property binding should always be used when possible, and will avoid such situations.


## 移除的 API {#removed-apis}

The following APIs have been removed.

*   `Polymer.instanceof` and `Polymer.isInstance`: no longer needed, use `instanceof` and
    `instanceof Polymer.Element`  instead.


*   `element.getPropertyInfo`: This API returned unexpected information some of the time and was
    rarely used.

*   `element.getNativePrototype`: Removed because it is no longer needed for internal code and was
    unused by users.

*   `element.beforeRegister`: This was originally added for metadata compatibility with ES6 classes.
    We now prefer users create ES6 classes by extending `Polymer.Element`, specifying metadata in
    the static `properties` and `observers` properties.

    For legacy elements, dynamic effects may now be added using the `registered` lifecycle method.

*   `element.attributeFollows`: Removed due to disuse.

*   `element.classFollows`: Removed due to disuse.

*   `listeners` Removed ability to use `id.event` to add listeners to elements in shadow DOM. Use
    declarative template event handlers instead.

*    Methods starting with `_` are not guaranteed to exist (most have been removed).

## 升级到基于类的元素 {#upgrading-to-class-based-elements}

To define a class-based element, create a class that extends `Polymer.Element` (a subclass of
`HTMLElement`), which provides most of the same features of Polymer 1.x based on static
configuration data supplied on the class definition.

The basic syntax looks like this:

```html
<!-- Load the Polymer.Element base class -->
<link rel="import" href="bower_components/polymer/polymer-element.html">

<script>
// Extend Polymer.Element base class
class MyElement extends Polymer.Element {

  static get is() { return 'my-element'; }

  static get properties() {
    return {
      /* properties meta data object just like 1.x */
      myProp: {
        type: Object,
        notifies: true
      }
    }
  }

  static get observers() {
    return [
      /* observer array just like 1.x */
      '_myPropChanged(myProp.*)'
    ]
  }

  constructor() {
    super();
    ...
  }

  connectedCallback() {
    super.connectedCallback();
    ...
  }

  _myPropChanged(changeRecord) {
    ...
  }
  ...
}

// Register custom element definition using standard platform API
customElements.define(MyElement.is, MyElement);
</script>
```

**Class-based elements are 2.0 only.** These elements are not backward compatible
with 1.x.
{.alert .alert-info}

Below are the general steps for defining a custom element using this new syntax:

*   Extend from `Polymer.Element`. This class provides the minimal surface area to integrate with
    2.0 DOM templating and data binding system. It provides the standard custom element lifecycle
    callbacks, plus the Polymer-specific `ready` callback.

*   Implement "behaviors" as [mixins that return class expressions](#mixins). Or use the
    `mixinBehaviors` method to mix hybrid behaviors into your element.

*   Element's `is` property should be defined as a static on the class.

*   The `listeners` and `hostAttributes` have been removed from element metadata; listeners and
    default attributes can be installed as and when needed. For convenience _`ensureAttribute` is
    available to set default attributes.

    ```js
    // set tabindex if it's not already set
    this._ensureAttribute('tabindex', 0);
    ```

    Note that attributes can't be manipulated in the constructor.

### 通用实用程序 API

`Polymer.Element` provides a cleaner base class without much of the sugared utility API
that present on legacy elements, such as `fire`, `transform`, and so on. With web platform surface
area becoming far more stable across browsers, we intend to add fewer utility methods and embrace
the raw platform API more.  This section describes replacements for some of the more common APIs.

In addition, many features are still included in the library, but as optional modules or mixins
rather than being bundled in with `Polymer.Element`. For details, see
[Import optional features](#optional-features).



#### async

In many cases you can use the native platform features (such as `setTimeout` or
`requestAnimationFrame` instead of the `async` call. Polymer 2.x also provides an optional
[`Polymer.Async`](/{{{polymer_version_dir}}}/docs/api/namespaces/Polymer.Async) module that provides
a set of Async APIs with a common interface. This is particularly useful for microtask timing, which
is harder to time consistently across browsers.


Before using `Polymer.Async`, you must import it:

```
<!-- import async module -->
<link rel="import" href="/bower_components/polymer/lib/utils/async.html">
```

With one arguments, the legacy `async` method produced microtask timing:

```
this.async(someMethod);
```

The equivalent method with `Polymer.Async` looks like this:

```
// in JS, execute someMethod with microtask timing
Polymer.Async.microTask.run(() => this.someMethod());
```

If using `async` with a timeout:

```
this.async(someMethod, 500);
```

The native `setTimeout` works fine:

```js
setTimeout(() => this.someMethod(), 500);
```

#### debounce

The legacy `debounce` method isn't available on `Polymer.Element`. In many cases, you can trivially
implement a debounced method that does what you want.

You can also use the `Polymer.Debouncer` class.


```html
<!-- import debounce module -->
<link rel="import" href="/bower_components/polymer/lib/utils/debounce.html">
```

```js
this._debouncer = Polymer.Debouncer.debounce(this._debouncer,
    Polymer.Async.timeOut.after(250),
    () => { this.doSomething() });
```

#### fire

Instead of using the legacy
`this.fire('some-event')` API, use the equivalent platform APIs:


```js
this.dispatchEvent(new CustomEvent('some-event', { bubbles: true, composed: true }));
```

The `fire` method sets the `bubbles` and `composed` properties by default. For more on using custom
events, see [Fire custom events](/{{{polymer_version_dir}}}/docs/devguide/events#custom-events).

(The `CustomEvent` constructor is not supported on IE, but the webcomponents polyfills include a
small polyfill for it so you can use the same syntax everywhere.)

#### importHref

The `importHref` instance method is replaced by the static `Polymer.importHref` function. The only
difference from the instance method is that the load and error callbacks don't have the `this`
value bound to the element. You can work around this by using arrow functions:

```js
Polymer.importHref(this.resolveUrl('some-other-file.html'),
    () => this.onLoad(loadEvent),
    () => this.onError(errorEvent),
    true /* true for async */);
```

#### $$

The `$$` method isn't available. Use `this.shadowRoot.querySelector` instead.

#### 使用遗留的 API

If you want to upgrade to a class-based element but depend on some of the removed APIs, you can
add most of the legacy APIs by using the `LegacyElementMixin`.

```js
class MyLegacyElement extends Polymer.LegacyElementMixin(Polymer.Element) { ... }
```

### 类混入和行为 {#mixins}

A class expression mixin is essentially a factory function that takes a class as an argument and
returns a new class, with new features "mixed in." Polymer 2.x provides a number of features as
optional mixins instead of building them into the base class.

Apply mixins when you create an element class:

```js
class MyElement extends MyMixin(Polymer.Element) {
  static get is() { return 'my-element' }
}
```

The `MyMixin(Polymer.Element)` returns a new class, which extends `Polymer.Element` and adds the
features from `MyMixin`. So `MyElement`'s inheritance is:

`MyElement => MyMixin(Polymer.Element) => Polymer.Element`

For information on writing your own class expression mixins, see
[Sharing code with class expression mixins](devguide/custom-elements#mixins)


#### 在类风格的元素上使用混合行为

In some cases, the features you want to use may be available as hybrid behaviors, but not as
class mixins.

You can add hybrid behaviors to your class-style element using the `Polymer.mixinBehavior` function:

```js
class XClass extends Polymer.mixinBehaviors([MyBehavior, MyBehavior2], Polymer.Element) {
  static get is() { return 'x-class'}

  ...
}
customElements.define(XClass.is, XClass);
```

The `mixinBehavior` function also mixes in the Legacy APIs, the same as if you extended
`Polymer.LegacyElement`. These APIs are required since since hybrid behaviors depend on them.

### 导入可选功能 {#optional-features}

A number of features have been omitted from the base `Polymer.Element` class and packaged as
separate, optional imports. These include:

-   [Gesture support](devguide/gesture-events).
-   [`<array-selector>` element](devguide/templates#array-selector)
-   [`<custom-style>` element](devguide/style-shadow-dom#custom-style)
-   [`<dom-bind>` element](devguide/templates#dom-bind)
-   [`<dom-if>` element](devguide/templates#dom-if)
-   [`<dom-repeat>` element](devguide/templates#dom-repeat)
-   [`Polymer.RenderStatus`](/{{{polymer_version_dir}}}/docs/api/namespaces/Polymer.RenderStatus)
    module.

Element imports are found in the Polymer folder under `/lib/elements`, mixins under `/lib/mixins`,
and utility modules under `/lib/utils`. For example, to load the `Polymer.RenderStatus` module,
use an import like this:

```html
<link rel="import" href="/bower_components/polymer/lib/utils/render-status.html">
```



>>>>>>> 20_zh

export function onclick() { … }
```