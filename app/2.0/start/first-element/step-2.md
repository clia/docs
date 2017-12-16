---
title: "Step 2: Add Shadow DOM"
subtitle: "Build your first Polymer element"
---

<!-- toc -->

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

起始代码——阴影 DOM 模板 { .caption }

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

*   `<dom-module>` 标签包装了元素的阴影 DOM 定义。
    在本例中，`id` 属性显示了这个模块包含一个叫做 `icon-toggle` 的元素的阴影 DOM。
*   `<template>` 实际定义元素的阴影 DOM 结构和样式。这就是您为自定义元素添加标记的位置。
*   `<template>` 里的 `<style>` 元素让您定义<em>作用域</em>为阴影 DOM 的样式，因此它们不会影响文档的其余部分。
*   `:host` 伪类匹配您所定义的自定义元素 (在本例中： `<icon-toggle>`)。这是包含或<em>主有 </em>该阴影 DOM 树的元素。

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

关键信息：

  * Polymer 使用 ES6 的类语法。使用此代码，您可以扩展基础 Polymer.Element 类来创建您自己的：

    ```
    class IconToggle extends Polymer.Element {...}
    ```

  * 然后，您为新的元素赋予一个名称，以便您在标签中使用它时浏览器可以识别它。该名称必须与您元素的模板定义 (`<dom-module id="icon-toggle">`) 中给定的 `id` 相匹配。
    
    ```
    static get is() {
      return "icon-toggle";
    }
    ```

  * 元素有一个构造函数：
    
    ```
    constructor() {
      super();
    }
    ```
    
    目前，这个构造函数什么都不做。它被包括在这里作为占位符，因为我们稍后会使用它。
	
  * 在脚本结尾处，此行从自定义元素 API 中调用 “define” 方法来注册您的元素：
    
    ```
    customElements.define(IconToggle.is, IconToggle);
    ```

### 创建阴影 DOM 结构

现在，您已经熟悉了元素的基本布局，下面为其阴影 DOM 模板添加一些有用的东西。

找到  `阴影 DOM 放在这里` 注释下面的 `<span>` ：

icon-toggle.html—before { .caption }

```html
    <!-- 阴影 DOM 放在这里 -->
    <span>Not much here yet.</span>
  </template>
```

 将 `<span>` 其及其内容替换为以下的 `<iron-icon>` 标签：

icon-toggle.html—after { .caption }

```html
    <!-- 阴影 DOM 放在这里 -->
    <iron-icon icon="polymer">
    </iron-icon>
  </template>
```

关键信息：

  * `<iron-icon>` 元素是呈现图标的自定义元素。这里用硬编码的方式来使用一个叫做 "polymer" 的图标。

### 样式化阴影 DOM

有一些新的 CSS 选择器可以用于处理阴影 DOM。前面讨论过，`icon-toggle.html ` 文件已经包括一个 `:host` 选择器，用来样式化顶级的 `<icon-toggle>` 元素。

要样式化 `<iron-icon>` 元素，在 `<style>` 标签内的现有内容之后添加 CSS 规则。

icon-toggle.html: 之前 { .caption }

```html
    <style>
      /* 阴影 DOM 样式放在这里 */
      :host {
        display: inline-block;
      }
    </style>
```

icon-toggle.html: 之后 { .caption }

```html
    <style>
      /* 阴影 DOM 样式放在这里 */
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

关键信息：

*   `<iron-icon>` 标签采用了 SVG 图标。`fill`
    和 `stroke` 属物是特定于 SVG 的 CSS 属物。
    它们分别设置图标的填充颜色和轮廓颜色。

*   <em>当 `:host()` 函数括号内的选择器匹配宿主元素时</em>，`:host()` 函数匹配宿主元素。
    在这种情况下，`[pressed]` 是一个标准的 CSS 属性选择器，所以当 `icon-toggle` 有一个 `pressed` 属性设置在上面时，
    该规则就匹配了。

您的自定义元素定义现在应如下所示：

icon-toggle.html { .caption }

```html
<link rel="import" href="../polymer/polymer-element.html">
<link rel="import" href="../iron-icon/iron-icon.html">
<dom-module id="icon-toggle">
  <template>
    <style>
      /* 阴影 DOM 样式放在这里 */
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
    <!-- 阴影 DOM 放在这里 -->
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

确保 `polymer serve` 正在运行并重新加载演示页面。您应该看到切换按钮处显示的硬编码的图标。

<img src="/images/2.0/first-element/hardcoded-toggles.png" alt="Demo showing icon toggles displaying Polymer icon">

您将注意到，一个切换按钮的样式是按下的，因为在这个演示中 `pressed` 属性是被设置的。
但点击所有您想要的，该按钮不会切换; 没有代码来更改 `pressed` 属物。

**如果没有看到新的切换按钮，** 请根据上面的代码仔细检查文件。如果您看到空白页面，
请确保您点击的是 demo 文件夹或 demo/index.html。
{ .alert .alert-info }

<a class="blue-button" href="intro">上一步：简介</a>
<a class="blue-button"
    href="step-3">下一步：使用数据绑定和属物</a>
