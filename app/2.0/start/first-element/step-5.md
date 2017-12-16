---
title: "Step 5: Theming with custom CSS properties"
subtitle: "Build your first Polymer element"
---

<!-- toc -->

您现在已有了一个基本功能的按钮。但它现在受困于使用已有的文本颜色，既用于按压的状态，也用于未按压的状态。
如果您想要更闪亮一点呢？

阴影 DOM 帮助防止用户无意中更改到了元素的内部样式。
要允许用户对组件进行样式化，您可以使用 _自定义 CSS 属物_。Polymer
提供了一个自定义 CSS 属物实现，灵感来自于
[用于级联变量的 CSS 自定义属物](http://www.w3.org/TR/css-variables/) 规范。

您可以使用 `var` 函数在您的元素中应用自定义属物。

<pre><code>background-color: var(<em>--my-custom-property</em>, <em>defaultValue</em>);</pre></code>

这里 <code>--<em>my-custom-property</em></code> 是一个自定义属物名称，总是以两个连字符开头 (`--`)，
而 <code><em>defaultValue</em></code> 是一个（可选的）CSS 值，当自定义属物未被设值时被使用。

## 添加新的自定义属物值

编辑您元素的 `<style>` 标签，使用自定义属物替换 `fill` 和 `stroke` 的值。

icon-toggle.html: 之前  { .caption }

```
  <style>
    /* 本地样式放在这里 */
    :host {
      display: inline-block;
    }
    iron-icon {
      fill: rgba(0,0,0,0);
      stroke: currentcolor;
    }
    :host([pressed]) iron-icon {
      fill: currentcolor;
    }
  </style>
```

icon-toggle.html: 之后  { .caption }

```
  <style>
    /* 本地样式放在这里 */
    :host {
      display: inline-block;
    }
    iron-icon {
      fill: var(--icon-toggle-color, rgba(0,0,0,0));
      stroke: var(--icon-toggle-outline-color, currentcolor);
    }
    :host([pressed]) iron-icon {
      fill: var(--icon-toggle-pressed-color, currentcolor);
    }
  </style>
```

由于有默认值，您依然可以仅仅设定 `color` 来样式化 `<icon-toggle>`，但您现在有其他选择。

从 `demo` 文件夹，打开 `demo-element.html`，设定新的属物。

demo-element.html: 之前 { .caption }

```
    <style>
      :host {
        font-family: sans-serif;
      }
    </style>
```

demo-element.html: 之后 { .caption }

```
    <style>
      :host {
        font-family: sans-serif;
        --icon-toggle-color: lightgrey;
        --icon-toggle-outline-color: black;
        --icon-toggle-pressed-color: red;
      }
    </style>
```

再次运行演示以获得多彩颜色。


<img src="/images/2.0/first-element/toggles-styled.png" alt="Demo showing
icon toggles with star and heart icons. Pressed icons are red.">

就这样 — 您的元素完成了。您已经创建了一个元素，有基础的
UI、API 和自定义样式属物。

如果您在使该元素工作的过程中遇到了任何麻烦，请检查
[完成的版本](https://github.com/PolymerLabs/polymer-2-first-element/tree/master/icon-toggle-finished)。

如果您想了解更多有关自定义属物的信息，请继续阅读。

## 额外加分：在文档级别设置自定义属物

Frequently you want to define custom property values at the document level, to
set a theme for an entire application, for example. Because custom properties
aren't built into most browsers yet, you need to use a special `custom-style`
tag to define custom properties outside of a Polymer element. Try
adding the following code inside the `<head>` tag of your `index.html` file:

```
<custom-style>
  <style>
    /* Define a document-wide default—will not override a :host rule in  */
    html {
      --icon-toggle-outline-color: red;
    }
    /* Override the value specified in demo-element */
    demo-element {
      --icon-toggle-pressed-color: blue;
    }
    /* This rule does not work! */
    body {
      --icon-toggle-color: purple;
    }
  </style>
</custom-style>
```

Key information:

*   The `demo-element` selector matches the `demo-element` element, and
    has a **higher specificity** than the `html` rule inside `demo-element`,
    so it overrides the values there.

*   Custom properties can **only** be defined in rule-sets that match the `html`
    selector **or a Polymer custom element.** This is a limitation
    of the Polymer implementation of custom properties.

Run the demo again, and you'll notice that the pressed buttons are now blue,
but **the main color and outline color haven't changed.**

The `--icon-toggle-color` property doesn't get set because it can't be applied
to the `body` tag. Try moving this rule into the `demo-element` block to see
it applied.

The `html` rule-set creates a document-wide default value for `--icon-toggle-outline-color`.
But this value is overridden by the corresponding rule inside the `demo-element`
element. To see this default value at work, comment out the corresponding rule in
`demo-element.html`:

demo-element.html { .caption }

```
    <style>
      :host {
        font-family: sans-serif;
        --icon-toggle-color: lightgrey;
        /* --icon-toggle-outline-color: black; */
        --icon-toggle-pressed-color: red;
      }
    </style>
```

Finally, note that to match a selector in the `custom-style`, the element must
be **in the document scope**—for example, in `index.html`, not inside another
element's shadow DOM. For example, these rules do **not** work inside the
`custom-style`:

```
    iron-icon {
      --iron-icon-width: 40px;
      --iron-icon-height: 40px;
    }
```

That's because the `iron-icon` elements on the page are inside another element's
shadow DOM. However, since custom properties inherit down the tree, you can set
these properties at the document level to set the size for all `iron-icon`
elements on the page:

```
    html {
      --iron-icon-width: 40px;
      --iron-icon-height: 40px;
    }
```

For more information, see the documentation on [custom CSS properties](https://www.polymer-project.org/2.0/docs/devguide/custom-css-properties).

Ready to get started on your own element? You can use the Polymer CLI to
[Create an element project](/2.0/docs/tools/polymer-cli#element).

You can also see the [Build an app](/2.0/start/toolbox/set-up)
tutorial to get started on an app using the Polymer App Toolbox.

Or review the previous section:

<a class="blue-button" href="step-4">
  Previous Step: React to input
</a>
