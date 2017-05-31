---
title: "Step 2: Add Local DOM"
subtitle: "Build your first Polymer element"
---

接下来，您将创建一个显示图标的简单元素。

在此步骤中，您将了解到：

*   使用 Polymer 创建自定义元素。
*   使用阴影 DOM。

_阴影 DOM_ 是由您的元素管理的一组 DOM 元素。您将在本节中了解更多信息。

在我们的开发者文档中阅读更多关于阴影 DOM 的概念： [阴影 DOM 概念](https://www.polymer-project.org/2.0/docs/devguide/shadow-dom)

## 编辑 icon-toggle.html

打开 `icon-toggle.html `。此文件包含自定义元素的骨架。

与大多数 HTML 文件不同，此文件<em>如果在浏览器中打开，将不会显示任何东西</em>——它仅仅<em>定义</em>了一个新的元素。演示导入了
`icon-toggle.html`，因此可以使用该 `<icon-toggle>`
元素。当您在以下步骤中为元素添加功能时，它们将显示在演示中。

首先看看现有代码：


开始代码——HTML 导入 { .caption }

```html
<link rel="import" href="../polymer/polymer-element.html">
<link rel="import" href="../iron-icon/iron-icon.html">
```

关键信息：

*   `link rel="import"` 元素是一个 <em>HTML 导入</em>，是将资源包含在 HTML 文件中的一种方式。
*   这些行将导入 Polymer 库和另一个自定义元素叫做
    `iron-icon`，您将在此步骤中稍后使用。

**了解更多：HTML 导入。** 请参阅 HTML5Rocks.com 上的 [HTML 导入：用于 Web 的 #include](http://www.html5rocks.com/en/tutorials/webcomponents/imports/)，
以深入讨论HTML导入。
{ .alert .alert-info }

接下来是元素本身的定义：

起始代码——本地 DOM 模板 { .caption }

```html
<dom-module id="icon-toggle">
  <template>
    <style>
      /* 阴影 DOM 样式放在这里 */
      :host {
        display: inline-block;
      }
    </style>
    <!-- 阴影 DOM 放在这里 -->
    <span>Not much here yet.</span>
  </template>
```

关键信息：

*   `<dom-module>` 标签包装了元素的本地 DOM 定义。
    在本例中，`id` 属性显示了这个模块包含一个叫做 `icon-toggle` 的元素的本地 DOM。
*   `<template>` 实际定义元素的本地 DOM 结构和样式。这就是您为自定义元素添加标记的位置。
*   `<template>` 里的 `<style>` 元素让您定义<em>作用域</em>为本地 DOM 的样式，因此它们不会影响文档的其余部分。
*   `:host` 伪类匹配您所定义的自定义元素 (在本例中： `<icon-toggle>`)。这是包含或<em>主有 </em>该本地 DOM 树的元素。

**了解更多：阴影 DOM。** 阴影 DOM 允许您在元素内添加<em>定界的</em> DOM 树，拥有与网页的其余部分解耦的本地样式和标记。
阴影 DOM 基于阴影 DOM 规范，当原生阴影 DOM 可用时，使用原生。
要了解更多信息，请参阅 Polymer 库文档中的 <a href="/2.0/docs/devguide/shadow-dom">阴影 
DOM 概念</a>。
{ .alert .alert-info }

元素定义的末尾是注册元素的一些JavaScript。如果该元素有一个 `<dom-module>`，这个脚本通常放在
`<dom-module>` 的<em>里面</em>，以保持所有东西在一起。


起始代码——元素注册 { .caption }

```html
<script>
  class IconToggle extends Polymer.Element {
    static get is() {
      return "icon-toggle";
    }
    constructor() {
      super();
    }
  }
  customElements.define(IconToggle.is, IconToggle);
</script>
```

Key information:

  * Polymer uses ES6 class syntax. With this code, you extend the base Polymer.Element class to create your own:

    ```
    class IconToggle extends Polymer.Element {...}
    ```

  * You then give your new element a name, so that the browser can recognize it when you use it in tags. This name must match the `id` given in your element's template definition (`<dom-module id="icon-toggle">`).
    
    ```
    static get is() {
      return "icon-toggle";
    }
    ```

  * The element has a constructor:
    
    ```
    constructor() {
      super();
    }
    ```
    
    At the moment, this constructor does nothing. It is included here as a placeholder since we'll use it later.
	
  * At the end of the script, this line calls the "define" method from the Custom Elements API to register your element: 
    
    ```
    customElements.define(IconToggle.is, IconToggle);
    ```

### 创建本地 DOM 结构

Now that you're familiar with the basic layout of the element, add something
useful to its local DOM template.

Find the `<span>` below the  `shadow DOM goes here` comment:

icon-toggle.html—before { .caption }

```html
    <!-- shadow DOM goes here -->
    <span>Not much here yet.</span>
  </template>
```

 Replace the `<span>` and its contents with the `<iron-icon>` tag below:

icon-toggle.html—after { .caption }

```html
    <!-- shadow DOM goes here -->
    <iron-icon icon="polymer">
    </iron-icon>
  </template>
```

Key information:

  * The `<iron-icon>` element is a custom element that renders an icon. Here it's hard-coded to use
an icon named "polymer".

### 样式化本地 DOM

There are a number of new CSS selectors to work with shadow DOM. The `icon-toggle.html ` file already includes a `:host` selector, discussed earlier, to style the top-level `<icon-toggle>` element.

To style the `<iron-icon>` element, add CSS rules inside the `<style>` tag after the existing content.

icon-toggle.html: Before { .caption }

```html
    <style>
      /* shadow DOM styles go here */
      :host {
        display: inline-block;
      }
    </style>
```

icon-toggle.html: After { .caption }

```html
    <style>
      /* shadow DOM styles go here */
      :host {
        display: inline-block;
      }
      iron-icon {
        fill: rgba(0,0,0,0);
        stroke: currentcolor;
      }
      :host([pressed]) iron-icon {
        fill: currentcolor;
      }
    </style>
```

Key information:

*   The `<iron-icon>` tag uses an SVG icon. The `fill`
    and `stroke` properties are SVG-specific CSS properties. They
    set the fill color and the outline color for the icon, respectively.

*   The `:host()` function matches the host element <em>if the
    selector inside the parentheses matches the host element</em>. In this
    case, `[pressed]`is a standard CSS attribute selector, so this
    rule matches when the `icon-toggle` has a `pressed`
    attribute set on it.

Your custom element definition should now look like this:

icon-toggle.html { .caption }

```html
<link rel="import" href="../polymer/polymer-element.html">
<link rel="import" href="../iron-icon/iron-icon.html">
<dom-module id="icon-toggle">
  <template>
    <style>
      /* shadow DOM styles go here */
      :host {
        display: inline-block;
      }
      iron-icon {
        fill: rgba(0,0,0,0);
        stroke: currentcolor;
      }
      :host([pressed]) iron-icon {
        fill: currentcolor;
      }
    </style>
    <!-- shadow DOM goes here -->
    <iron-icon icon="polymer"></iron-icon>
  </template>
  <script>
    class IconToggle extends Polymer.Element {
      static get is() {
      return "icon-toggle";
      }
      constructor() {
        super();
      }
    }
    customElements.define(IconToggle.is, IconToggle);
  </script>
</dom-module>
```

Make sure `polymer serve` is running and reload the demo page. You should see the toggle buttons show up with the hard-coded icon.

<img src="/images/2.0/first-element/hardcoded-toggles.png" alt="Demo showing icon toggles displaying Polymer icon">

You'll notice that one toggle is styled as pressed, because the `pressed`
attribute is set in the demo. But click all you want, the button won't toggle
yet; there's no code to change the `pressed` property.

**If you don't see the new toggles,** double-check your file against the code above. If you see a blank page, make
sure you're clicking on the demo folder or on demo/index.html.
{ .alert .alert-info }

<a class="blue-button" href="intro">Previous step: Intro</a>
<a class="blue-button"
    href="step-3">Next step: Use data binding and properties</a>
