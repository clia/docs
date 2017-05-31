---
title: "Step 1: Set up"
subtitle: "Build your first Polymer element"
---

<!-- toc -->

在本教程中，您将学习如何使用 Polymer 2.0 构建元素。您将创建一个简单的 Polymer 元素：一个切换按钮。
完成的按钮将如下所示：

![Sample star-shaped toggle buttons, showing pressed and unpressed
state](/images/2.0/first-element/sample-toggles.png)

您可以使用简单的标记，如下所示：

```html
<icon-toggle></icon-toggle>
```

该项目向您介绍使用 Polymer 的大多数关键概念。

如果您不明白这里的所有东西，不用担心。这里展示的每个概念都会在 Polymer 文档中有详细描述。


## 第一步：设置好

要遵循本教程，您需要：

-   [git](https://git-scm.com/downloads)。
-   起始代码，[可在 GitHub 上得到](https://github.com/PolymerLabs/polymer-2-first-element.git)。
-   [Polymer CLI](/2.0/docs/tools/polymer-cli) 来运行演示。

### 下载起始代码

1.  通过运行以下命令下载起始代码：

    ```bash
    git clone https://github.com/PolymerLabs/polymer-2-first-element.git
    ```
 
2.  打开项目文件夹：

    ```bash
    cd polymer-2-first-element
    ```

    你的项目文件夹应该是这样的：

    <pre>
    README.md
    bower.json
    demo/
    icon-toggle-finished/
    icon-toggle.html
    index.html
    </pre>

    您将使用的主文件是 `icon-toggle.html`，包含您的自定义元素的定义。

### 安装 Polymer CLI

安装 Polymer CLI 来在本地服务演示。

Polymer CLI 需要 Node.js、npm、git 和 Bower。有关完整的安装说明，请参阅 [Polymer CLI 文档](/{{{polymer_version_dir}}}/docs/tools/polymer-cli)。

要安装 Polymer CLI：

   ```bash
   npm install -g polymer-cli
   ```

### 安装依赖项并运行 demo

要安装元素的依赖项并运行演示：

1.  从仓库目录运行 `bower install`：

        bower install

    这将安装使用 Polymer 库和其他 Web 组件所需的组件和依赖项。

    您现在将在项目文件夹中看到一个额外的文件夹，叫 `bower_components`：

    <pre>
    README.md
    bower.json
    bower_components
    demo/
    icon-toggle-finished/
    icon-toggle.html
    index.html
    </pre>

2.  从项目文件夹中运行 Polymer 开发服务器：

        polymer serve --open

    在切换图标应显示的位置，您将会看到一些文本。它看起来不是很有趣，但它表明一切都正常。
 
    (请注意：URL 包含 `icon-toggle`——在此元素的 `bower.json` 文件中列出的组件名称——而不是实际的目录名。
    如果您想知道为什么 `polymer serve` 这样做，请看 [HTML 导入和依赖管理](/2.0/docs/tools/polymer-cli#element-project-layout)。)

<img src="/images/2.0/first-element/starting-state.png" alt="Initial state of the demo. The demo 
shows three icon-toggle elements, two labeled 'statically-configured icon toggles' and one labeled 
'data-bound icon toggle'. Since the icon toggles are not implemented yet, they appear as 
placeholder text reading 'Not much here yet'." title="Initial demo">

如果一切都看起来不错，请转到 [步骤 2](step-2).

<a class="blue-button" href="step-2">步骤 2：添加本地 DOM</a>
