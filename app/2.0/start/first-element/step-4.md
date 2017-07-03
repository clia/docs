---
title: "Step 4: React to input"
subtitle: "Build your first Polymer element"
---

当然，一个按钮如果不能点击，那它就不是一个按钮。

要切换按钮，我们将添加一个事件监听器。为了确保手势事件在不同浏览器上的运行方式相同，我们将使用 `GestureEventListeners` 混入。
这个混入提供了一个在桌面浏览器上像标准点击事件一样工作的 tap 事件，就像移动浏览器上的原生 tap 事件一样。

混入是一个定义一组相关函数并且永远不会被实例化的类。当您使用混入类时，您只继承其行为。
有关更多信息，请参阅 Justin Fagnani 的博客文章：[JavaScript 类的"真正的"混入](http://justinfagnani.com/2015/12/21/real-mixins-with-javascript-classes/)。

通过在 `icon-toggle.html` 中的 HTML 导入声明中添加以下代码来导入 `Polymer.GestureEventListeners` 混入：

 icon-toggle.html { .caption }

```html
<link rel="import" href="../polymer/polymer-element.html">
<link rel="import" href="../polymer/lib/mixins/gesture-event-listeners.html">
<link rel="import" href="../iron-icon/iron-icon.html">
```

在类声明中使用混入：

```html
<script>
  class IconToggle extends Polymer.GestureEventListeners(Polymer.Element) {
  ...
</script>
```

要切换按钮，请添加事件监听器。要在宿主元素上添加事件监听器（这个例子中：
`icon-toggle`），请将该监听器置于构造函数中其现有内容之后：

icon-toggle.html: 之前 { .caption }

```html
constructor() {
  super();
}
```

  icon-toggle.html: 之后 { .caption }

```html
constructor() {
  super();
  Polymer.Gestures.addListener(this, 'tap', () => this.toggle());
}
```

使用手势事件时，您可以使用 `Polymer.Gestures.addListener` 方法来替换标准的 `addEventListener` 方法。

添加一个方法来在按钮被按下时切换 `pressed` 属物。
将它放在 `IconToggle` 类的定义中，在构造函数之后。

icon-toggle.html { .caption }

```html
    toggle() {
      this.pressed = !this.pressed;
    }
```

您的代码现在应该是这样的：

icon-toggle.html { .caption }

```html
<script>
  class IconToggle extends Polymer.GestureEventListeners(Polymer.Element) {
    static get is() {
    return "icon-toggle";
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
        },
      }
    }
    constructor() {
      super();
      this.addEventListener('tap', 'toggle');
      Polymer.Gestures.addListener(this, 'tap', () => this.toggle());
    }
    toggle() {
      this.pressed = !this.pressed;
    }
  }
  customElements.define(IconToggle.is, IconToggle);
</script>
```

关键信息：

*   对于基于 Polymer.Element 的类风格的元素，您需要通过导入和使用 Polymer.GestureEventListeners 混入来显式添加手势支持：

    ```html
    <link rel="import" href="polymer/lib/mixins/gesture-event-listeners.html">
    ````

*   使用标准的 `addEventListener` 方法来命令式地添加事件监听器。

*   当用户用鼠标点击目标或是用手指点按目标时，`tap` 事件就被 Polymer 的 [手势系统](/2.0/docs/devguide/gesture-events) 生成了。

保存 `icon-toggle.html` 文件并再次查看演示。您应该能够按下按钮，看到它在其按压状态和未按压状态之间切换。

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
