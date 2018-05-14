---
title: 尝试 Polymer
---

<!-- toc -->

Polymer 使声明性地创建 Web 组件变得简单。

新的 Web 开发者能够简单地使用标记来添加自定义 HTML 元素到一个网页上去。这就像您已经熟悉的使用 HTML 标签的用法一样：

```html
<h1>A heading!</h1>
```

```html
<fancy-thing>A fancy thing!</fancy-thing>
```

Experienced web developers can use Polymer's special features to reduce boilerplate
and make it even easier to build complex, interactive elements. In this tour, you'll
learn how to:

- 注册元素
- 使用生命周期回调
- 观察属物
- 使用模板创建阴影 DOM
- 使用数据绑定

In this section you can tour the Polymer library,
without installing anything. Click the **Edit on StackBlitz** button to open any
of the samples in an interactive sandbox.

点击每个功能后面的按钮了解更多信息。

### Register an element {#register}

To register a new element, create an ES6 class that extends
`PolymerElement`, then call the `customElements.define` method, which
_registers_ a new element with the browser. Registering an element associates
an element name with a class, so you can add properties and methods to your custom
element. The custom element's name **must start with an ASCII letter and
contain a dash (-)**.

<demo-tabs selected="0" name="qt-1-register" editor-open-file="custom-element.js" project-path="/3.0/start/samples/custom-element">
  <paper-tab slot="tabs">custom-element.js</paper-tab>
  <div>

```js
<!-- include_file 3.0/start/samples/custom-element/custom-element.js -->
```

  </div>
  <paper-tab slot="tabs">index.html</paper-tab>
  <div>

```html
<!-- include_file 3.0/start/samples/custom-element/index.html -->
```

  </div>
</demo-tabs>

Try it out in **StackBlitz**:
* Try modifying the contents of `this.textContent`.
* If you’re familiar with your browser’s developer tools, try printing the
  custom element’s `tagName` property to the console.
  Hint: add `console.log(this.tagName);` to the constructor method!

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

<demo-tabs selected="0" name="qt-2-shadow-dom" editor-open-file="dom-element.js" project-path="/3.0/start/samples/dom-element">
  <paper-tab slot="tabs">dom-element.js</paper-tab>
  <div>

```js
<!-- include_file 3.0/start/samples/dom-element/dom-element.js -->
```

  </div>
  <paper-tab slot="tabs">index.html</paper-tab>
  <div>

```html
<!-- include_file 3.0/start/samples/dom-element/index.html -->
```

  </div>
</demo-tabs>

Try it out in **StackBlitz**:
* Try adding some other html elements inside the <template></template> block. For example, add `<h1>A heading!</h1>` or `<a href="stuff.html">A link!</a>`

阴影 DOM 被封装在元素内。

<p><a href="/{{{polymer_version_dir}}}/docs/devguide/dom-template" class="blue-button">了解更多：DOM 模板化</a></p>

### 构造阴影 DOM

阴影 DOM 可让您控制 _构造_。元素的子元素可以是 _分布式的_
以让它们可以被渲染成像被插入到阴影 DOM 树中一样。

此示例创建一个简单的标签，通过使用一个样式化的 `<div>` 标签来包装一个图片来装饰该图片。

<demo-tabs selected="0" name="qt-3-compose" editor-open-file="picture-frame.js" project-path="/3.0/start/samples/picture-frame">
  <paper-tab slot="tabs">picture-frame.js</paper-tab>
  <div>

```js
<!-- include_file 3.0/start/samples/picture-frame/picture-frame.js -->
```

  </div>
  <paper-tab slot="tabs">index.html</paper-tab>
  <div>

```html
<!-- include_file 3.0/start/samples/picture-frame/index.html -->
```

  </div>
</demo-tabs>

Try it out in **StackBlitz**:
* Try adding a `<div>` to `index.html`; is it affected by the styles in `<picture-frame>`'s shadow DOM?
* Try adding other HTML elements to the DOM template to see how they are positioned relative to the distributed child nodes.

**注意：**  `<dom-module>` 里面定义的 CSS 样式的 _作用域_ 仅限于元素的阴影 DOM。
所以这里的 `div` 规则仅仅影响 `<picture-frame>` 里的 `<div>` 标签。
{: .alert .alert-info }

<p><a href="/3.0/docs/devguide/shadow-dom#shadow-dom-and-composition" class="blue-button">
Learn more: Composition & distribution</a></p>

### 使用数据绑定

当然，静态阴影 DOM 还不够。您通常想让您的元素动态地更新它的阴影 DOM。

数据绑定是快速传播元素内改变并减少样板代码的好方法。
您可以使用“双胡子”语法 (`{%raw%}{{}}{%endraw%}`) 来绑定组件中的属物。
这 `{%raw%}{{}}{%endraw%}` 由大括号中引用的属物的值所替换。

<demo-tabs selected="0" name="qt-4-data-binding" editor-open-file="name-tag.js" project-path="/3.0/start/samples/name-tag">
  <paper-tab slot="tabs">name-tag.js</paper-tab>
  <div>

```js
<!-- include_file 3.0/start/samples/name-tag/name-tag.js -->
```

  </div>
  <paper-tab slot="tabs">index.html</paper-tab>
  <div>

```html
<!-- include_file 3.0/start/samples/name-tag/index.html -->
```

  </div>
