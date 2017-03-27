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
    <dom-module id="element-name">

      <template>
        <style>
          /* 用于您的元素的 CSS 样式 */
        </style>

        <!-- 用于您的元素的本地 DOM -->

        <div>{{greeting}}</div> <!-- 本地 DOM 中的数据绑定 -->
      </template>

      <script>
        // 元素注册
        Polymer({
          is: "element-name",

          // 添加属物和方法到元素的原型上

          properties: {
            // 声明属物用于该元素的公共 API
            greeting: {
              type: String,
              value: "Hello!"
            }
          }
        });
      </script>

    </dom-module>
```


本指南把功能划分为以下几组：

*   [注册和生命周期](registering-elements)。用自定义的元素名称注册一个元素与一个类（原型）相关联。
    该元素提供回调方法来管理它的生命周期。使用行为来共享代码。

*   [声明 properties](properties)。声明的 properties 可通过标记语言使用 attributes 进行配置。
    声明的 properties 可选择支持变更观察者，双向数据绑定和反射到 attributes。您也可以声明被计算的
    properties 和只读 properties。

*   [本地 DOM](local-dom)。本地 DOM 是由元素创建和管理的 DOM。

*   [事件](events)。附加事件监听器到宿主对象和本地 DOM 的子节点。事件重定向。

*   [数据绑定](data-binding)。Property 绑定。绑定到 attributes。

*   [行为](behaviors)。行为是可重用的代码模块，可混入 Polymer 元素。

*   [实用函数](instance-methods)。用于通用任务的辅助方法。

*   [实验性的功能和元素](experimental)。实验性的模板和样式功能。功能分层。

如果您要迁移现有的 0.5 版本的元素到新的 API，请参阅 [迁移指南](/1.0/docs/migration) 以获得建议。

如果您从0.8版本升级，请参见 [发行说明](/1.0/docs/release-notes)。
