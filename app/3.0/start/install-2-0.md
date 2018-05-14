---
title: 安装 Polymer 2.x
---

<!-- toc -->

如果您熟悉 Polymer，只是想要开始使用新版本，那么您就在正确的位置！如果您想要一份对 Polymer 项目和 Web 组件的介绍：

* [快速浏览 Polymer](/{{{polymer_version_dir}}}/start/quick-tour)
* [了解如何构建您的第一个 Polymer App](/{{{polymer_version_dir}}}/start/toolbox/set-up)
* [了解如何使用 Polymer 库创建您的第一个元素](/{{{polymer_version_dir}}}/start/first-element/intro)

Polymer 是通过 [Bower 包管理器](https://bower.io/) 进行分发的。

要创建一个应用模板，并自动安装 Polymer，您可以 [使用 Polymer CLI](#use-cli)。

要从零开始一个项目，您可以 [用 Bower 安装 Polymer](#use-bower)。

### 使用 Polymer CLI 来创建应用模板，并安装 Polymer {#use-cli}

Polymer CLI 需要 Node.js、npm、Git 和 Bower。如要完全安装指南，请见 [Polymer CLI 文档](../docs/tools/polymer-cli)。

1. 安装 Polymer CLI.

    ```bash
    npm install -g polymer-cli
    ```

3. 为 Polymer 2.0 创建一个测试文件夹，然后切换到其中：

    ```bash
    mkdir polymer-20-test
    cd polymer-20-test
    ```

4. 初始化您的项目：

    ```bash
    polymer init
    ```

5. 选择 `polymer-2-application`；

6. 服务您的项目：

    ```bash
    polymer serve
    ```

### 用 Bower 安装 Polymer {#use-bower}

1. 安装 Bower：

    ```bash
    npm install -g bower
    ```

2. 安装 Polymer CLI：

    The Polymer CLI requires Node.js and npm as well as Bower. For full installation instructions, see [the Polymer CLI documentation](../docs/tools/polymer-cli).

    ```bash
    npm install -g polymer-cli
    ```

3. 从 bower 安装最新的 Polymer 2.0 版本

    ```bash
    bower install Polymer/polymer#^2.0.0
    ```

4. 创建一个测试 `index.html` 文件，把下面的代码加进 `<head>` 标签里：
  - `<script src="/bower_components/webcomponentsjs/webcomponents-loader.js"></script>`
  用来装载 polyfills
  - `<link rel="import" href="/bower_components/polymer/polymer.html">`
  用来导入 Polymer

5. 导入和使用您想要的任何元素；

6. 服务您的项目：

    ```bash
    polymer serve
    ```

有关为生产环境构建项目的信息，请参考文档 [为生产环境构建 Polymer 应用](../toolbox/build-for-production).

