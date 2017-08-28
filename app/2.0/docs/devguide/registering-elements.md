---
title: Define an element
---

<!-- toc -->


## 定义一个自定义元素 {#register-element}


要定义一个自定义元素，创建一个类扩展 `Polymer.Element` 并将该类传递给 `customElements.define` 方法。

按照规范，自定义元素的名称 **必须以小写 ASCII 字母开头，并且必须包含连字符（-）**。

示例： { .caption }

```
// 定义元素的类元素
class MyElement extends Polymer.Element {

  // 元素类能定义一些自定义元素的反应
  connectedCallback() {
    super.connectedCallback();
    console.log('my-element created!');
  }

  ready() {
    super.ready();
    this.textContent = 'I\'m a custom element!';
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
To override this behavior, or modify the superclass template, override the subclass's `template`
getter.

## 使用混入

You can share code using _mixins_. You use a mixin to add new features on top of a base class:

```js
class MyElementWithMixin extends MyMixin(Polymer.Element) {

}
```

This pattern may be easier to understand if you think of it as two steps:

```js
// Create a new base class that adds MyMixin's features to Polymer.Element
const BaseClassWithMixin = MyMixin(Polymer.Element);

// Extend the new base class
class MyElementWithMixin extends BaseClassWithMixin { ... }
```

Because mixins are simply adding classes to the inheritance chain, all of the usual rules of
inheritance apply.

For information on defining mixins, see [Sharing code with class expression mixins](custom-elements#mixins)
in Custom element concepts.

## 导入和 API

There are three main HTML imports for defining Polymer elements:

| Import | Description |
|---|-------|
| `polymer-element.html` | Defines the `Polymer.Element` base class.  |
| `legacy-element.html` | Defines the `Polymer.LegacyElementMixin` base class, which can be used to add 1.x compatible legacy API to `Polymer.Element`. Also defines the legacy `Polymer()` factory method for creating hybrid elements. (Includes `polymer-element.html`.)|
| `polymer.html` | Includes the previous imports plus the helper elements (`custom-style`, `dom-bind`, `dom-if`, and `dom-repeat`) that were included in the 1.x `polymer.html` bundle. |

For the smallest footprint, use the `polymer-element.html` import and import any required helper
elements separately.

If you need some of the backwards-compabile APIs from 1.x, you can use the `Polymer.LegacyElement`
class as the base for 2.x class-style elements. You must still import any helper elements you
use individually.

Use the `polymer.html` import for defining hybrid elements that can run under both 1.x and 2.x.



## 在类风格的元素上使用混合行为

You can add hybrid behaviors to your class-style element using the `Polymer.mixinBehavior` function:

```
class XClass extends Polymer.mixinBehaviors([MyBehavior, MyBehavior2], Polymer.Element) {

  ...
}
customElements.define('x-class', XClass);
```

The `mixinBehavior` function also mixes in the Legacy APIs, the same as if you extended
`Polymer.LegacyElement`. These APIs are required since since hybrid behaviors depend on them.

## 在主 HTML 文档中定义一个元素 {#main-document-definitions}

You should only define elements from the main document when
experimenting. In production, elements should always be defined in
separate files and imported into your main document.

To define an element in your main HTML document, define the element
from `HTMLImports.whenReady(callback)`. `callback` is invoked when
all imports in the document have finished loading.

```
<!DOCTYPE html>
<html>
  <head>
    <script src="bower_components/webcomponentsjs/webcomponents-lite.js">
    </script>
    <link rel="import" href="bower_components/polymer/polymer-element.html">
    <title>Defining a Polymer Element from the Main Document</title>
  </head>
  <body>
    <dom-module id="main-document-element">
      <template>
        <p>
          Hi! I'm a Polymer element that was defined in the
          main document!
        </p>
      </template>
      <script>
        HTMLImports.whenReady(function() {
          class MainDocumentElement extends Polymer.Element {

            static get is() { return 'main-document-element'; }

          }
          window.customElements.define(MainDocumentElement.is, MainDocumentElement);
        });
      </script>
    </dom-module>
    <main-document-element></main-document-element>
  </body>
</html>
```

## 定义遗留元素 {#legacy-element}

Legacy elements can use use the `Polymer` function to register an element.
The function takes as its argument the  prototype for the new element. The prototype
must have an `is` property that specifies the HTML tag name for your custom element.

By specification, the custom element's name **must start with an ASCII letter and contain a dash (-)**.

Example: { .caption }

```
    // register an element
    MyElement = Polymer({

      is: 'my-element',

      // See below for lifecycle callbacks
      created: function() {
        this.textContent = 'My element!';
      }

    });

    // create an instance with createElement:
    var el1 = document.createElement('my-element');

    // ... or with the constructor:
    var el2 = new MyElement();
```

The `Polymer` function registers the element with the browser and returns a
constructor that can be used to create new instances of your element via code.

The `Polymer` function sets up the prototype chain for your custom element,
chaining it to the Polymer `Base` prototype (which provides
Polymer value-added features), so you cannot set up your own
prototype chain. However, you can use [behaviors](#prototype-mixins) to
share code between elements.

## 生命周期回调 {#lifecycle-callbacks}

The Polymer.Element class implements the standard Custom Element lifecycle
callbacks to perform tasks necessary for Polymer's built-in features.

Polymer adds an extra callback, `ready`, which is invoked when Polymer has
finished creating and initializing the element's DOM.

<table>
  <tr>
    <th>Legacy callback</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>created</code></td>
    <td>Called when the element has been created, but before property values are
       set and local DOM is initialized.
      <p>Use for one-time set-up before property values are set.
      </p>
      <p>Equivalent to the native constructor.
      </p>
    </td>
  </tr>
  <tr>
    <td><code>ready</code></td>
    <td>Called after property values are set and local DOM is initialized.
      <p>Use for one-time configuration of your component after local
        DOM is initialized. (For configuration based on property values, it
        may be preferable to use an <a href="observers">observer</a>.)
      </p>
    </td>
  </tr>
  <tr>
    <td><code>attached</code></td>
    <td>Called after the element is attached to the document. Can be called multiple
        times during the lifetime of an element. The first <code>attached</code> callback
        is guaranteed not to fire until after <code>ready</code>.
      <p>Uses include adding document-level event listeners. (For listeners local to the element, you can use declarative
        event handling, such as <a href="events.html#annotated-listeners">annotated
        event listeners</a> or the
        <a href="events#event-listeners"><code>listeners</code> object</a>.)</p>
     <p>Equivalent to native <code>connectedCallback</code>.</p>
      </p>
    </td>
  </tr>
  <tr>
    <td><code>detached</code></td>
    <td>Called after the element is detached from the document. Can be called
        multiple times during the lifetime of an element.
      <p>Uses include removing event listeners added in <code>attached</code>.
      </p>
      <p>Equivalent to native <code>disconnectedCallback</code>.</p>
      </p>
    </td>
  </tr>
  <tr>
    <td><code>attributeChanged</code></td>
    <td>Called when one of the element's attributes is changed.
      <p>Use to handle attribute changes that <em>don't</em> correspond to
        declared properties. (For declared properties, Polymer
        handles attribute changes automatically as described in
        <a href="properties#attribute-deserialization">attribute deserialization</a>.)
      </p>
      <p>Equivalent to the native <code>attributeChangedCallback</code>.
      </p>
    </td>
  </tr>
</table>

### 遗留的行为 {#prototype-mixins}

Legacy elements can share code in the form of _behaviors_, which can define
properties, lifecycle callbacks, event listeners, and other features.

For more information, see [Behaviors](/1.0/docs/devguide/behaviors) in the Polymer 1.x docs.
