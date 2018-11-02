---
title: 步骤3. 添加一些元素
subtitle: "使用 App 工具箱构建 App"
---

<!-- toc -->

现在您已经向应用程序添加了新的视图，您可以开始构建
该视图的细节了。

在此过程中，您可能想使用一些现成的组件，例如从 [webcomponents.org][webcomponents.org] 获取。


## 安装现成的组件

Once you've identified a component you'd like to install, you'll want to find
the npm package name for the component.

In this step, you'll add Polymer's `<paper-checkbox>` element to your app.

Run the following command from your root project folder:

    npm install @polymer/paper-checkbox@next --save

## 将元素添加到您的应用

1.  Open `src/my-new-view.js` in a text editor.

1.  Import `paper-checkbox.js`.

    Add this import beneath the existing import for `polymer-element.js`:

    ```
    import '@polymer/paper-checkbox/paper-checkbox.js';
    ```

1.  为该元素向模板中添加 `<paper-checkbox>` 元素。

    ```
    <paper-checkbox>Ready to deploy!</paper-checkbox>
    ```

    You can add it under the `<h1>` you added in the previous step. Your `template` function
    should now look like this:

    my-new-view.js {. caption}

    ```js
    static get template() {
      return html`
        <style include="shared-styles">
          :host {
            display: block;

            padding: 10px;
          }
        </style>

        <div class="card">
          <div class="circle">1</div>
          <h1>New View</h1>
          <paper-checkbox>Ready to deploy!</paper-checkbox>
          <p>New view!</p>
        </div>
      `;
    }
    ```

您现在应该可以看到新视图中已经出现 `paper-checkbox`:

![Example of page with checkbox](/images/3.0/toolbox/starter-kit-checkbox.png)

**Note about duplicate dependencies:** If you get `Uncaught DOMException: Failed to execute 'define' on 'CustomElementRegistry': this name has already been used with this registry` after installing another component, it is probably because NPM installed a nested version of Polymer within that component's `node_modules/` directory. To resolve this, reset with a fresh set of dependences (`rm -rf node_modules/ package-lock.json; npm i`). See [polymer-starter-kit Issues #1123](https://github.com/Polymer/polymer-starter-kit/issues/1123) for more details. { .alert .alert-info }

## 下一步

现在您已经向页面添加了第三方组件，该学习如何
[部署 App 到 Web 上](deploy).

[webcomponents.org]: https://www.webcomponents.org
[paper-checkbox]: https://www.webcomponents.org/element/PolymerElements/paper-checkbox
