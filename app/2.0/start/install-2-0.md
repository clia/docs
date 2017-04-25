---
title: 安装 Polymer 2.x
---

<!-- toc -->

Polymer 是通过 [Bower 包管理器](https://bower.io/) 进行分发的。

要创建一个应用模板，并自动安装 Polymer，您可以 [使用 Polymer CLI](#use-cli)。

要从零开始一个项目，您可以 [用 Bower 安装 Polymer](#use-bower). 

### 使用 Polymer CLI 来创建应用模板，并安装 Polymer {#use-cli}

1. 安装 Bower：

    ```bash
    npm install -g bower
    ```

2. 安装 Polymer CLI：

    ```bash
    npm install -g polymer-cli
    ```

3. 验证您的 Polymer 版本：

    ```bash
    polymer --version
    ```

    这个命令的输出应该至少不低于 `0.18.0`；

4. 为 Polymer 2.0 创建一个测试文件夹，然后切换到其中：

    ```bash
    mkdir polymer-20-test
    cd polymer-20-test
    ```

5. 初始化您的项目：

    ```bash
    polymer init
    ```

6. 选择 `polymer-2-application`；

7. 服务您的项目：

    ```bash
    polymer serve
    ```

### 用 Bower 安装 Polymer {#use-bower}

1. 安装 Bower：

    ```bash
    npm install -g bower
    ```

2. 安装 Polymer CLI：

    ```bash
    npm install -g polymer-cli
    ```

3. 验证您的 Polymer CLI 版本：

    ```bash
    polymer --version
    ```

    这个命令的输出应该至少不低于 `0.18.0`；

4. 用 Bower 安装最新版的 Polymer 2.0 RC 版：

    ```bash
    bower install Polymer/polymer#^2.0.0-rc.3
    ```

5. 创建一个测试 `index.html` 文件，把下面的代码加进 `<head>` 标签里：
  - `<script src="/bower_components/webcomponentsjs/webcomponents-loader.js"></script>` 
  用来装载 polyfills
  - `<link rel="import" href="/bower_components/polymer/polymer.html">` 
  用来导入 Polymer

6. 导入和使用您想要的任何元素；

7. 服务您的项目：

    ```bash
    polymer serve
    ```

有关为生产环境构建项目的信息，请参考文档 [为生产环境构建 Polymer 应用](../docs/tools/build-for-production.md).

