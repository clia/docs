---
title: Step 4. Deploy
subtitle: "Build an app with App Toolbox"
---

<!-- toc -->

在此步骤中，您将把应用部署到 Web 上。

## 为部署而构建

输入 `polymer build` 来为生产环境构建您的 Polymer 应用。

您可以向浏览器服务您的 App 的不同的构建，支持不同的能力。Polymer 入门套件被配置成生成三种构建：

* 一种打包的、最小化的构建，提供服务工作者，编译为 ES5 以兼容旧的浏览器。
* 一种打包的、最小化的构建，提供服务工作者，ES6 代码以原样服务。这种构建是用于那些能处理 ES6 代码的浏览器。
* 一种未打包的、最小化的构建，提供服务工作者，ES6 代码以原样服务。这种构建是用于那些能支持 HTTP/2 服务器推技术的浏览器。

在这一步中，您将会部署一种打包的、编译的构建 (`es5-bundled`)，以提供最大的兼容性。服务其他形式的构建需要更复杂的服务器设置。

构建种类已在项目根目录下的一个配置文件 `polymer.json` 中的 `builds` 对象下配置了。

polymer.json { .caption}
```
...
"builds": [
  {
    "preset": "es5-bundled"
  },
  {
    "preset": "es6-bundled"
  },
  {
    "preset": "es6-unbundled"
  }
]
...
```

构建的文件将被输出到 `build/` 目录的子目录中，如下所示：

    build/
      es5-bundled/
      es6-bundled/
      es6-unbundled/

要配置一种自定义的构建，您可以使用命令行选项，或者编辑 `polymer.json`。运行 `polymer help build` 以查看所有可用选项和优化项的列表。
另外，查看这些文档： [polymer.json 规范](https://www.polymer-project.org/2.0/docs/tools/polymer-json) 和 [为生产环境构建您的 Polymer 应用](https://www.polymer-project.org/2.0/toolbox/build-for-production)。

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
      static_dir: build/es5-bundled/bower_components
      secure: always

    - url: /images
      static_dir: build/es5-bundled/images
      secure: always

    - url: /src
      static_dir: build/es5-bundled/src
      secure: always

    - url: /manifest.json
      static_files: build/es5-bundled/manifest.json
      upload: build/es5-bundled/manifest.json
      secure: always

    - url: /.*
      static_files: build/es5-bundled/index.html
      upload: build/es5-bundled/index.html
      secure: always
    ```

1. 将您的项目 ID 设置为 App Engine 提供给您的 App 的ID。例如：
   
       gcloud config set project my-app-164409

1. 创建您的 App：
   
       gcloud app create
     
   您将需要为您的 App 选择要部署的区域。这不能更改。

1. 部署您的 App：
   
       gcloud app deploy

1. 您的 App 将在其指定的 URL 上在线提供。例如：
   
       https://my-app-164409.appspot.com/new-view
   
   通过键入以下命令在浏览器中打开您的 App 的 URL：
   
       gcloud app browse

### 使用 Firebase 部署

以下说明基于 [Firebase 托管快速入门指南](https://www.firebase.com/docs/hosting/quickstart.html)。

1.  [注册一个 Firebase 帐号](https://www.firebase.com/signup/)。

1.  转到 [https://www.firebase.com/account](https://www.firebase.com/account) 去创建一个新的 App。记下与您的 App 关联的项目 ID。

    ![Welcome to Firebase showing Project ID](/images/2.0/toolbox/welcome-firebase.png)

1.  安装 Firebase 命令行工具。

        npm install -g firebase-tools

1.  `cd` 进入您的项目目录。

1.  初始化 Firebase 应用。

        firebase login
        firebase init

1.  Firebase 会询问与您的 App 关联的项目。选择您之前创建的。

1.  Firebase 会询问您的 App 的公共目录的名称。输入 `build/es5-bundled/`。

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
        "public": "build/es5-bundled/",
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

