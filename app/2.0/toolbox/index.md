---
subtitle: 箱子里有什么？
title: Polymer App 工具箱
---

Polymer App 工具箱是一套组件、工具和模板的集合，用来使用 Polymer 构建
[渐进式 Web Apps](https://developers.google.com/web/progressive-web-apps)。
App 工具箱功能：

-   基于组件的架构，使用 Polymer 和 Web 组件。
-   响应式设计，使用 [App 布局组件](https://www.webcomponents.org/element/PolymerElements/app-layout)。
-   模块化路由，使用
    [`<app-route>`](https://www.webcomponents.org/element/PolymerElements/app-route) 元素。
-   本地化，使用
    [`<app-localize-behavior>`](https://www.webcomponents.org/element/PolymerElements/app-localize-behavior)。
-   本地存储的交钥匙支持，使用
    [App 存储元素](https://www.webcomponents.org/element/PolymerElements/app-storage)。
-   离线缓存作为渐进增强，使用服务工作者。
-   构建工具以支持以多种方式服务您的 App：未打包的用于通过 HTTP/2 和服务器推技术进行分发，打包的用于通过 HTTP/1 进行分发。

您可以单独使用这些组件中的任何一个，或者使用它们一起构建一个功能全面的渐进式 Web App。
最重要的是，各组件是_可累加的_。对于一个简单的 App，您可能只需要app-layout。当它变得更复杂时，您可以根据需要添加路由，离线缓存和高性能服务器。

**混合兼容。** 工具箱元素和行为可用作混合版本，可与 Polymer 1 和 Polymer 2 一起使用。在使用 2.0 正式版时，使用元素的 `2.0` 分支。
{.alert .alert-info}

要了解这些组件的操作，您可以尝试两个演示 App 之一：

-   [商店](https://shop.polymer-project.org/)。商店是一个使用工具箱构建的功能齐全的电子商务渐进式 Web App 演示。了解如何构建
    [案例研究：商店 App](case-study)。

-   [新闻](https://news.polymer-project.org/)。新闻是一个功能齐全的渐进式 Web App 演示，像商店一样，但专注于发布。了解如何构建
    [案例研究：新闻 App](news-case-study)。


要开始使用 App 工具箱，请访问 [使用 App 工具箱创建 App](/2.0/start/toolbox/set-up)。

或者继续阅读，了解 [响应式 App 布局](app-layout)。

<a href="/2.0/start/toolbox/set-up" class="blue-button">创建 App
</a>

<a href="app-layout" class="blue-button">响应式 App 布局
</a>
