---
title: "Step 4: React to input"
subtitle: "Build your first Polymer element"
---

<!-- toc -->

## 添加事件监听器

当然，一个按钮如果不能点击，那它就不是一个按钮。

To toggle the button, add an event listener. Polymer lets us add event listeners with simple <code>on-<var>event</var></code> annotations in an element's template. Modify your code to use the Polymer `on-click` annotation to listen for the button's `click` event: 

icon-toggle.html { .caption } 

```html
<iron-icon icon="[[toggleIcon]]" on-click="toggle"></iron-icon>
```

**`on-click` is different from `onclick`.** This is different from the [standard <code><var>element</var>.onclick</code> property](https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onclick). The dash in `on-click` indicates a Polymer annotated event listener.
{.alert .alert-info}

The code above calls a method called `toggle` when the button is pressed.  

## Write a method to call when the event occurs

Now, create the `toggle` method to toggle the `pressed` property when the button is pressed. Place the `toggle` method inside the class definition for `IconToggle`, after the constructor.

icon-toggle.html { .caption }

```js
toggle() {
  this.pressed = !this.pressed;
}
```

Your code should now look like this:

icon-toggle.html { .caption }

```html
<script>
  class IconToggle extends Polymer.Element {
    static get is() { 
      return 'icon-toggle';
    }
    static get properties() {
      return {
        pressed: {
          type: Boolean,
          notify: true,
          reflectToAttribute: true,
          value: false
        },
        toggleIcon: {
          type: String
        }
      }
    }
    constructor() {
      super();
    }
    toggle() {
      this.pressed = !this.pressed;
    }
  }

  customElements.define(IconToggle.is, IconToggle);
</script>
```

Save the `icon-toggle.html` file and look at the demo again. You should be able to press the button and see it
toggle between its pressed and unpressed states.

<img src="/images/2.0/first-element/databound-toggles.png" alt="Demo showing icon toggles with star and heart icons.">

**了解更多：数据绑定。** 要了解演示如何工作，请打开 `demo-element.html`
并看一看里面（如果您已下载代码，您将在 `demo` 文件夹中找到该文件。）
是的，该元素的演示 _也是_ 一个元素。
该元素使用 <a href="/2.0/docs/devguide/data-binding#two-way-bindings">双向数据绑定</a> 和
<a href="/2.0/docs/devguide/data-binding#annotated-computed">被计算的绑定</a> 来更改当您切换按钮时显示的字符串。
{ .alert .alert-info }

<a class="blue-button" href="step-3">
  上一步：使用数据绑定和属物
</a>

<a class="blue-button" href="step-5">
  下一步：用自定义 CSS 属物主题化
</a>
