---
title: 第 1 步：设置好
subtitle: "使用应用工具箱创建一个应用"
---

<!-- toc -->

[Polymer 应用工具箱][toolbox] 是组件，工具和模板的一个集合，用来使用 Polymer 构建渐进式 Web 应用。

按照以下说明，使用应用工具箱模板，在不到 15 分钟内安装、创建和部署一个项目。

<<<<<<< HEAD
## 安装 Polymer CLI

Polymer CLI 是 Polymer 项目的一个一体化命令行工具。在本教程中，您使用 Polymer CLI 初始化，服务和构建您的项目。您还可以使用它来进行代码检查和测试，但本教程不会涵盖这些主题。

1.  通过运行以下命令检查是否已安装了所有 Polymer CLI 的依赖项。
=======
## Install Polymer CLI

Polymer CLI is an all-in-one command line tool for Polymer projects. In this tutorial you use 
Polymer CLI to initialize, serve, and build your project. You can also use it for linting and 
testing, but this tutorial won't cover those topics.

Polymer CLI requires Node.js, npm, Git and Bower. For full installation instructions, see [the 
Polymer CLI documentation](/{{{polymer_version_dir}}}/docs/tools/polymer-cli).
>>>>>>> e04073f2ffb28a90217133a7c99af4085a170bda

To install Polymer CLI:

<<<<<<< HEAD
            git --version

    *   Node.js (LTS 版本 6.x)

            node -v

    *   npm v3 or higher

            npm -v

    *   Bower

            bower -v

    您应该看到典型的输出，指示您正在运行的每个这些依赖项的版本。如果您缺少任何这些依赖项，
    请按照 Polymer CLI 指南中的以下部分中的说明操作，了解如何安装每个依赖项：
    [Polymer CLI 指南中的安装部分](/2.0/docs/tools/polymer-cli#install)。



1.  安装 Polymer CLI。

        npm install -g polymer-cli@next
=======
   ```bash
   npm install -g polymer-cli
   ```
>>>>>>> e04073f2ffb28a90217133a7c99af4085a170bda

## 从模板初始化您的项目

1. 创建一个新的项目文件夹以开始

        mkdir my-app
        cd my-app

1. 使用应用模板初始化您的项目

        polymer init polymer-2-starter-kit

## 服务您的项目

应用工具箱模板不需要任何构建步骤即可开始开发。您可以使用 Polymer CLI 服务应用，并且您所做的文件更改将通过刷新浏览器立即可见。

要服务您的项目：

    polymer serve --open

## 项目结构

下图是项目中的文件和目录的简要摘要。

```text
bower.json             # bower 配置
bower_components/      # 应用依赖
images/
index.html             # 您的应用的主入口
manifest.json          # 应用清单配置
package.json           # NPM 元数据文件
polymer.json           # Polymer CLI 配置
service-worker.js      # 自动生成的 service worker
src/                   # 应用特定元素
  my-app.html            # 顶级元素
  my-icons.html          # 应用图标
  my-view1.html          # 示例视图或“页面”
  my-view2.hmtl
  my-view3.html
  my-view404.html        # 示例 404 页面
  shared-styles.html     # 示例共享样式
sw-precache-config.js  # service worker 预缓存配置
test/                  # 单元测试
```

## 下一步

您的应用现已建立并在本机运行。接下来，了解如何向您的应用添加页面。

<a class="blue-button"
    href="create-a-page">下一步：创建页面</a>

[toolbox]: /2.0/toolbox/
[md]: http://www.google.com/design/spec/material-design/introduction.html
