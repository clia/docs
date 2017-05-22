---
title: Polymer 快速浏览
---

<!-- toc -->

Polymer 使声明性地创建 Web 组件变得简单。

自定义元素可以利用 Polymer 的特殊功能来减少样板，使其更容易构建复杂的互动元素：

- 注册元素
- 生命周期回调
- 属物观察
- 阴影 DOM 模板
- 数据绑定

在本节中，您可以快速浏览 Polymer 库，而无需安装任何内容。单击 **在Plunker上编辑** 按钮打开交互式沙箱中的任何示例。

点击每个功能后面的按钮了解更多信息。

### 注册元素 {#register}

要注册一个新元素，创建 ES6 类扩展
`Polymer.Element`，然后调用 `customElements.define` 方法，该方法在浏览器中 _注册_ 一个新的元素。
注册元素将元素名称与类相关联，因此您可以向自定义元素添加属物和方法。自定义元素的名称 **必须以ASCII字母开头，并包含连接号（-）**。

<demo-tabs selected="0" src="http://plnkr.co/edit/ScvcB4?p=preview">
  <demo-tab heading="custom-element.html">
<pre><code>{{{include_file('2.0/start/samples/custom-element/custom-element.html')}}}</code></pre>
  </demo-tab>
  <demo-tab heading="index.html">
<pre><code>{{{include_file('2.0/start/samples/custom-element/index.html')}}}</code></pre>
  </demo-tab>

  <iframe frameborder="0" src="samples/custom-element/index.html" width="100%" height="40"></iframe>
</demo-tabs>

此示例使用一个生命周期回调把内容添加到 `<custom-element>` 上，在它初始化完成时。
当自定义元素完成其初始化时，`ready` 生命周期回调被调用。
您可以使用 `ready` 回调进行一次性的初始化工作，在元素被创建以后。

<p><a href="/{{{polymer_version_dir}}}/docs/devguide/registering-elements" class="blue-button">
  了解更多：元素注册
</a></p>

<p><a href="/{{{polymer_version_dir}}}/docs/devguide/registering-elements#lifecycle-callbacks" class="blue-button">
  了解更多：生命周期回调
</a></p>

### 添加阴影 DOM

许多元素包括一些内部 DOM 节点来实现元素的 UI 和行为。您可以使用 Polymer 的 DOM 模板化为元素创建一个阴影 DOM 树。

<demo-tabs selected="0" src="http://plnkr.co/edit/DaiLYY?p=preview">
  <demo-tab heading="dom-element.html">
<pre><code>{{{include_file('2.0/start/samples/dom-element/dom-element.html')}}}</code></pre>
  </demo-tab>
  <demo-tab heading="index.html">
<pre><code>{{{include_file('2.0/start/samples/dom-element/index.html')}}}</code></pre>
  </demo-tab>

  <iframe frameborder="0" src="samples/dom-element/index.html" width="100%" height="40"></iframe>
</demo-tabs>

阴影 DOM 被封装在元素内。

<p><a href="/{{{polymer_version_dir}}}/docs/devguide/dom-template" class="blue-button">了解更多：DOM 模板化</a></p>

### 构造阴影 DOM

Shadow DOM lets you control _composition_. The element's children can be _distributed_
so they render as if they were inserted into the shadow DOM tree.

This example creates a simple tag that decorates an image by wrapping it
with a styled `<div>` tag.

<demo-tabs selected="0" src="http://plnkr.co/edit/BzgJBN?p=preview">
  <demo-tab heading="picture-frame.html">
<pre><code>{{{include_file('2.0/start/samples/picture-frame/picture-frame.html')}}}</code></pre>
  </demo-tab>
  <demo-tab heading="index.html">
<pre><code>{{{include_file('2.0/start/samples/picture-frame/index.html')}}}</code></pre>
  </demo-tab>

  <iframe frameborder="0" src="samples/picture-frame/index.html" width="100%" height="60"></iframe>
</demo-tabs>

**Note:** The CSS styles defined inside the `<dom-module>` are _scoped_ to the element's shadow DOM.
So the `div` rule here only affects `<div>` tags inside `<picture-frame>`.
{: .alert .alert-info }

<p><a href="/2.0/docs/devguide/shadow-dom#shadow-dom-and-composition" class="blue-button">
Learn more: Composition & distribution</a></p>

