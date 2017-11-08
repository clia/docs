---
title: 尝试 Polymer
---

<!-- toc -->

Polymer 使声明性地创建 Web 组件变得简单。

新的 Web 开发者能够简单地使用标记来添加自定义 HTML 元素到一个网页上去。这就像您已经熟悉的使用 HTML 标签的用法一样：

<pre><code>&lt;h1&gt;A heading!&lt;/h1&gt;</code></pre>

<pre><code>&lt;fancy-thing&gt;A fancy thing!&lt;/fancy-thing&gt;</code></pre>


有经验的 Web 开发者能够使用 Polymer 的特殊功能来减少样板代码，使构建复杂的、交互的元素变得更容易。
在这个教程中，您将学会如何：

- 注册元素
- 使用生命周期回调
- 观察属物
- 使用模板创建阴影 DOM
- 使用数据绑定

在本节中，您可以快速浏览 Polymer 库，而无需安装任何内容。单击 **在Plunker上编辑** 按钮打开交互式沙箱中的任何示例。

点击每个功能后面的按钮了解更多信息。

### 注册元素 {#register}

要注册一个新元素，创建 ES6 类扩展
`Polymer.Element`，然后调用 `customElements.define` 方法，该方法在浏览器中 _注册_ 一个新的元素。
注册元素将元素名称与类相关联，因此您可以向自定义元素添加属物和方法。自定义元素的名称 **必须以ASCII字母开头，并包含连接号（-）**。

<demo-tabs selected="0" name="qt-1-register" src="http://plnkr.co/edit/Q4E8zO?p=preview">
  <demo-tab slot="demo-tab" heading="custom-element.html">
<pre><code>{{{include_file('2.0/start/samples/custom-element/custom-element.html')}}}</code></pre>
  </demo-tab>
  <demo-tab slot="demo-tab" heading="index.html">
<pre><code>{{{include_file('2.0/start/samples/custom-element/index.html')}}}</code></pre>
  </demo-tab>

  <iframe frameborder="0" src="samples/custom-element/index.html" width="100%" height="40"></iframe>
</demo-tabs>

在 **Plunker** 上尝试：
* 尝试更改 `this.textContent` 的内容。
* 如果您熟悉您的浏览器的开发者工具，尝试在控制台里面打印该自定义元素的 `tagName` 属物。
  提示：添加 `console.log(this.tagName);` 到构造方法里！

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

<demo-tabs selected="0" name="qt-2-shadow-dom" src="http://plnkr.co/edit/buPxSJ?p=preview">
  <demo-tab slot="demo-tab" heading="dom-element.html">
<pre><code>{{{include_file('2.0/start/samples/dom-element/dom-element.html')}}}</code></pre>
  </demo-tab>
  <demo-tab slot="demo-tab" heading="index.html">
<pre><code>{{{include_file('2.0/start/samples/dom-element/index.html')}}}</code></pre>
  </demo-tab>

  <iframe frameborder="0" src="samples/dom-element/index.html" width="100%" height="40"></iframe>
</demo-tabs>

在 **Plunker** 上尝试：
* 尝试在 <template></template> 块中添加一些其他 HTML 元素。例如，添加 `<h1>A heading!</h1>` 或 `<a href=”stuff.html”>A link!</a>`

阴影 DOM 被封装在元素内。

<p><a href="/{{{polymer_version_dir}}}/docs/devguide/dom-template" class="blue-button">了解更多：DOM 模板化</a></p>

### 构造阴影 DOM

阴影 DOM 可让您控制 _构造_。元素的子元素可以是 _分布式的_
以让它们可以被渲染成像被插入到阴影 DOM 树中一样。

此示例创建一个简单的标签，通过使用一个样式化的 `<div>` 标签来包装一个图片来装饰该图片。

<demo-tabs selected="0" name="qt-3-compose" src="http://plnkr.co/edit/KvBnmE?p=preview">
  <demo-tab slot="demo-tab" heading="picture-frame.html">
<pre><code>{{{include_file('2.0/start/samples/picture-frame/picture-frame.html')}}}</code></pre>
  </demo-tab>
  <demo-tab slot="demo-tab" heading="index.html">
<pre><code>{{{include_file('2.0/start/samples/picture-frame/index.html')}}}</code></pre>
  </demo-tab>

  <iframe frameborder="0" src="samples/picture-frame/index.html" width="100%" height="60"></iframe>
</demo-tabs>

在 **Plunker** 上尝试：
* 尝试添加 `<div>` 到 `index.html`；它是否受 `<picture-frame>` 的阴影 DOM 里的样式影响？
* 尝试添加其他 HTML 元素到 DOM 模板中，以观察它们如何相对于那些分布的子节点来定位。

**注意：**  `<dom-module>` 里面定义的 CSS 样式的 _作用域_ 仅限于元素的阴影 DOM。
所以这里的 `div` 规则仅仅影响 `<picture-frame>` 里的 `<div>` 标签。
{: .alert .alert-info }

<p><a href="/2.0/docs/devguide/shadow-dom#shadow-dom-and-composition" class="blue-button">
了解更多：构造和分布</a></p>

### 使用数据绑定

当然，静态阴影 DOM 还不够。您通常想让您的元素动态地更新它的阴影 DOM。

