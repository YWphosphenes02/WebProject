## 声明
本项目仅供零杯网页设计大赛参赛使用，请勿用于其余用途。

## 项目介绍

2024年零杯网页设计大赛零组的项目，主题为环境保护，网页性质为Wiki站。主要功能包括用户注册、登录、文章发布、文章编辑、文章删除等，部分简单功能具有响应式布局，同时首页具有视差滚动功能。

## 技术栈

本项目使用了 **Vue3** 作为前端框架，使用 **Axios** 库与后端进行 HTTP 通信，使用**mongoDB**作为后端数据库；
同时使用 vue-router 库管理页面路由，使用 js-cookie 库管理浏览器中的 cookies，使用 marked 库将 Markdown 文本转换为 HTML，使用 lodash-es 库提供实用的函数。

本项目使用了以下开源库来增强功能和简化开发流程：

- **axios**：用于与后端进行 HTTP 通信，处理登录、注册和数据检索等请求。
- **js-cookie**：管理浏览器中的 cookies，用于维护用户的登录状态。
- **vue-router**：Vue.js 的官方路由管理器，用于创建单页应用程序的页面路由和导航。
- **marked**：将 Markdown 文本转换为 HTML，以便在前端显示格式化的内容。
- **lodash-es**：提供实用的函数，用于实现防抖等功能性操作。

## 项目结构

本项目的前端代码位于 `frontend` 目录，后端代码位于 `backend` 目录。
简单目录结构如下：

```
├── README.md
├── requirements.txt
├── frontend
│   ├── public
│   ├── src
│   │   ├── App.vue
│   │   ├── assets
│   │   ├── components
│   │   ├── main.js
│   │   ├── router
│   │   └── views
│   ├── index.html
│   ├── jsconfig.json
│   ├── package.json    
│   ├── package-lock.json
│   └── vue.config.js
└── backend
    ├── app.py
    └── __pycache__
```

## 运行项目


首先，保证安装了 Node.js 环境和 Python3 环境，然后安装依赖：

```bash
pip install -r requirements.txt

```

### 前端
首先，安装依赖：

```bash
cd frontend
npm install
```

运行项目：

```bash
npm run dev
```

### 后端

首先，安装依赖：

```bash
cd backend
pip install 

```

运行项目：

```bash
flask run
```

## 界面规格

菜单栏具有简单的响应式布局，**推荐使用标准比例**查看。

## 注意事项

- 请不要在生产环境中使用本项目，仅供参赛使用。
- 请不要在生产环境中使用 MongoDB，仅供开发环境使用。
- 请不要在生产环境中使用 js-cookie，仅供开发环境使用。

## 鸣谢

- icon图标库：[iconfont](https://igoutu.cn/icons)
- 前端首页图像来源：[Element Pic](https://github.com/zbf1999/note/tree/master/parallaxScrollingWebsite01) 
    ————**注意：本项目视差滚动代码并未参考此来源，请仔细甄别！**
- 前端框架：[Vue.js](https://cn.vuejs.org/)
- 后端框架：[Flask](https://flask.palletsprojects.com/en/1.1.x/)
- 后端数据库：[MongoDB](https://www.mongodb.com/)

