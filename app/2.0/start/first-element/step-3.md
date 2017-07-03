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

这些代码行 _已经准备好_，您无需手动添加它们。这些代码行是您在屏幕上看到的演示的一部分。
但如果您想自己试验一下，可以尝试添加一个新的 `<icon-toggle>` 元素到 `demo-element.html` 文件里。
您可以尝试的一些图标名称包括 `add`、`menu` 和 `settings`。

**了解更多：属性和属物名称。** 您会注意到上面使用的标记是 `toggle-icon`，而不是 `toggleIcon`。
Polymer 使用连字符形式的属性名称来表示驼峰形式的属物名称。
要了解更多信息，请参阅 Polymer 库文档中的 <a href="/2.0/docs/devguide/properties#property-name-mapping">属物名称到属性名称映射</a>。
{ .alert .alert-info }

`properties` 对象还支持其他多个功能。添加以下行以添加对
`pressed` 属物的支持：

icon-toggle.html: 之前 { .caption }
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

icon-toggle.html: 之后 { .caption }

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

关键信息：

 *   对于这个更复杂的属物，您提供了一个具有多个字段的配置对象。
*   `value` 指定属物的 [默认值](/2.0/docs/devguide/properties#configure-values)。
*   `notify` 属物告诉 Polymer 在属物值更改时 <em>分发属物变更事件
    </em>。这样可以让其他节点观察到变化。
*   `reflectToAttribute` 属物告诉 Polymer
    [在属物更改时更新相应的属性](/2.0/docs/devguide/properties#attribute-reflection)。
    这样可以让您使用属性选择器，如 `icon-toggle[pressed]` 来样式化该元素。

**了解更多：`notify` 和 `reflectToAttribute`。** `notify` 和
`reflectToAttribute` 属物可能 _听起来_ 相似：它们都使元素的状态为外面的世界可见。
`reflectToAttribute` 使状态**在 DOM 树中**可见，以便它能在 CSS 中可见和被 `querySelector` 方法检索到。
`notify` **使状态变更能被元素外部观察到**，或者使用 JavaScript 事件处理器，或者使用 Polymer
<a href="/2.0/docs/devguide/data-binding#two-way-bindings">双向数据绑定</a>。
{ .alert .alert-info }

现在您的元素已有 `pressed` 和 `toggleIcon` 属物在工作。

重新加载演示，您应该看到星形和心形图标，而不是上一步中的硬编码图标：

<img src="/images/2.0/first-element/static-toggles.png" alt="Demo showing icon toggles with star and heart icons">

<a class="blue-button" href="step-2">上一步：添加本地 DOM</a>
<a class="blue-button" href="step-4">下一步：响应输入</a>
