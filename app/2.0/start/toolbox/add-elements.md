---
title: 步骤3. 添加一些元素
subtitle: "使用 App 工具箱构建 App"
---

<!-- toc -->

现在您已经向应用程序添加了新的视图，您可以开始构建
该视图的细节了。

在此过程中，您可能想使用一些现成的组件，例如从 [webcomponents.org][webcomponents.org] 获取。


## 安装现成的组件

确定要安装的组件后，您将需要找到该组件的
bower 软件包名称。

在此步骤中，你将要在应用中添加 Polymer 的 `<paper-checkbox>` 元素，该元素在
[webcomponents.org][paper-checkbox] 列出。您可以使用 Bower 来安装它。

在您的项目根目录运行以下命令：

    bower install --save PolymerElements/paper-checkbox#2.0-preview

## 将元素添加到你的应用

1.  在文本编辑器中打开 `src/my-new-view.html`.

1.  作为依赖导入 `paper-checkbox.html`.

    向已有导入 `polymer-element.html` 下面增加新导入：
    
    ```
    <link rel="import" href="../bower_components/paper-checkbox/paper-checkbox.html">
    ```

1.  为该元素向模板中添加 `<paper-checkbox>` 元素。

    ```
    <paper-checkbox>Ready to deploy!</paper-checkbox>
    ```
    
    你可以把它添加到前面步骤的 `<h1>` 下面. 之后，你的新模版看起来应该像:

    ```
    <!-- 定义元素的样式和本地 DOM -->
    <template>
      <style>
        :host {
          display: block;

          padding: 16px;
        }
      </style>

      <h1>New view</h1>
      <paper-checkbox>Ready to deploy!</paper-checkbox>
    </template>
    ```

你现在应该可以看到新视图中已经出现 `paper-checkbox`:

![Example of page with checkbox](/images/2.0/toolbox/starter-kit-checkbox.png)

## 下一步

现在您已经向页面添加了第三方组件，该学习如何
[部署 App 到 Web 上](deploy).

[bower]: http://bower.io/
[webcomponents.org]: https://www.webcomponents.org
[paper-checkbox]: https://www.webcomponents.org/element/PolymerElements/paper-checkbox
