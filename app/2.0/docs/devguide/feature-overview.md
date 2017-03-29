---
subtitle: 功能概述
title: Polymer 库
---

Polymer 库提供用于创建自定义元素的一组功能。这些功能的设计，使其更容易、更快地创建像标准的 DOM 元素一样工作的自定义元素。
类似于标准 DOM 元素，Polymer 元素可以是：

* 使用构造函数实例化或是 `document.createElement`。
* 使用 attributes 或者 properties 进行配置。
* 填充每个实例内部的内部 DOM。
* 响应于 property 和 attribute 的变化（例如，通过填充数据到 DOM，或触发一个事件）。
* 用内部默认值来实现样式，或通过外部途径。
* 响应于操纵其内部状态的方法。

一个基础的 Polymer 元素定义如下所示：

```
    <dom-module id="x-custom">
      <!-- 可选的阴影 DOM 模板 -->
      <template>
        <style>
          /* 用于您的元素的 CSS 样式 */
        </style>

        <!-- 用于您的元素的阴影 DOM -->

        <div>{{greeting}}</div> <!-- 本地 DOM 中的数据绑定 -->
      </template>

      <script>
        // 使用 ES2015 的类定义元素的 API
        class XCustom extends Polymer.Element {

          static get is() { return 'x-custom'; }

          // 为元素的公共 API 声明属物
          static get properties() {
            return {
              greeting: {
                type: String,
                value: "Hello!"
              }
            }
          }

          // Add methods to the element's public API
          greetMe() {
            console.log(this.greeting);
          }

        }

        // Register the x-custom element with the browser
        customElements.define(XCustom.is, XCustom);
      </script>

    </dom-module>
```


本指南把功能划分为以下几组：

*   [自定义元素](custom-elements)。注册元素将类与自定义元素名称相关联。该元素提供回调以管理其生命周期。
    Polymer 还可以让您声明属物，将元素的属物 API 与 Polymer 数据系统集成。

*   [阴影 DOM](shadow-dom)。阴影 DOM 为您的元素提供了本地封装的DOM树。Polymer 可以自动用 DOM 模板为您的元素创建和填充阴影树。

*   [事件](events)。Polymer 提供了一个用于将事件监听器附加到阴影 DOM 子节点的声明性语法。它还提供了一个用于处理手势事件的可选库。

*   [数据系统](data-system)。Polymer 数据系统提供与属物和属性的数据绑定; 属物观察者，和被计算的属物。


如果您要迁移现有的 1.x 版本的元素到新的 API，请参阅
[迁移指南](/2.0/docs/upgrade) 以获得建议。

如果您要查找此版本中的最新更改，请参阅
[发行说明](/2.0/docs/release-notes)。