数据绑定是快速传播元素内改变并减少样板代码的好方法。
您可以使用“双胡子”语法 (`{%raw%}{{}}{%endraw%}`) 来绑定组件中的属物。
这 `{%raw%}{{}}{%endraw%}` 由大括号中引用的属物的值所替换。

<demo-tabs selected="0" name="qt-4-data-binding" src="http://plnkr.co/edit/8mZK8S?p=preview">
  <demo-tab slot="demo-tab" heading="name-tag.html">
<pre><code>{{{include_file('2.0/start/samples/name-tag/name-tag.html')}}}</code></pre>
  </demo-tab>
  <demo-tab slot="demo-tab" heading="index.html">
<pre><code>{{{include_file('2.0/start/samples/name-tag/index.html')}}}</code></pre>
  </demo-tab>

  <iframe frameborder="0" src="samples/name-tag/index.html" width="100%" height="40"></iframe>
</demo-tabs>

Try it out in **Plunker**:
* Try editing the value of the `owner` property.
* Try adding another property and binding it in your component. 
  Hint: Add `this.propertyName = "Property contents";` to the constructor
  and add {{propertyName}} to the element’s shadow DOM.  

<p><a href="/2.0/docs/devguide/data-binding" class="blue-button">
了解更多：数据绑定</a></p>

### 声明属物

属物是元素的公共 API 的重要组成部分。Polymer
_声明的属物_ 支持许多常见的用于属物的模式——设置默认值，从标记配置属物，观察属物更改，以及更多。

以下示例声明来自于上一个示例的 `owner` 属物。
它还展示了在 `index.html` 中用标记配置 owner 属物。

<demo-tabs selected="0" name="qt-5-declare-property" src="http://plnkr.co/edit/3Nz8GL?p=preview">
  <demo-tab slot="demo-tab" heading="configurable-name-tag.html">
<pre><code>{{{include_file('2.0/start/samples/configurable-name-tag/configurable-name-tag.html')}}}</code></pre>
  </demo-tab>
  <demo-tab slot="demo-tab" heading="index.html">
<pre><code>{{{include_file('2.0/start/samples/configurable-name-tag/index.html')}}}</code></pre>
  </demo-tab>

  <iframe frameborder="0" src="samples/configurable-name-tag/index.html" width="100%" height="40"></iframe>
</demo-tabs>

Try it out in **Plunker**:
* Try editing the initial value of `owner` in index.html. Observe how this sets the property directly from your HTML.

<p><a href="/2.0/docs/devguide/properties" class="blue-button">
了解更多：声明的属物</a></p>

### 绑定到属物

除文本内容之外，您还可以绑定到元素的 _属物_ (使用
`property-name="[[binding]]"`)。Polymer 属物可以选择性地支持双向绑定，
使用花括号 (`property-name="{{binding}}"`)。

的值绑定到元素的 (`iron-input`)
的值绑定到元素的 `owner` 属物，因此它将在用户输入时进行更新。

<demo-tabs selected="0" name="qt-6-bind-property" src="http://plnkr.co/edit/03HGzn98uIN5I1WgkDwu?p=preview">
  <demo-tab slot="demo-tab" heading="editable-name-tag.html">
<pre><code>{{{include_file('2.0/start/samples/editable-name-tag/editable-name-tag.html')}}}</code></pre>
  </demo-tab>
  <demo-tab slot="demo-tab" heading="index.html">
<pre><code>{{{include_file('2.0/start/samples/editable-name-tag/index.html')}}}</code></pre>
  </demo-tab>

  <iframe frameborder="0" src="samples/editable-name-tag/index.html" width="100%" height="100"></iframe>
</demo-tabs>

在 **Plunker** 上尝试：
* 编辑占位符文本以观察双向数据绑定如何工作的。

**注意：** `<iron-input>` 元素包装了原生的 `<input>` 元素，并提供双向数据绑定和输入校验。
{: .alert .alert-info }

### 使用 `<dom-repeat>` 来进行模板循环

模板重复器 (`dom-repeat`) 是一个绑定到数组的专用模板。它为数组中的每个项创建模板内容的一个实例。

<demo-tabs selected="0" name="qt-7-dom-repeat" src="http://plnkr.co/edit/FdgkAtcLFHX5TpTsYtZn?p=preview">
  <demo-tab slot="demo-tab" heading="employee-list.html">
<pre><code>{{{include_file('2.0/start/samples/employee-list/employee-list.html')}}}</code></pre>
  </demo-tab>
  <demo-tab slot="demo-tab" heading="index.html">
<pre><code>{{{include_file('2.0/start/samples/employee-list/index.html')}}}</code></pre>
  </demo-tab>

  <iframe frameborder="0" src="samples/employee-list/index.html" width="100%" height="100"></iframe>
</demo-tabs>

在 **Plunker** 上尝试：
* 更改 this.employees 中的名字和姓氏
* 在 Tony Morelli 之后，通过将以下文本插入数组定义添加另一名员工:<br/>
  ```
     {first: 'Shawna', last: 'Williams'} 
  ```

<p><a href="/2.0/docs/devguide/templates" class="blue-button">
了解更多：模板重复器</a></p>

## 下一步

现在您已经了解了这些基本的 Polymer 概念，您可以 [使用 App 工具箱创建 App](/2.0/start/toolbox/set-up) 或查看 [Polymer 库的功能概述](/2.0/docs/devguide/feature-overview)。
