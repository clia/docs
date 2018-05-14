---
subtitle: 功能概述
title: Polymer 库
---

Polymer 库提供用于创建自定义元素的一组功能。这些功能的设计，使其更容易、更快地创建像标准的 DOM 元素一样工作的自定义元素。
类似于标准 DOM 元素，Polymer 元素可以是：

* 使用构造函数实例化或是 `document.createElement`。
* 使用属性或者属物进行配置。
* 填充每个实例内部的内部 DOM。
* 响应于属物和属性的变化。
* 用内部默认值来实现样式，或通过外部途径。
* 响应于操纵其内部状态的方法。

一个基础的 Polymer 元素定义如下所示：

```js
import {PolymerElement, html} from '@polymer/polymer/polymer-element.js';

// Define the element's API using an ES2015 class
class XCustom extends PolymerElement {

  // Define optional shadow DOM template
  static get template() { 
    return html`
      <style>
        /* CSS rules for your element */
      </style>

        <!-- shadow DOM for your element -->

      <div>[[greeting]]</div> <!-- data bindings in shadow DOM -->
    `;
  }

  // Declare properties for the element's public API
  static get properties() {
    return {
      greeting: {
        type: String
      }
    }
  }

  constructor() {
    super();
    this.greeting = 'Hello!';
  }

  // Add methods to the element's public API
  greetMe() {
    console.log(this.greeting);
  }

}

// Register the x-custom element with the browser
customElements.define('x-custom', XCustom);
```

本指南把功能划分为以下几组：

*   [自定义元素](custom-elements)。注册元素将类与自定义元素名称相关联。该元素提供回调以管理其生命周期。
    Polymer 还可以让您声明属物，将元素的属物 API 与 Polymer 数据系统集成。

*   [阴影 DOM](shadow-dom)。阴影 DOM 为您的元素提供了本地封装的 DOM 树。Polymer 可以自动用 DOM 模板为您的元素创建和填充阴影树。

*   [事件](events)。Polymer 提供了一个用于将事件监听器附加到阴影 DOM 子节点的声明性语法。它还提供了一个用于处理手势事件的可选库。

*   [数据系统](data-system)。Polymer 数据系统提供与属物和属性的数据绑定; 属物观察者，和被计算的属物。


If you're upgrading an existing 2.x element to 3.x, see the
[Upgrade guide](/3.0/docs/upgrade) for advice.

If you're looking for the latest changes in this release, see the
[Release notes](/3.0/docs/release-notes).