### 使用数据绑定

Of course, it's not enough to have static shadow DOM. You usually want to have your element update
its shadow DOM dynamically.

Data binding is a great way to quickly propagate changes in your element and reduce boilerplate code.
You can bind properties in your component using the "double-mustache" syntax (`{%raw%}{{}}{%endraw%}`).
The `{%raw%}{{}}{%endraw%}` is replaced by the value of the property referenced between the brackets.

<demo-tabs selected="0" src="http://plnkr.co/edit/8mZK8S?p=preview">
  <demo-tab heading="name-tag.html">
<pre><code>{{{include_file('2.0/start/samples/name-tag/name-tag.html')}}}</code></pre>
  </demo-tab>
  <demo-tab heading="index.html">
<pre><code>{{{include_file('2.0/start/samples/name-tag/index.html')}}}</code></pre>
  </demo-tab>

  <iframe frameborder="0" src="samples/name-tag/index.html" width="100%" height="40"></iframe>
</demo-tabs>

<p><a href="/2.0/docs/devguide/data-binding" class="blue-button">
Learn more: data binding</a></p>

### 声明属物

Properties are an important part of an element's public API. Polymer
_declared properties_ support a number of common patterns for properties—setting default
values, configuring properties from markup, observing property changes, and more.

The following example declares the `owner` property from the last example.
It also shows configuring the owner property from markup in `index.html`.

<demo-tabs selected="0" src="http://plnkr.co/edit/ROIvZg?p=preview">
  <demo-tab heading="configurable-name-tag.html">
<pre><code>{{{include_file('2.0/start/samples/configurable-name-tag/configurable-name-tag.html')}}}</code></pre>
  </demo-tab>
  <demo-tab heading="index.html">
<pre><code>{{{include_file('2.0/start/samples/configurable-name-tag/index.html')}}}</code></pre>
  </demo-tab>

  <iframe frameborder="0" src="samples/configurable-name-tag/index.html" width="100%" height="40"></iframe>
</demo-tabs>

<p><a href="/2.0/docs/devguide/properties" class="blue-button">
Learn more: declared properties</a></p>

### 绑定到属物

In addition to text content, you can bind to an element's _properties_ (using
`property-name="[[binding]]"`). Polymer properties
can optionally support two-way binding, using curly braces (`property-name="{{binding}}"`).

This example uses two-way binding: binding the value of a custom input element (`iron-input`)
to the element's `owner` property, so it's updated as the user types.

<demo-tabs selected="0" src="http://plnkr.co/edit/VYR8my?p=preview">
  <demo-tab heading="editable-name-tag.html">
<pre><code>{{{include_file('2.0/start/samples/editable-name-tag/editable-name-tag.html')}}}</code></pre>
  </demo-tab>
  <demo-tab heading="index.html">
<pre><code>{{{include_file('2.0/start/samples/editable-name-tag/index.html')}}}</code></pre>
  </demo-tab>

  <iframe frameborder="0" src="samples/editable-name-tag/index.html" width="100%" height="100"></iframe>
</demo-tabs>

**Note:** The `<iron-input>` element wraps a native `<input>` element and provides two-way
data binding and input validation.
{: .alert .alert-info }

### 使用 `<dom-repeat>` 来进行模板循环

The template repeater (`dom-repeat`) is a specialized template that binds to an array. It creates one instance of the template's contents for each item in the array.

<demo-tabs selected="0" src="http://plnkr.co/edit/FdgkAtcLFHX5TpTsYtZn?p=preview">
  <demo-tab heading="employee-list.html">
<pre><code>{{{include_file('2.0/start/samples/employee-list/employee-list.html')}}}</code></pre>
  </demo-tab>
  <demo-tab heading="index.html">
<pre><code>{{{include_file('2.0/start/samples/employee-list/index.html')}}}</code></pre>
  </demo-tab>

  <iframe frameborder="0" src="samples/employee-list/index.html" width="100%" height="100"></iframe>
</demo-tabs>

<p><a href="/2.0/docs/devguide/templates" class="blue-button">
Learn more: Template repeater</a></p>

## 下一步

Now that you understand these fundamental Polymer concepts, you can [build an app with App Toolbox](/2.0/start/toolbox/set-up) or see a [feature overview of the Polymer library](/2.0/docs/devguide/feature-overview).
