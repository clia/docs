---
title: Styling local DOM
---

<!-- toc -->

Polymer uses [Shadow DOM styling
rules](http://www.html5rocks.com/en/tutorials/webcomponents/shadowdom-201/) for
providing scoped styling of the element's local DOM.  Scoped styles should be
provided via `<style>` tags placed inside the element's local DOM `<template>`.

```html
<dom-module id="my-element">

  <template>

    <style>
      :host {
        display: block;
        border: 1px solid red;
      }
      #child-element {
        background: yellow;
      }
      /* styling elements distributed to content (via ::content) requires */
      /* selecting the parent of the <content> element for compatibility with */
      /* shady DOM . This can be :host or a wrapper element. */
      .content-wrapper ::content > .special {
        background: orange;
      }
    </style>

    <div id="child-element">In local DOM!</div>
    <div class="content-wrapper"><content></content></div>

  </template>

  <script>

      Polymer({
          is: 'my-element'
      });

  </script>

</dom-module>
```

To place styles outside of the element, or share styles between elements, you can create
a [style module](#style-modules).

**Note:**  Prior to Polymer 1.1, the recommendation was to place `<style>` tags
inside the `<dom-module>` for an element (but _outside_ the `<template>`). This
 is still supported, but is no longer recommended.
{.alert .alert-info}


### Styling distributed children (::content)

Under shady DOM, the `<content>` tag doesn't appear in the DOM tree. Styles are rewritten to remove the
`::content` pseudo-element, **and any combinator immediately to the left of `::content`.**

This implies:

*   You must have a selector to the left of the `::content` pseudo-element.

    ```css
    :host ::content div
    ```

    Becomes:

    ```css
    x-foo div
    ```

    (Where `x-foo` is the name of the custom element.)

*   To limit styles to elements inside the ::content tag, add a wrapper element around the
    `<content>` element. This is especially important when using a child combinator (`>`) to
    select top-level children.

    ```html
    <dom-module id="my-element">

      <template>

        <style>
          .content-wrapper ::content > .special {
            background: orange;
          }
        </style>

        <div class="content-wrapper"><content></content></div>

      </template>

    </dom-module>
    ```

    In this case, the rule:

    ```css
    .content-wrapper ::content > .special
    ```

    Becomes:

    ```css
    .content-wrapper > .special
    ```

**Custom properties can't style distributed children.** The Polymer
[custom properties](#xscope-styling-details) shim doesn't support styling
distributed children.
{.alert .alert-info}


## Cross-scope styling {#xscope-styling}


### Background

Shadow DOM (and its approximation via Shady DOM) bring much needed benefits of
scoping and style encapsulation to web development, making it safer and easier
to reason about the effects of CSS on parts of your application.  Styles do not
leak into the local DOM from above, and styles do not leak from one local DOM
into the local DOM of other elements inside.

This is great for *protecting* scopes from unwanted style leakage.  But what
about when you intentionally want to *customize* the style of a custom element's
local DOM, as the user of an element?  This often comes up under the umbrella of
"theming".  For example a "custom-checkbox" element that may internally use a
`.checked` class can protect itself from being affected by CSS from other
components that may also happen to use a `.checked` class.  However, as the user
of the checkbox you may wish to intentionally change the color of the check to
match your product's branding, for example.  The same "protection" that Shadow
DOM provides at the same time introduces a practical barrier to "theming" use
cases.

**Deprecated shadow DOM selectors.** One solution the Shadow DOM spec authors
provided to address the theming problem was the `/deep/` combinator and `::shadow`
pseudo-element, which allowed writing rules that pierce through the Shadow DOM
encapsulation boundary. However, these proved problematic and have been deprecated.
{.alert .alert-info}

<!-- retain legacy anchor -->
<a id="xscope-styling-details"></a>

### Custom CSS properties {#custom-css-properties}

Polymer includes a shim for custom CSS properties inspired by (and compatible with)
the future W3C [CSS Custom Properties for Cascading Variables](http://dev.w3.org/csswg/css-variables/)
specification (see
[Using CSS Variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_variables)
on the Mozilla Developer Network).

Rather than exposing the details of an element's internal implementation for
theming, instead an element author defines one or more custom CSS
properties as part of the element's API.

These custom properties can be defined similarly to other standard CSS properties
and will inherit from the point of definition down the composed DOM tree,
similar to the effect of `color` and `font-family`.

In the simple example below, the author of `my-toolbar` identified the need for
users of the toolbar to be able to change the color of the toolbar title.  The
author exposed a custom property called `--my-toolbar-title-color` which is
assigned to the `color` property of the selector for the title element.  Users
of the toolbar may define this variable in a CSS rule anywhere up the tree, and
the value of the property will inherit down to the toolbar where it is used if
defined, similar to other standard inheriting CSS properties.

Example: { .caption }

```html
<dom-module id="my-toolbar">

  <template>

    <style>
      :host {
        padding: 4px;
        background-color: gray;
      }
      .title {
        color: var(--my-toolbar-title-color);
      }
    </style>

    <span class="title">{{title}}</span>

  </template>

  <script>
    Polymer({
      is: 'my-toolbar',
      properties: {
        title: String
      }
    });
  </script>

</dom-module>
```

Example usage of `my-toolbar`: { .caption }

```html
<dom-module id="my-element">

  <template>

    <style>

      /* Make all toolbar titles in this host green by default */
      :host {
        --my-toolbar-title-color: green;
      }

      /* Make only toolbars with the .warning class red */
      .warning {
        --my-toolbar-title-color: red;
      }

    </style>

    <my-toolbar title="This one is green."></my-toolbar>
    <my-toolbar title="This one is green too."></my-toolbar>

    <my-toolbar class="warning" title="This one is red."></my-toolbar>

  </template>

  <script>
    Polymer({ is: 'my-element'});
  </script>

</dom-module>
```

The `--my-toolbar-title-color` property only affects the color of the title
element encapsulated in `my-toolbar`'s internal implementation.  In the
future the `my-toolbar` author can rename the `title` class or
restructure the internal details of `my-toolbar` without changing the custom
property exposed to users.

You can also include a default value in the `var()` function, to use in case the user
doesn't set the custom property:

```css
color: var(--my-toolbar-title-color, blue);
```

Thus, custom CSS properties introduce a powerful way for element authors to
expose a theming API to their users in a way that naturally fits right alongside
normal CSS styling. It is already on a standards track (currently in the candidate recommendation (CR) stage of the process) with support in Firefox, Safari, and [Chrome 49](https://www.chromestatus.com/features/6401356696911872).

### Custom CSS mixins

It may be tedious (or impossible) for an element author to predict every
CSS property that may be important for theming, let alone expose every
property individually.

The custom properties shim includes an extension that enables an element
author to define a set of CSS properties as a single custom property and
then allow all properties in the set to be applied to a specific CSS rule
in an element's local DOM. The extension enables this with a mixin capability
that is analogous to `var`, but which allows an entire set of properties
to be mixed in. This extension adheres to the
[CSS @apply rule](http://tabatkins.github.io/specs/css-apply-rule/)
proposal.

Use `@apply` to apply a mixin:

<pre><code class="language-css">@apply --<var>mixin-name</var>;</code></pre>

Defining a mixin is just like defining a custom property, but the
value is an object that defines one or more rules:

<pre><code class="language-css"><var>selector</var> {
  --<var>mixin-name</var>: {
    /* rules */
  };
}</code></pre>


Example: { .caption }

```html
<dom-module id="my-toolbar">

  <template>

    <style>
      :host {
        padding: 4px;
        background-color: gray;
        /* apply a mixin */
        @apply --my-toolbar-theme;
      }
      .title {
        @apply --my-toolbar-title-theme;
      }
    </style>

    <span class="title">{{title}}</span>

  </template>

  ...

</dom-module>
```

Example usage of `my-toolbar`: { .caption }

```html
<dom-module id="my-element">

  <template>

    <style>
      /* Apply custom theme to toolbars */
      :host {
        --my-toolbar-theme: {
          background-color: green;
          border-radius: 4px;
          border: 1px solid gray;
        };
        --my-toolbar-title-theme: {
          color: green;
        };
      }

      /* Make only toolbars with the .warning class red and bold */
      .warning {
        --my-toolbar-title-theme: {
          color: red;
          font-weight: bold;
        };
      }
    </style>

    <my-toolbar title="This one is green."></my-toolbar>
    <my-toolbar title="This one is green too."></my-toolbar>

    <my-toolbar class="warning" title="This one is red."></my-toolbar>

  </template>

  <script>
    Polymer({ is: 'my-element'});
  </script>

</dom-module>
```

**Older @apply syntax.** The `@apply` syntax was originally implemented in Polymer using
parenthesis: <code>@apply(<var>--mixin-name</var>)</code>. Polymer 1.6.0 and later accepts `@apply`
without parenthesis, matching the proposal. You can continue using the older syntax in Polymer 1.x,
but starting in Polymer 2.0, only the newer syntax (without parenthesis) is accepted.
{.alert .alert-info}

### Custom property API for Polymer elements {#style-api}

Polymer's custom property shim evaluates and applies custom property values once
at element creation time.  In order to have an element (and its subtree) re-
evaluate custom property values due to dynamic changes such as application of
CSS classes, etc., call the [`updateStyles`](/1.0/docs/api/Polymer.Base#method-updateStyles)
method on the element. To update all elements on the page, you can also call
`Polymer.updateStyles`.

You can  directly modify a Polymer element's custom property by setting
key-value pairs in [`customStyle`](/1.0/docs/api/Polymer.Base#property-customStyle)
on the element (analogous to setting `style`) and then calling `updateStyles`.
Or you can pass a dictionary of property names and values as an argument to
`updateStyles`.

To get the value of a custom property on an element, use
[`getComputedStyleValue`](/1.0/docs/api/Polymer.Base#method-getComputedStyleValue).


Example: { .caption }

```html
<dom-module id="x-custom">

  <template>

    <style>
      :host {
        --my-toolbar-color: red;
      }
    </style>

    <my-toolbar>My awesome app</my-toolbar>
    <button on-tap="changeTheme">Change theme</button>

  </template>

  <script>
    Polymer({
      is: 'x-custom',
      changeTheme: function() {
        this.customStyle['--my-toolbar-color'] = 'blue';
        this.updateStyles();
      }
    });
  </script>

</dom-module>
```

### Custom properties shim limitations

Cross-platform support for custom properties is provided in Polymer by a
JavaScript library that **approximates** the capabilities of the CSS Variables
specification  *for the specific use case of theming custom elements*, while
also extending it to add the capability to mixin property sets to rules as
described above. For performance reasons, Polymer **does
not attempt to replicate all aspects of native custom properties.**
The shim trades off aspects of the full dynamism possible in CSS in the
interests of practicality and performance.

Below are current limitations of the shim. Improvements to performance and
dynamism will continue to be explored.

#### Dynamism limitations

Only property definitions which match the element at *creation time* are applied.
Any dynamic changes that update property values are not applied automatically. You
can force styles to be re-evaluated by calling the
[`updateStyles`](/1.0/docs/api/Polymer.Base#method-updateStyles) method on a
Polymer element, or `Polymer.updateStyles` to update all element
styles.

For example, given this markup inside an element:

HTML: { .caption }

```html
<div class="container">
  <x-foo class="a"></x-foo>
</div>
```

CSS: { .caption }

```css
/* applies */
x-foo.a {
  --foo: brown;
}
/* does not apply */
x-foo.b {
  --foo: orange;
}
/* does not apply to x-foo */
.container {
  --nog: blue;
}
```

After adding class `b` to `x-foo` above, the host element must call `this.updateStyles`
to apply the new styling. This re-calculates and applies styles down the tree from this point.

Dynamic effects **are** reflected at the point of a property's application.

For the following example, adding/removing the `highlighted` class on the `#title` element will
have the desired effect, since the dynamism is related to *application* of a custom property.

```css
#title {
  background-color: var(--title-background-normal);
}

#title.highlighted {
  background-color: var(--title-background-highlighted);
}
```

#### Inheritance limitations

Unlike normal CSS inheritance which flows from parent to child, custom
properties in Polymer's shim can only change when inherited by a custom element
from rules that set properties in scope(s) above it, or in a `:host` rule for
that scope.  **Within a given element's local DOM scope, a custom property can
only have a single value.**  Calculating property changes within a scope would be
prohibitively expensive for the shim and is not required to achieve cross-scope
styling for custom elements, which is the primary goal of the shim.

```html
<dom-module id="my-element">

  <template>

    <style>
     :host {
       --custom-color: red;
     }
     .container {
       /* Setting the custom property here will not change */
       /* the value of the property for other elements in  */
       /* this scope.                                      */
       --custom-color: blue;
     }
     .child {
       /* This will be always be red. */
       color: var(--custom-color);
     }
    </style>

    <div class="container">
      <div class="child">I will be red</div>
    </div>

  </template>

  <script>
    Polymer({ is: 'my-element'});
  </script>

</dom-module>
```

#### Styling distributed elements not supported

The custom properties shim doesn't support styling distributed elements.

```css
/* Not supported */
:host ::content div {
  --custom-color: red;
}
```

## Custom element for document styling (custom-style) {#custom-style}


Polymer provides a `<style is="custom-style">` custom element
for defining styles **in the main document** that can take advantage of several
special features of Polymer's styling system:

*   Document styles defined in a `custom-style` are shimmed to ensure they do
    not leak into local DOM when running on browsers without native Shadow
    DOM.

*   Custom properties used by Polymer's
    [shim for cross-scope styling](#xscope-styling-details) may be defined in an
    `custom-style`. Use the `:root` selector to define custom properties that apply
    to all custom elements.

*   For backwards compatibility, the deprecated `/deep/` combinator and `::shadow`
    pseudo-element are shimmed on browsers without native Shadow DOM. You should avoid
    using these in new code.


Example: { .caption }

```html
<!doctype html>
<html>
<head>
  <script src="components/webcomponentsjs/webcomponents-lite.js"></script>
  <link rel="import" href="components/polymer/polymer.html">

  <style is="custom-style">

    /* Will be prevented from affecting local DOM of Polymer elements */
    * {
      box-sizing: border-box;
    }

    /* Use the :root selector to define custom properties and mixins */
    /* at the document level  */
    :root {
      --my-toolbar-title-color: green;
    }

  </style>

</head>
<body>

    ...

</body>
</html>
```

All features of `custom-style` are available when defining styles as part of
Polymer elements (for example, in `<style>` elements within a custom element's
`<dom-module>`). The exception is the `:root` selector, which is only useful at
the document level. **The `custom-style` extension should only be used for
defining document styles, outside of a custom element's local DOM.**

## Shared styles and external stylesheets {#style-modules}

To share style declarations between elements, you can package a set
of style declarations inside a `<dom-module>` element. In this section,
a `<dom-module>` holding styles is called a _style module_ for convenience.

A style module declares a named set of style rules that can be imported into
an element definition, or into a `custom-style` element.

**Note:** Style modules were introduced in Polymer 1.1;
they replace the experimental support for [external stylesheets](#external-stylesheets).
{.alert .alert-info}

Define a style module inside an HTML import using the `<dom-module>`
element.

```html
<!-- shared-styles.html -->
<dom-module id="shared-styles">
  <template>
    <style>
      .red { color: red; }
    </style>
  </template>
</dom-module>
```

The `id` attribute specifies the name you'll use to reference
your shared styles. Style module names use the same namespace as elements,
so your style modules must have unique names.

Using the shared styles is a two-step process: you need to use a `<link>` tag
to _import_ the module, and a `<style>` tag to _include_ the styles in the correct place.

To use a style module in an element:

```html
<!-- import the module  -->
<link rel="import" href="../shared-styles/shared-styles.html">
<dom-module id="x-foo">
  <template>
    <!-- include the style module by name -->
    <style include="shared-styles"></style>
    <style>:host { display: block; }</style>
    Hi
  </template>
  <script>Polymer({is: 'x-foo'});</script>
</dom-module>
```

You can also use a shared style module in a `custom-style` element.

```html
<!-- import the shared styles  -->
<link rel="import" href="../shared-styles/shared-styles.html">
<!-- include the shared styles -->
<style is="custom-style" include="shared-styles"></style>
```

A single style tag can both `include` shared styles
and define local rules:

```html
<style include="shared-styles">
  :host { display: block; }
</style>
```

(This works for both `custom-style` elements and `<style>` tags inside
custom elements.) The shared styles are applied _before_ the styles defined
inside the body of the `<style>` tag, so the shared styles can be overridden
by the styles defined in the body.

### External stylesheets (deprecated) {#external-stylesheets}

**Deprecated feature.** This experimental feature is now deprecated in favor of
[style modules](#style-modules). It is still supported, but support will
be removed in the future.
{.alert .alert-info}

Polymer includes an experimental feature to support loading external stylesheets
that will be applied to the local DOM of an element.  This is typically
convenient for developers who like to separate styles, share common styles
between elements, or use style pre-processing tools.  The syntax is slightly
different from how stylesheets are typically loaded, as the feature leverages
HTML Imports (or the HTML Imports polyfill, where appropriate) to load the
stylesheet text such that it may be properly shimmed and/or injected as an
inline style.

To include a remote stylesheet that applies to your Polymer element's local DOM,
place a special HTML import `<link>` tag with `type="css"` in your `<dom-
module>` that refers to the external stylesheet to load.

Example: { .caption }

```html
<dom-module id="my-awesome-button">

  <!-- special import with type=css used to load remote CSS
       Note: this style of importing CSS is deprecated -->
  <link rel="import" type="css" href="my-awesome-button.css">

  <template>
    ...
  </template>

  <script>
    Polymer({
      is: 'my-awesome-button',
      ...
    });
  </script>

</dom-module>
```

## Third-party libraries that modify local DOM {#scope-subtree}

If you are using a third-party library that adds local DOM nodes to your
Polymer element, you may notice that styles on the element do not update
properly.

The correct way to add DOM nodes to a Polymer element's local DOM is via
the Polymer [DOM API](local-dom#dom-api). This API lets you manipulate
nodes in a way that respects the local DOM and ensures that styles are
updated properly.

When using third-party libraries that **do not use** the Polymer DOM
API, use the [`scopeSubtree`](/1.0/docs/api/Polymer.Base#method-scopeSubtree)
method to apply proper CSS scoping to a node and all of its descendants.

1.  Create a container node inside your element's local DOM, and have your
    third-party library create DOM under that container node.

    ```html
    <dom-module is="x-example">
      <template>
        <div id="container">
        </div>
      </template>
    </dom-module>
    ```

2.  Call `scopeSubtree` on the container node.

    ```js
    ready: function() {
      this.scopeSubtree(this.$.container, true);
    }
    ```

    `containerNode` is the root node of the tree you wish to scope. Setting
    the second argument to `false` scopes the specified node and descendants
    **once.** Setting it to `true` enables a mutation observer that applies CSS
    scoping whenever `containerNode` or any of its descendants are modified.

**Not for use on Polymer elements.** If the subtree that you scope
contains any Polymer elements with local DOM, `scopeSubtree` will
cause the descendants' local DOM to be styled incorrectly.
{.alert .alert-error}
