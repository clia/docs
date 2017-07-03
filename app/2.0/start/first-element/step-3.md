---
title: "Step 3: Use data binding and properties"
subtitle: "Build your first Polymer element"
---

现在，这个元素并没有做多少事。在此步骤中，您将给它一个基本的 API，
允许您从标记中使用属性，或是从 JavaScript 中使用属物，来配置图标。

首先，来一点数据绑定。我们将创建一个 `toggleIcon` 属物，您能在 HTML 标记中使用，如下所示：

```html
<iron-icon icon="[[toggleIcon]]"></iron-icon>
```

在这个起作用之前，我们需要将 toggleIcon 声明为属物。

接下来，添加 `toggleIcon` 属物声明。

找到脚本标签，并将以下属物添加到元素的类定义中：

icon-toggle.html: 之前 { .caption }

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
icon-toggle.html: 之后 { .caption }

```html
<script>
  class IconToggle extends Polymer.Element {
    static get is() {
    return "icon-toggle";
    }
    static get properties() {
      return {
        toggleIcon: {
          type: String
        },
      }
    }
    constructor() {
      super();
    }
  }
  customElements.define(IconToggle.is, IconToggle);
</script>
```

关键信息：

  * 您必须声明一个属物才能在 HTML 中使用它。
  * 像这样一个简单的属物声明只包括类型（在这个例子中：`String`）。

**了解更多：反序列化属性。** 声明的属物类型将影响到 Polymer 如何把属性值（始终是一个字符串值）转换或是<em>反序列化</em>
为一个 JavaScript 属物值。
默认的是 `String`，所以此处 `toggleIcon` 的声明仅仅是走个形式。
要了解更多信息，请参阅 Polymer 文档中的 <a href="/2.0/docs/devguide/properties#attribute-deserialization">属性反序列化
</a>。
{ .alert .alert-info }

现在找到 `<iron-icon>` 元素并将 `icon` 属性的值从 `"polymer"` 改为  "`[[toggleIcon]]`"。

icon-toggle.html { .caption }

```html
<!-- 本地 DOM 放在这里 -->
<iron-icon icon="[[toggleIcon]]">
</iron-icon>
```

关键信息：

  * `toggleIcon` 是您将在切换按钮元素上定义的 <em>属物</em>。它还没有默认值。
    
  * `icon="[[toggleIcon]]" `分配是一个 <em>数据绑定</em>。它连接您的元素的 `toggleIcon` <em>属物</em> 与 `<iron-icon>` 的 `icon` 属物。

您现在可以使用您的元素，在标记中或使用 JavaScript 设置 `toggleIcon` 属物。
如果您好奇新图标来自哪里，请看一看 `demo` 文件夹中的 `demo-element.html`。

您会看到这样的行：

demo-element.html——已有的演示代码 { .caption }

```html
<icon-toggle toggle-icon="star" pressed></icon-toggle>
```

These lines are _already in place_, you don't have to add them. These lines
are part of the demo you see on screen. But if you'd like to experiment, try
adding a new `<icon-toggle>` element to the `demo-element.html` file. Some
icon names you can try are `add`, `menu`, and `settings`.

**Learn more: attribute and property names.** You'll note that the markup above
uses `toggle-icon`, not `toggleIcon`. Polymer represents camelCase property names
using dash-case attribute names. To learn more, see <a href="/2.0/docs/devguide/properties#property-name-mapping">Property
name to attribute name mapping</a> in the Polymer library docs.
{ .alert .alert-info }

The `properties` object also supports several more features. Add the following lines to add
support for the `pressed` property:

icon-toggle.html: Before { .caption }
```html
<script>
  class IconToggle extends Polymer.Element {
    static get is() {
    return "icon-toggle";
    }
    static get properties() {
      return {
        toggleIcon: {
          type: String
        },
      }
    }
    constructor() {
      super();
    }
  }
  customElements.define(IconToggle.is, IconToggle);
</script>
```

icon-toggle.html: After { .caption }

```html
<script>
  class IconToggle extends Polymer.Element {
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
    }
  }
  customElements.define(IconToggle.is, IconToggle);
</script>
```

Key information:

 *   For this more complicated property, you supply a configuration object with
several fields.
*   The `value` specifies the property's [default value](/2.0/docs/devguide/properties#configure-values).
*   The `notify` property tells Polymer to <em>dispatch property change events
    </em>when the property value changes. This lets the change be observed by
    other nodes.
*   The `reflectToAttribute` property tells Polymer to
    [update the corresponding attribute when the property changes](/2.0/docs/devguide/properties#attribute-reflection).
    This lets you style the element using an attribute selector, like
    `icon-toggle[pressed]`.

**Learn more: `notify` and `reflectToAttribute`.** The `notify` and
`reflectToAttribute` properties may _sound_ similar: they both make the element's
state visible to the outside world. `reflectToAttribute` makes the
state visible **in the DOM tree**, so that it's visible to CSS and the
`querySelector` methods. `notify` **makes state changes observable outside the
element**, either using JavaScript event handlers or Polymer
<a href="/2.0/docs/devguide/data-binding#two-way-bindings">two-way data binding</a>.
{ .alert .alert-info }

Now your element has `pressed` and `toggleIcon` properties working.

Reload the demo, and you should see star and heart icons instead of the
hard-coded icon from the previous step:

<img src="/images/2.0/first-element/static-toggles.png" alt="Demo showing icon toggles with star and heart icons">

<a class="blue-button" href="step-2">Previous step: Add local DOM</a>
<a class="blue-button" href="step-4">Next step: React to input</a>
