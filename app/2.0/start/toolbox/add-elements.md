---
title: 步骤3. 添加一些添加一些元
subtitle: "使用 App Toolbox 构建应用"
---

<!-- toc -->

现在您已经向应用程序添加了新的 view, 您可以开始构建
该 view 的细节.

在此过程中, 你可能想使用一些现成的组件, 例子在这里 [webcomponents.org][webcomponents.org].


## 安装现成的组件

确定要安装的组件后, 您就可以找到
对应该组建 bower 安装包.

这一步, 你要在应用中添加 Polymer 的 `<paper-checkbox>`, 该元素在
[webcomponents.org][paper-checkbox]列出.  你可以使用 Bower 来安装它.

在你的项目根目录运行以下命令:
    bower install --save PolymerElements/paper-checkbox#2.0-preview

## 将元素添加到你的应用

1.  在文本编辑器中打开 `src/my-new-view.html`.

1.  作为依赖导入 `paper-checkbox.html`.

    向已有导入内添加为`polymer-element.html`增加新导入:
    ```
    <link rel="import" href="../bower_components/paper-checkbox/paper-checkbox.html">
    ```

1.  向模板中添加 `<paper-checkbox>`.

    ```
    <paper-checkbox>Ready to deploy!</paper-checkbox>
    ```
    
    你可以把它添加到前面步骤的 `<h1>` 下面. 之后, 你的新模版看起来应该像:

    ```
    <!-- 定义元素风格和本地 DOM -->
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

Now that you've added a 3rd-party component to your page, learn how to
[deploy the app to the web](deploy).
现在您已经向页面添加了第三方组件, 该学习如何
[deploy the app to the web](部署).

[bower]: http://bower.io/
[webcomponents.org]: https://www.webcomponents.org
[paper-checkbox]: https://www.webcomponents.org/element/PolymerElements/paper-checkbox
