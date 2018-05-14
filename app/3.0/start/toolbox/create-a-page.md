---
title: 步骤 2. 创建一个新页面
subtitle: "使用 App Toolbox 构建应用程序"
---

<!-- toc -->

The starter kit includes placeholder pages you can use to start building out
the views of your application. But at some point, you'll probably want to add more.

此步骤将引导您完成向应用添加新页面或顶级视图的过程。

## 为新页面创建元素

首先，创建一个封装新视图内容的新自定义元素。

1.  Create a new file called `src/my-new-view.js` and open it in an editor.

2.  使用 Polymer 为新的自定义元素定义添加一些脚手架：

    ```js
    /* Load the PolymerElement base class and html helper function */
    import { PolymerElement, html } from '@polymer/polymer/polymer-element.js';
    /* Load shared styles. All view elements use these styles */
    import './shared-styles.js';
    
    /* Extend the base PolymerElement class */
    class MyNewView extends PolymerElement {
      /* Define a template for the new element */
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
            <p>New view!</p>
          </div>
        `;
      }
    }
    /* Register the new element with the browser */
    window.customElements.define('my-new-view', MyNewView);
    ```

## Add the element to your app

Your element is defined, but your app isn't actually using it yet. To use it,
you need to add it to your app's HTML template.

1.  Open `src/my-app.js` in a text editor.

1.  在 `<iron-pages>` 中找到一组已有的页面：

    ```html
    <iron-pages
        selected="[[page]]"
        attr-for-selected="name"
        role="main">
      <my-view1 name="view1"></my-view1>
      <my-view2 name="view2"></my-view2>
      <my-view3 name="view3"></my-view3>
      <my-view404 name="view404"></my-view404>
    </iron-pages>
    ```

    `<iron-pages>` 是绑定到 `page` 变量，根据路由而改变，并且选择活动的页面，而隐藏其他页面。

1.  在 iron-pages 中添加您的新页面：

    ```html
    <my-new-view name="new-view"></my-new-view>
    ```

    您的 `<iron-pages>` 现在应该看起来像这样：

    ```html
    <iron-pages
        selected="[[page]]"
        attr-for-selected="name"
        role="main">
      <my-view1 name="view1"></my-view1>
      <my-view2 name="view2"></my-view2>
      <my-view3 name="view3"></my-view3>
      <my-new-view name="new-view"></my-new-view>
      <my-view404 name="view404"></my-view404>
    </iron-pages>
    ```

## Add a valid route for your new view

As the user navigates your app, the route data changes. In `src/my-app.js`, the app checks
the requested route against a list of valid routes. Now, you'll add your new view to the 
list of valid routes. 

1.  Locate the `_routePageChanged` function:

    ```js
    _routePageChanged(page) {
      if (!page) {
        /* If no page was found in the route data, page will be an empty string.
           Default to 'view1' in that case. */
        this.page = 'view1';
      } else if (['view1', 'view2', 'view3'].indexOf(page) !== -1) {
        this.page = page;
      } else {
        this.page = 'view404';
      }
      ...
    }
    ```

2.  Modify the `else if` line to include the name of your new view (`new-view`).
    
    `_routePageChanged` should now look like this:

    ```js
    _routePageChanged(page) {
      if (!page) {
        /* If no page was found in the route data, page will be an empty string.
            Default to 'view1' in that case. */
        this.page = 'view1';
      } else if (['view1', 'view2', 'view3', 'new-view'].indexOf(page) !== -1) {
        this.page = page;
      } else {
        this.page = 'view404';
      }
      ...
    }
    ```

## Import your new view dynamically

The starter kit uses [dynamic `import()`](https://developers.google.com/web/updates/2017/11/dynamic-import) to load views on demand. You need to add the file you created earlier (`src/my-new-view.js`) to the set of views that are imported dynamically. 
    
1.  In `src/my-app.js`, locate the `_pageChanged` function:

    ```js
    _pageChanged(page) {
      // Load page import on demand. Show 404 page if fails
      // Note: `polymer build` doesn't like string concatenation in
      // the import statement, so break it up.

      switch(page) {
        case 'view1':
          import('./my-view1.js');
          break;
        case 'view2':
          import('./my-view2.js');
          break;
        case 'view3':
          import('./my-view3.js');
          break;
        case 'view404':
          import('./my-view404.js');
          break;
      }
    }
    ```

2.  Add the following `case` to the `switch` statement to handle your new view:

    ```js
    case 'new-view':
      import('./my-new-view.js');
      break;
    ```

    Your `_pageChanged` function should now look like this:

    ```js
    _pageChanged(page) {
      // Load page import on demand. Show 404 page if fails
      // Note: `polymer build` doesn't like string concatenation in
      // the import statement, so break it up.

      switch(page) {
        case 'view1':
          import('./my-view1.js');
          break;
        case 'view2':
          import('./my-view2.js');
          break;
        case 'view3':
          import('./my-view3.js');
          break;
        case 'new-view':
          import('./my-new-view.js');
          break;
        case 'view404':
          import('./my-view404.js');
          break;
      }
    }
    ```

## 创建导航菜单项

You've defined your new element, created a valid route to handle the case when a user navigates to it, and imported its JavaScript file dynamically. Now you need to add a menu item in the left-hand drawer so that users can navigate to the new page.

1.  In `src/my-app.js`, find the navigation menu inside the `<app-drawer>` element:

    ```html
    <!-- Drawer content -->
    <app-drawer id="drawer" slot="drawer" swipe-open="[[narrow]]">
      <app-toolbar>Menu</app-toolbar>
      <iron-selector selected="[[page]]" attr-for-selected="name" class="drawer-list" role="navigation">
        <a name="view1" href="[[rootPath]]view1">View One</a>
        <a name="view2" href="[[rootPath]]view2">View Two</a>
        <a name="view3" href="[[rootPath]]view3">View Three</a>
      </iron-selector>
    </app-drawer>
    ```

1.  Add the following new navigation item to the bottom of the menu:

    ```html
    <a name="new-view" href="[[rootPath]]new-view">New View</a>
    ```

    您的菜单现在应如下所示：

    ```html
    <!-- Drawer content -->
    <app-drawer id="drawer" slot="drawer" swipe-open="[[narrow]]">
      <app-toolbar>Menu</app-toolbar>
      <iron-selector selected="[[page]]" attr-for-selected="name" class="drawer-list" role="navigation">
        <a name="view1" href="[[rootPath]]view1">View One</a>
        <a name="view2" href="[[rootPath]]view2">View Two</a>
        <a name="view3" href="[[rootPath]]view3">View Three</a>
        <a name="new-view" href="[[rootPath]]new-view">New View</a>
      </iron-selector>
    </app-drawer>
    ```

## Serve your app

Your new page is now ready! If the Polymer CLI development server is still running, you can refresh your browser window to see the changes. Otherwise, serve your app with `polymer serve` and open the URL shown at `applications`.

![Example new page](/images/3.0/toolbox/new-view.png)

## 下一步

您已经在应用中添加了一个新页面。接下来，了解如何安装和添加现成的自定义元素到您的 App。

<a class="blue-button"
    href="add-elements">下一步：添加元素</a>
