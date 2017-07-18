---
title: Custom element concepts
---

<!-- toc -->

自定义元素为 Web 提供了一套组件模型。自定义元素规范提供：

*   将类与自定义元素名称关联的机制。
*   当自定义元素的实例更改状态（例如，从文档添加或删除）时调用的一组生命周期回调。
*   当实例上的一组特定属性之一更改时，将被调用的一个回调。

放在一起，这些功能可以让您使用元素自己的公共 API 构建一个元素，该 API 对状态更改做出反应。

本文档提供了一份与 Polymer 有关的自定义元素的概述。有关自定义元素的更详细的概述，请参阅：
[自定义元素 v1: 可重用的 Web 组件](https://developers.google.com/web/fundamentals/getting-started/primers/customelements)
于 Web 基础集。

要定义一个自定义元素，您将创建一个 ES6 类并将其与自定义元素名称相关联。

```
// 创建一个类扩展 HTMLElement (直接或非直接)
class MyElement extends HTMLElement { … };

// 把这个新的类与一个元素名相关联
window.customElements.define('my-element', MyElement);
```


您可以像使用标准元素一样使用自定义元素：


```html
<my-element></my-element>
```

或者：

```js
const myEl = document.createElement('my-element');
```

或者：

```js
const myEl = new MyElement();
```

该元素的类定义了它的行为和公共 API。该类必须扩展 `HTMLElement` 或者它的一个子类（例如另一个自定义元素）。

**自定义元素名称。** 按照规范，自定义元素的名称 **必须以小写 ASCII 字母开头，并且必须包含连字符（-）**。
还有一个与已存在的元素名称冲突的被禁用的名称的简短列表。
有关详细信息，请参阅 HTML 规范中的 [自定义元素核心概念](https://html.spec.whatwg.org/multipage/scripting.html#custom-elements-core-concepts)
章节。
{.alert .alert-info}

Polymer 在基本的自定义元素规范之上提供了一组功能。要将这些功能添加到您的元素中，
请扩展 Polymer 的基本元素类 `Polymer.Element`：

```html
<link rel="import" href="/bower_components/polymer/polymer-element.html">

<script>
  class MyPolymerElement extends Polymer.Element {
    ...
  }

  customElements.define('my-polymer-element', MyPolymerElement);
</script>
```

Polymer 为基本的自定义元素添加了一组功能：

*   用于处理常见任务的实例方法。
*   用于处理属物和属性的自动化，例如基于相应属性来设置属物。
*   基于提供的 `<template>` 为元素实例创建阴影 DOM 树。
*   支持数据绑定，属物变更观察者和被计算的属物的数据系统。

## 自定义元素的生命周期 {#element-lifecycle}

The custom element spec provides a set of callbacks called "custom element reactions" that allow you
to run user code in response to certain lifecycle changes.

<table>
  <tr>
   <th>Reaction
   </th>
   <th>Description
   </th>
  </tr>
  <tr>
   <td>constructor
   </td>
   <td>Called when the element is upgraded (that is, when an  element is created, or when a
   previously-created element becomes defined).
   </td>
  </tr>
  <tr>
   <td>connectedCallback
   </td>
   <td>Called when the element is added to a document.
   </td>
  </tr>
  <tr>
   <td>disconnectedCallback
   </td>
   <td>Called when the element is removed from a document.
   </td>
  </tr>
  <!-- <tr>
  <td>adoptedCallback
   </td>
   <td>Called when the element is adopted into a new document.
   </td>
  </tr> -->
  <tr>
   <td>attributeChangedCallback
   </td>
   <td>Called when any of the element's attributes are changed, appended, removed, or replaced,
   </td>
  </tr>
</table>

For each reaction, the first line of your implementation must be a call to the superclass
constructor or reaction. For the constructor, this is simply the `super()` call.

```js
constructor() {
  super();
  // …
}
```

For other reactions, call the superclass method. This is required so Polymer can hook into the
element's lifecycle.

```js
connectedCallback() {
  super.connectedCallback();
  // …
}
```

The element constructor has a few special limitations:

*   The first statement in the constructor body must be a parameter-less call to the `super` method.
*   The constructor can't include a return statement, unless it is a simple early return (`return`
    or `return this`).
*   The constructor can't examine the element's attributes or children, and the constructor can't
    add attributes or children.

For a complete list of limitations, see [Requirements for custom element constructors](https://html.spec.whatwg.org/multipage/scripting.html#custom-element-conformance) in the WHATWG HTML Specification.

Whenever possible, defer work until the `connectedCallback` or later instead of performing it in the constructor.

### 一次性初始化

The custom elements specification doesn't provide a one-time initialization callback. Polymer
provides a `ready` callback, invoked the first time the element is added to the DOM.

```js
ready() {
  super.ready();
  // When possible, use afterNextRender to defer non-critical
  // work until after first paint.
  Polymer.RenderStatus.afterNextRender(this, function() {
    ...
  });
}
```


The `Polymer.Element` class initializes your element's template and data system during the `ready`
callback, so if you override ready, you must call `super.ready()` at some point.

When the superclass `ready` method returns, the element's template has been instantiated and initial
property values have been set. However, light DOM elements may not have been distributed when
`ready` is called.

Don't use `ready` to initialize an element based on dynamic values, like property values or an
element's light DOM children. Instead, use [observers](observers) to react to property changes, and
`observeNodes` or the `slotchange` event to react to children being added and removed from the
element.

Related topics:

*   [DOM templating](dom-template)
*   [Data system concepts](data-system)
*   [Observers and computed properties](observers)
*   [Observe added and removed children](shadow-dom#observe-nodes)

## 元素升级

By specification, custom elements can be used before they're defined. Adding a definition for an
element causes any existing instances of that element to be *upgraded* to the custom class.

For example, consider the following code:

```html
<my-element></my-element>
<script>
  class MyElement extends HTMLElement { ... };

  // ...some time much later...
  customElements.define('my-element', MyElement);
</script>
```


When parsing this page, the browser will create an instance of `<my-element>` before parsing and
executing the script. In this case, the element is created as an instance of `HTMLElement`, not
`MyElement`. After the element is defined, the `<my-element>` instance is upgraded so it has the
correct class (`MyElement`). The class constructor is called during the upgrade process, followed
by any pending lifecycle callbacks.

Element upgrades allow you to place elements in the DOM while deferring the cost of initializing them. It's a progressive enhancement feature.

Elements have a *custom element state* that takes one of the following values:



*   "uncustomized". The element does not have a valid custom element name. It is either a built-in
    element (`<p>`, `<input>`) or an unknown element that cannot become a custom element
    (`<nonsense>`)
*   "undefined". The element has a valid custom element name (such as "my-element"), but has not
    been defined.
*   "custom". The element has a valid custom element name and has been defined and upgraded.
*   "failed". An attempt to upgrade the element failed (for example, because the class was invalid).

The custom element state isn't exposed as a property, but you can style elements depending on
whether they're defined or undefined.

Elements in the "custom" and "uncustomized" state are considered "defined". In CSS you can use the
`:defined` pseudo-class selector to target elements that are defined. You can use this to provide
placeholder styles for elements before they're upgraded:

```
my-element:not(:defined) {
  background-color: blue;
}
```

## 扩展其他元素

In addition to `HTMLElement`, a custom element can extend another custom element:


```
class ExtendedElement extends MyElement {
  static get is() { return 'extended-element'; }

  static get properties() {
    return {
      thingCount: {
        value: 0,
        observer: '_thingCountChanged'
      }
    }
  }
  _thingCountChanged() {
    console.log(`thing count is ${this.thingCount}`);
  }
};

customElements.define(ExtendedElement.is, ExtendedElement);
```

**Polymer does not currently support extending built-in elements.** The custom elements spec
provides a mechanism for extending built-in elements, such as `<button>` and `<input>`. The spec
calls these elements *customized built-in elements*. Customized built-in elements provide many
advantages (for example, being able to take advantage of built-in accessibility features of UI
elements like `<button>` and `<input>`). However, not all browser makers have agreed to support
customized built-in elements, so Polymer does not support them at this time.
{.alert .alert-info}

## 与类表达式混入共享代码 {#mixins}

ES6 classes allow single inheritance, which can make it challenging to share code between different
elements. Class expression mixins let you share code between elements.

A class expression mixin is basically a function that operates as a *class factory*. You pass in a
superclass, and the function generates a new class which extends the superclass with the mixin's
methods.


```js
MyMixin = function(superClass) {
  return class extends superClass {
    constructor() {
      super();
      this.addEventListener('keypress', e => this.handlePress(e));
    }

    static get properties() {
      return {
        bar: {
          type: Object
        }
      };
    }

    static get observers() {
      return [ '_barChanged(bar.*)' ];
    }

    _barChanged(bar) { ... }

    handlePress(e) { console.log('key pressed: ' + e.charCode); }
  }
}
```


The mixin can define properties, observers, and methods just like a regular element class.

Add a mixin to your element like this:

```js
class MyElement extends MyMixin(Polymer.Element) {
  static get is() { return 'my-element' }
}
```

This creates a new class defined by the `MyMixin` factory, so the inheritance hierarchy is:

```
MyElement <= MyMixin(Polymer.Element) <= Polymer.Element
```

You can apply multiple mixins in sequence:

```js
class AnotherElement extends AnotherMixin(MyMixin(Polymer.Element)) { … }
```


## 资源

More information: [Custom elements v1: reusable web components](https://developers.google.com/web/fundamentals/primers/customelements/?hl=en) on Web Fundamentals.
