---
title: 步骤 2. 创建一个新页面
subtitle: "使用 App Toolbox 构建应用程序"
---

<!-- toc -->

`starter-kit` 包括您可以用它来开始构建您的应用的视图的占位页面。但在某些时候，您可能需要添加更多。

此步骤将引导您完成向应用添加新页面或顶级视图的过程。

## 为新页面创建元素

首先，创建一个封装新视图内容的新自定义元素。

1.  创建一个新文件叫做 `src/my-new-view.html`，在编辑器中打开它。

2.  使用 Polymer 为新的自定义元素定义添加一些脚手架：

    ```html
    <!-- 载入 Polymer.Element 基类 -->
    <link rel="import" href="../bower_components/polymer/polymer-element.html">

    <dom-module id="my-new-view">
      <!-- 定义元素的样式和本地 DOM -->
      <template>
        <style>
          :host {
            display: block;

            padding: 16px;
          }
        </style>

        <h1>新视图</h1>
      </template>
      <script>
        // 您的新元素扩展 Polymer.Element 基类
        class MyNewView extends Polymer.Element {
          static get is() { return 'my-new-view'; }
        }
        //现在，注册您的新的自定义元素，以便浏览器能使用它
        customElements.define(MyNewView.is, MyNewView);
      </script>
    </dom-module>
    ```

到现在您的元素是非常基本的，仅有一个 `<h1>` 在说 "新视图"，
但是之后我们可以回到它，让它更有趣。

## 将元素添加到您的 App

您的元素已定义好了，但您的 App 尚未实际使用它。要使用它，您需要将其添加到您 App 的 HTML 中。

1.  在文本编辑器中打开 `src/my-app.html`。

1.  在 `<iron-pages>` 中找到一组已有的页面：

    ```
    <iron-pages
        selected="[[page]]"
        attr-for-selected="name"
        fallback-selection="view404"
        role="main">
      <my-view1 name="view1"></my-view1>
      <my-view2 name="view2"></my-view2>
      <my-view3 name="view3"></my-view3>
      <my-view404 name="view404"></my-view404>
    </iron-pages>
    ```

    `<iron-pages>` 是绑定到 `page` 变量，根据路由而改变，并且选择活动的页面，而隐藏其他页面。

1.  在 iron-pages 中添加您的新页面：

    ```
    <my-new-view name="new-view"></my-new-view>
    ```

    您的 `<iron-pages>` 现在应该看起来像这样：

    ```
    <iron-pages
        selected="[[page]]"
        attr-for-selected="name"
        fallback-selection="view404"
        role="main">
      <my-view1 name="view1"></my-view1>
      <my-view2 name="view2"></my-view2>
      <my-view3 name="view3"></my-view3>
      <my-new-view name="new-view"></my-new-view>
      <my-view404 name="view404"></my-view404>
    </iron-pages>
    ```

    注意：通常当第一次添加新的自定义元素时，您需要添加一个 HTML 导入，以确保已经加载组件定义。
    然而，这个 App 模板已经被设置成根据路由按需对顶级视图进行懒加载，因此在这种情况下，您不需要为您的新
    `<my-new-view>` 元素添加导入。

    App 模板附带的以下代码将确保在路由更改时每个页面的定义已加载。
    您可以看到，应用程序遵循一个简单的惯例 (`'my-' + page + '.html'`)
    导入每个路由的定义。您可以根据需要调整此代码，以处理更复杂的路由和懒加载。

    现有的模板代码 — 您不需要添加它 { .caption }

    ```
      _pageChanged(page) {
        // 按需装载页面导入，失败则显示 404 页面
        var resolvedPageUrl = this.resolveUrl('my-' + page + '.html');
        Polymer.importHref(
            resolvedPageUrl,
            null,
            this._showPage404.bind(this),
            true);
      }
    ```

## 创建导航菜单项

您已经定义了您的新元素，并在您的 App 中声明了它。
现在您只需要在左侧的抽屉里添加一个菜单项，以便用户可以导航到新页面。

1.  保持 `src/my-app.html` 在您的编辑器中打开。

1.  找到 `<app-drawer>` 元素内的导航菜单。

    ```
      <!-- 抽屉内容 -->
      <app-drawer id="drawer" slot="drawer">
        <app-toolbar>Menu</app-toolbar>
        <iron-selector selected="[[page]]" attr-for-selected="name" class="drawer-list" role="navigation">
          <a name="view1" href="/view1">View One</a>
          <a name="view2" href="/view2">View Two</a>
          <a name="view3" href="/view3">View Three</a>
        </iron-selector>
      </app-drawer>
    ```

    每个导航菜单项都包含一个由 CSS 修饰的锚点元素 (`<a>`)。

1.  将以下新的导航项添加到菜单底部。

    ```
    <a name="new-view" href="/new-view">New View</a>
    ```

    您的菜单现在应如下所示：

    ```
    ...
      <!-- 抽屉内容 -->
      <app-drawer id="drawer" slot="drawer">
        <app-toolbar>Menu</app-toolbar>
        <iron-selector selected="[[page]]" attr-for-selected="name" class="drawer-list" role="navigation">
          <a name="view1" href="/view1">View One</a>
          <a name="view2" href="/view2">View Two</a>
          <a name="view3" href="/view3">View Three</a>
          <a name="new-view" href="/new-view">New View</a>
        </iron-selector>
      </app-drawer>
    ...
    ```

您的新页面现在准备好了！用 `polymer serve --open` 服务您的 App。

![Example new page](/images/2.0/toolbox/new-view.png)

## 注册要构建的页面

当您将应用部署到 Web 时，您将使用 Polymer CLI 来准备文件进行部署。
Polymer CLI 将需要了解所有按需加载的片段，如您刚添加的懒加载视图。

1.  在文本编辑器中打开 `polymer.json`。

1.  添加 `src/my-new-view.html` 到 `fragments` 的列表中。

    新列表应如下所示：

    ```
    "fragments": [
      "src/my-view1.html",
      "src/my-view2.html",
      "src/my-view3.html",
      "src/my-new-view.html",
      "src/my-view404.html"
    ]
    ```

注意：您只需要添加您要懒加载的文件到 `fragments` 列表，或是使用 `async` 属性来导入。
任何使用同步的 `<link rel="import">` 标签导入的文件*都不应该*被添加到 `fragments`。

## 下一步

您已经在应用中添加了一个新页面。接下来，了解如何安装和添加现成的自定义元素到您的 App。

<a class="blue-button"
    href="add-elements">下一步：添加元素</a>
