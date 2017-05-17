---
subtitle: 箱子里有什么？
title: Polymer App 工具箱
---

Polymer App 工具箱是一套组件、工具和模板的集合，用来使用 Polymer 构建
[渐进式 Web App](https://developers.google.com/web/progressive-web-apps)。
App 工具箱功能：

-   基于组件的架构，使用 Polymer 和 Web 组件。
-   响应式设计，使用[App 布局组件](https://elements.polymer-project.org/elements/app-layout)。
-   模块化路由，使用
    [`<app-route>`](https://elements.polymer-project.org/elements/app-route) 元素。
-   本地化，使用
    [`<app-localize-behavior>`](https://elements.polymer-project.org/elements/app-localize-behavior)。
-   本地存储的交钥匙支持，使用
    [App 存储元素](https://elements.polymer-project.org/elements/app-storage)。
-   离线缓存作为渐进增强，使用 service workers。
-   构建工具以支持以多种方式服务您的 App：未打包的用于通过 HTTP/2 和服务器推技术进行分发，打包的用于通过 HTTP/1 进行分发。

您可以单独使用这些组件中的任何一个，或者使用它们一起构建一个功能全面的渐进式 Web App。
最重要的是，各组件是_可累加的_。对于一个简单的 App，您可能只需要app-layout。当它变得更复杂时，您可以根据需要添加路由，离线缓存和高性能服务器。

要实际感觉这些组件在实况中的 App，您可以尝试
[商店演示](https://shop.polymer-project.org/)。商店是一个使用工具箱构建的功能齐全的电子商务渐进式 Web App 演示。
了解它是如何建成的 [案例：商店 App](case-study).

[新闻 App 演示](https://news.polymer-project.org) 展示了一个新闻站点的渐进式 Web App 的实现。了解该新闻站点 App 相关的实现细节 [案例：新闻 App](news-case-study)。

要开始使用 App 工具箱，请访问 [使用 App 工具箱创建 App](/1.0/start/toolbox/set-up)。

或者继续阅读，了解 [响应式 App 布局](app-layout).

<a href="/1.0/start/toolbox/set-up" class="blue-button">构建 App
</a>

<a href="app-layout" class="blue-button">响应式 App 布局
</a>