</demo-tabs>

Try it out in **StackBlitz**:
* Try editing the value of the `owner` property.
* Try adding another property and binding it in your component.
  Hint: Add `this.propertyName = 'Property contents';` to the constructor
  and add something like `<p>{{propertyName}}</p>` to the element’s template.

<p><a href="/3.0/docs/devguide/data-binding" class="blue-button">
Learn more: data binding</a></p>

### 声明属物

属物是元素的公共 API 的重要组成部分。Polymer
_声明的属物_ 支持许多常见的用于属物的模式——设置默认值，从标记配置属物，观察属物更改，以及更多。

以下示例声明来自于上一个示例的 `owner` 属物。
它还展示了在 `index.html` 中用标记配置 owner 属物。

<demo-tabs selected="0" name="qt-5-declare-property" editor-open-file="configurable-name-tag.js" project-path="/3.0/start/samples/configurable-name-tag">
  <paper-tab slot="tabs">configurable-name-tag.js</paper-tab>
  <div>

```js
<!-- include_file 3.0/start/samples/configurable-name-tag/configurable-name-tag.js -->
```

  </div>
  <paper-tab slot="tabs">index.html</paper-tab>
  <div>

```html
<!-- include_file 3.0/start/samples/configurable-name-tag/index.html -->
```

  </div>
</demo-tabs>

Try it out in **StackBlitz**:
* Try editing the initial value of `owner` in index.html. Observe how this sets the property directly from your HTML.

<p><a href="/3.0/docs/devguide/properties" class="blue-button">
Learn more: declared properties</a></p>

### 绑定到属物

除文本内容之外，您还可以绑定到元素的 _属物_ (使用
`property-name="[[binding]]"`)。Polymer 属物可以选择性地支持双向绑定，
使用花括号 (`property-name="{{binding}}"`)。

<!--

This example uses two-way binding: binding the value of a property on a parent element to a property
on the child element. When the child element updates the property, the changes are bound to the
parent element.

<demo-tabs selected="0" name="qt-6-bind-property" editor-open-file="parent-element.js" project-path="/3.0/start/samples/parent-element">
  <paper-tab slot="tabs">parent-element.js</paper-tab>
  <div>

```js
<!-- include_file 3.0/start/samples/parent-element/parent-element.js --
```

  </div>
  <paper-tab slot="tabs">child-element.js</paper-tab>
  <div>

```js
<!-- include_file 3.0/start/samples/parent-element/child-element.js --
```

  </div>
  <paper-tab slot="tabs">index.html</paper-tab>
  <div>

```html
<!-- include_file 3.0/start/samples/parent-element/index.html --
```

  </div>
</demo-tabs>

**Note:** `<child-element>` exposes its property to be used in two-way binding by setting the
`reflectToAttribute` and `notify` attributes when the property is declared.
{: .alert .alert-info }
--
<p><a href="/3.0/docs/devguide/data-binding#two-way-bindings" class="blue-button">
Learn more: Two-way binding</a></p>
-->

The following example uses two-way binding: binding the value of a custom input element (`iron-input`)
to the element's `owner` property, so it's updated as the user types.

<demo-tabs selected="0" name="qt-6-bind-property" editor-open-file="editable-name-tag.js" project-path="/3.0/start/samples/editable-name-tag">
  <paper-tab slot="tabs">editable-name-tag.js</paper-tab>
  <div>

```js
<!-- include_file 3.0/start/samples/editable-name-tag/editable-name-tag.js -->
```

  </div>
  <paper-tab slot="tabs">index.html</paper-tab>
  <div>

```html
<!-- include_file 3.0/start/samples/editable-name-tag/index.html -->
```

  </div>
</demo-tabs>

Try it out in **StackBlitz**:
* Edit the placeholder text to see two-way data binding at work.

**注意：** `<iron-input>` 元素包装了原生的 `<input>` 元素，并提供双向数据绑定和输入校验。
{: .alert .alert-info }

<p><a href="/3.0/docs/devguide/data-binding#two-way-bindings" class="blue-button">
Learn more: Two-way binding</a></p>

### Using <dom-repeat> for template repeating

The template repeater (`<dom-repeat>`) is a specialized template that binds to an array. It creates one instance of the template's contents for each item in the array.

<demo-tabs selected="0" name="qt-7-dom-repeat" editor-open-file="employee-list.js" project-path="/3.0/start/samples/employee-list">
  <paper-tab slot="tabs">employee-list.js</paper-tab>
  <div>

```js
<!-- include_file 3.0/start/samples/employee-list/employee-list.js -->
```

  </div>
  <paper-tab slot="tabs">index.html</paper-tab>
  <div>

```html
<!-- include_file 3.0/start/samples/employee-list/index.html -->
```

  </div>
</demo-tabs>

Try it out in **StackBlitz**:
* Change the first and last names inside this.employees
* Add another employee by inserting the following item into the array definition:<br/>
  ```js
     {first: 'Shawna', last: 'Williams'}
  ```

Don't forget to make sure your commas are correct!

<p><a href="/3.0/docs/devguide/templates" class="blue-button">
Learn more: Template repeater</a></p>

## 下一步

Now that you understand these fundamental Polymer concepts, you can [build an app with App Toolbox](/3.0/start/toolbox/set-up) or see a [feature overview of the Polymer library](/3.0/docs/devguide/feature-overview).
