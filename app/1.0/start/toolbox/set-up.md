---
title: 第 1 步：设置好
subtitle: "使用应用工具箱创建一个应用"
---

<!-- toc -->

[Polymer 应用工具箱][toolbox] 是组件，工具和模板的一个集合，用来使用 Polymer 构建渐进式 Web 应用。

按照以下说明，使用应用工具箱模板，在不到 15 分钟内安装、创建和部署一个项目。

## 安装 Polymer CLI

1.  安装 Node.js 的 LTS 版本（4.x）。当前版本（6.x）应该工作，但是没有官方支持。不支持低于LTS的版本。

1.  安装 Polymer CLI

        npm install -g polymer-cli

## 从模板初始化您的项目

1. 创建一个新的项目文件夹以开始

        mkdir my-app
        cd my-app

1. 使用应用模板初始化项目

        polymer init starter-kit

## 服务您的项目

应用工具箱模板不需要任何构建步骤即可开始开发。您可以使用 Polymer CLI 服务应用，并且您所做的文件更改将通过刷新浏览器立即可见。

    polymer serve --open

上面的任务会自动打开默认 Web 浏览器并获取本地托管的应用 (位于 `http://localhost:8080`).

![应用工具箱：入门套件模板](/images/1.0/toolbox/starter-kit.png)

## 初始化 Git 存储库（可选）

您的应用模板不包含任何版本控制系统。如果要使用 Git 管理源代码，请按照以下说明操作。

1.  `cd` 进入您的项目的基本目录。

1.  初始化一个 Git 仓库。

        git init

1.  添加并提交所有文件。

        git add . && git commit -m "Initial commit."

## 目录结构

下图是模板中目录的简要描述。

    /
    |---index.html
    |---src/
    |---bower_components/
    |---images/
    |---test/


*   `index.html` 是您的应用的主要入口点
*   `src/` 是您的应用自身的自定义元素将去的地方
*   `bower_components/` 是可重用的自定义元素和/或通过 bower 获取的库将去的地方
*   `images/` 是用于静态图像
*   `test/` 是您 [定义您的 Web 组件的测试用例](https://github.com/Polymer/web-component-tester)的地方。

## 下一步

现在，您的应用工具箱模板已经建立和运行，学习如何 [添加新的内容页面](create-a-page)，或如何 [部署应用到 Web](deploy).

[toolbox]: /1.0/toolbox/
[shared styles]: /1.0/docs/devguide/styling.html#style-modules
[md]: http://www.google.com/design/spec/material-design/introduction.html
