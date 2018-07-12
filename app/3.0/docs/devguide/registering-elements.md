---
title: Define an element
---

<!-- toc -->


## 定义一个自定义元素 {#register-element}


To define a custom element, create a class that extends `PolymerElement` and pass the class to the
`customElements.define` method.

按照规范，自定义元素的名称 **必须以小写 ASCII 字母开头，并且必须包含连字符（-）**。

示例： { .caption }

```js
// Import PolymerElement class
import {PolymerElement} from '@polymer/polymer/polymer-element.js';

// define the element's class element
class MyElement extends PolymerElement {

  // 元素类能定义一些自定义元素的反应
  connectedCallback() {
    super.connectedCallback();
    this.textContent = 'I\'m a custom element!';
    console.log('my-element created!');
  }

  ready() {
    super.ready();
    console.log('my-element is ready!');
  }
}

// 将新类与一个元素名称相关联
customElements.define('my-element', MyElement);

// 用 createElement 创建一个实例：
var el1 = document.createElement('my-element');

// ... 或者使用构造方法：
var el2 = new MyElement();
```

如上所示，元素的类可以定义一些自定义元素反应的回调，如在 [自定义元素生命周期](custom-elements#element-lifecycle) 中所描述的那样。

## 扩展现有元素 {#extend-element}

You can leverage native subclassing support provided by ES6 to extend and customize existing
elements defined using ES6 syntax:

```js
// Subclass existing element
class MyElementSubclass extends MyElement {
  static get is() { return 'my-element-subclass'; }
  static get properties() { ... }
  constructor() {
    super();
    ...
  }
  ...
}

// Register custom element definition using standard platform API
customElements.define(MyElementSubclass.is, MyElementSubclass);
```

For more information on extending elements, see [Extending other elements](custom-elements#extending-elements)
in Custom element concepts.

If you don't provide a template for your subclass, it inherits the superclass's template by default.
For more information, see [Inherit a template from another Polymer element](dom-template#inherit).

## 使用混入

You can share code using _class expression mixins_. You use a mixin to add new features on top of a base class:

```js
class MyElementWithMixin extends MyMixin(PolymerElement) {

}
```

This pattern may be easier to understand if you think of it as two steps:

```js
// Create a new base class that adds MyMixin's features to Polymer.Element
const BaseClassWithMixin = MyMixin(PolymerElement);

// Extend the new base class
class MyElementWithMixin extends BaseClassWithMixin { ... }
```

Because mixins are simply adding classes to the inheritance chain, all of the usual rules of
inheritance apply.

For information on defining mixins, see [Sharing code with class expression mixins](custom-elements#mixins)
in Custom element concepts.


## Using legacy behaviors with class-style elements

You can add legacy behaviors to your class-style element using the `mixinBehaviors` function:

```js
import {mixinBehaviors} from '@polymer/polymer/lib/legacy/class.js';
import {PolymerElement} from '@polymer/polymer/polymer-element.js';
import {MyBehavior} from './my-behavior.js'
import {MyBehavior2} from './my-behavior-2.js';

class XClass extends mixinBehaviors([MyBehavior, MyBehavior2], PolymerElement) {
  ...
}
customElements.define('x-class', XClass);
```

The `mixinBehaviors` function also mixes in the Legacy APIs, the same as if you applied the
`LegacyElementMixin`. These APIs are required since since legacy behaviors depend on them.

