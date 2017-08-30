---
title: 第 1 步：设置好
subtitle: "使用 App 工具箱创建一个 App"
---

<!-- toc -->

[Polymer App 工具箱][toolbox] 是组件，工具和模板的一个集合，用来使用 Polymer 构建渐进式 Web App。

按照以下说明，使用 App 工具箱模板，在不到 15 分钟内安装、创建和部署一个项目。

## 安装 Polymer CLI

Polymer CLI 是 Polymer 项目的一个一体化命令行工具。在本教程中，您使用 Polymer CLI 初始化，服务和构建您的项目。
您还可以使用它来进行代码检查和测试，但本教程不会涵盖这些主题。

Polymer CLI 需要 Node.js、npm、Git 和 Bower。如要完全安装指南，请见 [ 
Polymer CLI 文档](/{{{polymer_version_dir}}}/docs/tools/polymer-cli)。

要安装 Polymer CLI：

    npm install -g polymer-cli


## 从模板初始化您的项目
1. 创建一个新的项目文件夹以开始

        mkdir my-app
        cd my-app

1. 使用 App 模板初始化您的项目

        polymer init

    Press the down arrow until `polymer-2-starter-kit` is highlighted and press the enter / return
    key to select.


## 服务您的项目

App 工具箱模板不需要任何构建步骤即可开始开发。您可以使用 Polymer CLI 服务应用，并且您所做的文件更改将通过刷新浏览器立即可见。

要服务您的项目：

    polymer serve --open

## 项目结构

下图是项目中的文件和目录的简要摘要。

```text
bower.json             # bower 配置
bower_components/      # App 依赖
images/
index.html             # 您的 App 的主入口
manifest.json          # App 清单配置
package.json           # NPM 元数据文件
polymer.json           # Polymer CLI 配置
service-worker.js      # 自动生成的服务工作者
src/                   # App 特定元素
  my-app.html            # 顶级元素
  my-icons.html          # App 图标
  my-view1.html          # 示例视图或“页面”
  my-view2.html
  my-view3.html
  my-view404.html        # 示例 404 页面
  shared-styles.html     # 示例共享样式
sw-precache-config.js  # 服务工作者预缓存配置
test/                  # 单元测试
```

## 下一步

您的 App 现已建立并在本机运行。接下来，了解如何向您的 App 添加页面。

<a class="blue-button"
    href="create-a-page">下一步：创建页面</a>

[toolbox]: /2.0/toolbox/
[md]: http://www.google.com/design/spec/material-design/introduction.html
