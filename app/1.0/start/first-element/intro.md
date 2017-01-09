---
title: "第 1 步：设置好"
subtitle: "构建您的第一个 Polymer 元素"
---

<!-- toc -->

在本教程中，您将学习如何使用 Polymer 1.0 创建元素。您将创建一个简单的 Polymer 元素：一个切换按钮。
完成后的按钮会是这个样子：

![Sample star-shaped toggle buttons, showing pressed and unpressed
state](/images/1.0/first-element/sample-toggles.png)

您可以用简单的标记像这样使用它：

```html
<icon-toggle></icon-toggle>
```

该项目向您介绍 Polymer 使用过程中最关键的概念。

如果您不明白一切，不要担心。这里提出的每个概念在 Polymer 文档中都有详细的描述。


## 第 1 步：设置好

要学习本教程，您需要：

-   开始代码。
-   [Polymer CLI](/1.0/docs/tools/polymer-cli) 来运行演示程序。


**什么都不想安装吗？** 要在网上运行本教程，
按照指令 [第 1 步：无需安装的版本](#noinstall).
{ .alert .alert-info }


### 下载开始代码

1.  点击按钮下载开始代码为ZIP文件。

    <a class="blue-button" href="https://github.com/googlecodelabs/polymer-first-elements/releases/download/v1.0/polymer-first-elements.zip">
      下载 ZIP
    </a>

2.  展开存档创建项目文件夹。

    您的项目文件夹应该是这个样子：

    <pre>
    README.md
    bower.json
    bower_components/
    demo/
    icon-toggle-finished/
    icon-toggle.html
    </pre>

    您工作的主要文件是 `icon-toggle.html`，它包含了您的自定义元素的定义。


### 安装 Polymer CLI

安装 Polymer CLI 来本地提供演示程序服务。

1.  安装 LTS 版本的 (4.x) [Node.js](https://nodejs.org/en/download/).
    当前版本 (6.x) 也可以工作，但不正式支持。不支持低于 LTS 版本。

2.  安装 [git](https://git-scm.com/downloads).

3.  安装最新版本的 [Bower](http://bower.io/#install-bower).

        npm install -g bower

4.  安装 Polymer CLI.

        npm install -g polymer-cli

### 运行演示程序

要运行元素的演示：

1.  从 repo 目录运行 `polymer serve` :

        polymer serve

2.  在您的浏览器打开 `localhost:8080/components/icon-toggle/demo/` 。

    （请注意，路径使用 `icon-toggle`，在此元素的 `bower.json` 文件中列出的组件名称，而不是实际的目录名。
    如果您想知道为什么 `polymer serve` 这样做，请看 [HTML 导入和依赖管理](/1.0/docs/tools/polymer-cli#element-imports)。）

    您会看到一些文字，出现在切换图标应该出现的地方。它看起来并不很有趣，但它表明一切正常。


<img src="/images/1.0/first-element/starting-state.png" alt="Initial state of the demo. The demo shows three icon-toggle elements, two labeled 'statically-configured icon toggles' and one labeled 'data-bound icon toggle'. Since the icon toggles are not implemented yet, they appear as placeholder text reading 'Not much here yet'." title="Initial demo">

**如果文本没有出现**，请确保您正在查看的是演示文件夹本身，或者 `demo/index.html`,
而不是 `toggle-icon.html` 或 `toggle-icon-demo.html`.
{ .alert .alert-info }

如果一切正常，进入到 [第 2 步](step-2).

<a class="blue-button" href="step-2">第 2 步：添加本地 DOM</a>



## 第 1 步：无需安装版本 {#noinstall}

要在线运行本教程，不安装任何东西：

1.  打开 [Plunker 上的入门项目](https://plnkr.co/edit/QfsudzAPCbAu56Qpb7eB?p=preview){target="\_blank"}。

2. 点击 **Fork** 来创建您自己的工作副本。

继续 [第 2 步](step-2).

<a class="blue-button" href="step-2">第 2 步：添加本地 DOM</a>
