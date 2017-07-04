---
title: Step 2. Create a new page
subtitle: "Build an app with App Toolbox"
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

    Note: Normally when adding a new custom element for the first time, you'd
    want to add an HTML import to ensure the component definition has been
    loaded.  However, this app template is already set up to lazy-load top
    level views on-demand based on the route, so in this case you don't need
    to add an import for your new `<my-new-view>` element.

    The following code that came with the app template will ensure the
    definition for each page has been loaded when the route changes.  As
    you can see, the app follows a simple convention (`'my-' + page + '.html'`)
    when importing the definition for each route,. You can adapt this code as you
    like to handle more complex routing and lazy loading.

    Existing template code—you do not need to add this { .caption }

    ```
      _pageChanged(page) {
        // Load page import on demand. Show 404 page if fails
        var resolvedPageUrl = this.resolveUrl('my-' + page + '.html');
        Polymer.importHref(
            resolvedPageUrl,
            null,
            this._showPage404.bind(this),
            true);
      }
    ```

## 创建导航菜单项

You've defined your new element and declared it in your app. Now you
just need to add a menu item in the left-hand drawer so that users can navigate to the new page.

1.  Keep `src/my-app.html` open in your editor.

1.  Find the navigation menu inside the `<app-drawer>` element.

    ```
      <!-- Drawer content -->
      <app-drawer id="drawer" slot="drawer">
        <app-toolbar>Menu</app-toolbar>
        <iron-selector selected="[[page]]" attr-for-selected="name" class="drawer-list" role="navigation">
          <a name="view1" href="/view1">View One</a>
          <a name="view2" href="/view2">View Two</a>
          <a name="view3" href="/view3">View Three</a>
        </iron-selector>
      </app-drawer>
    ```

    Each navigation menu item consists of an anchor element (`<a>`) styled with CSS.

1.  Add the following new navigation item to the bottom of the menu.

    ```
    <a name="new-view" href="/new-view">New View</a>
    ```

    Your menu should now look like the following:

    ```
    ...
      <!-- Drawer content -->
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

Your new page is now ready! Serve your app with `polymer serve --open`.

![Example new page](/images/2.0/toolbox/new-view.png)

## 注册要构建的页面

When you deploy your application to the web, you'll use the Polymer CLI
to prepare your files for deployment.  Polymer CLI will need to know about any
demand-loaded fragments like the lazy-loaded view you just added.

1.  Open `polymer.json` in a text editor.

1.  Add `src/my-new-view.html` to the list of `fragments`.

    The new list should look like this:

    ```
    "fragments": [
      "src/my-view1.html",
      "src/my-view2.html",
      "src/my-view3.html",
      "src/my-new-view.html",
      "src/my-view404.html"
    ]
    ```

Note: You only need to add files you will lazy load or import using the `async`
attribute to the `fragments` list.  Any files that are imported using synchronous
`<link rel="import">` tags should *not* be added to `fragments`.

## 下一步

You've added a new page to your application. Next, learn how to install and add an off-the-shelf custom element to your app.

<a class="blue-button"
    href="add-elements">Next step: Add an element</a>
