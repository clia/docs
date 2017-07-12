---
title: Step 4. Deploy
subtitle: "Build an app with App Toolbox"
---

<!-- toc -->

在此步骤中，您将把应用部署到 Web 上。

## 为部署而构建

运行以下 Polymer CLI 命令来准备好您的应用进行部署：

    polymer build

此命令将缩小您的应用的 HTML，JS 和 CSS 依赖项，并生成一个服务工作者，
以预缓存应用的所有依赖项，以使其能够脱机工作。

构建好的文件被输出到 `build/default` 文件夹。默认构建包含一个非打包的构建，
生成适合通过 HTTP/2 与服务器推技术服务的细粒度资源。

有关构建选项的更多信息，请参阅 [`polymer build` 命令的文档](/2.0/docs/tools/polymer-cli#build)。
这包含生成打包的（联结的）资源的文档，适用于从不支持 HTTP/2 服务器推技术的服务器，或向不支持该技术的客户端提供服务。

## 部署到服务器

Polymer 应用可以部署到任何 Web 服务器。

这个模板采用了 `<app-location>` 元素来启用基于 URL 的路由，这就要求服务器为所有路由服务 `index.html` 入口点。

您可以按照以下其中一节所述将此 App 部署到
[Google AppEngine](https://cloud.google.com/appengine) 或是 [Firebase
静态托管](https://www.firebase.com/docs/hosting/)，都是免费和安全的部署 Polymer App 的方法。
其他主机提供商的方法也与此类似。

### 使用 AppEngine 部署

1.  下载 [Google App Engine SDK](https://cloud.google.com/appengine/downloads)，
并按照平台的说明进行安装。本教程使用 Python SDK。

1.  [注册一个 AppEngine 帐号](https://cloud.google.com/appengine)。

1.  [打开项目仪表板](https://console.cloud.google.com/iam-admin/projects)
并创建一个新项目

    * 单击“创建项目”按钮。
    * 键入项目名称。
    * 单击“创建”按钮。
    
    App Engine 会根据您的项目名称为您提供一个项目ID。记下这个ID。

1.  `cd` 进入您的 App 的主文件夹（例如 `my-app/`）。

1. 创建一个 `app.yaml` 文件，包含以下内容：

    ```
    runtime: python27
    api_version: 1
    threadsafe: yes

    handlers:
    - url: /bower_components
      static_dir: build/default/bower_components
      secure: always

    - url: /images
      static_dir: build/default/images
      secure: always

    - url: /src
      static_dir: build/default/src
      secure: always

    - url: /manifest.json
      static_files: build/default/manifest.json
      upload: build/default/manifest.json
      secure: always

    - url: /.*
      static_files: build/default/index.html
      upload: build/default/index.html
      secure: always
    ```

1.  将您的项目 ID 设置为 App Engine 提供给您的 App 的ID。例如：
    ````
    gcloud config set project my-app-164409
    ````

1. 创建您的 App。
    ````
    gcloud app create
    ````
	
    您将需要为您的 App 选择要部署的区域。这不能更改。

1. 部署您的 App。

    ````
    gcloud app deploy
    ````

1. 您的 App 将在其指定的 URL 上在线提供。例如：

    ````
    https://my-app-164409.appspot.com/new-view
    ````

    通过键入以下命令在浏览器中打开您的 App 的 URL：

    ````
    gcloud app browse
    ````

### 使用 Firebase 部署

以下说明基于 [Firebase 托管快速入门指南](https://www.firebase.com/docs/hosting/quickstart.html)。

1.  [注册一个 Firebase 帐号](https://www.firebase.com/signup/)。

1.  转到 [https://www.firebase.com/account](https://www.firebase.com/account) 去创建一个新的 App。记下与您的 App 关联的项目 ID。

    ![Welcome to Firebase showing Project ID](/images/2.0/toolbox/welcome-firebase.png)

1.  安装 Firebase 命令行工具。

        npm install -g firebase-tools

1.  `cd` 进入你的项目目录。

1.  初始化 Firebase 应用。

        firebase login
        firebase init

1.  Firebase 会询问与您的 App 关联的项目。选择您之前创建的。

1.  Firebase 会询问您的 App 的公共目录的名称。输入
    `build/default`.

1.  编辑您的 Firebase 配置以添加对 URL 路由的支持。将以下内容添加到 `firebase.json` 文件的 `hosting` 对象中。

    ```
    "rewrites": [
      {
        "source": "!/__/**",
        "destination": "/index.html"
      },
      {
        "source": "**/!(*.js|*.html|*.css|*.json|*.svg|*.png|*.jpg|*.jpeg)",
        "destination": "/index.html"
      }
    ]
    ```

    例如，您的 `firebase.json` 修改后可能会如下所示：
	
    ```
    {
      "database": {
        "rules": "database.rules.json"
      },
      "hosting": {
        "public": "build/default",
        "rewrites": [
          {
            "source": "!/__/**",
            "destination": "/index.html"
          },
          {
            "source": "**/!(*.js|*.html|*.css|*.json|*.svg|*.png|*.jpg|*.jpeg)",
            "destination": "/index.html"
          }
        ]
      }
    }
    ```	

    这将指示 Firebase 为所有其他的不是以文件扩展名结束的 URL 服务 `index.html` 文件。

1.  部署您的项目。

        firebase deploy

    输出中列出了您的实时站点的 URL。您还可以通过运行 `firebase open hosting:site` 来在您的默认浏览器中打开该站点。

