this README.md file is encoded in GBK.

## 声明
本项目仅供零杯网页设计大赛参赛使用，请勿用于其余用途。

## 项目介绍

2024年零杯网页设计大赛零组的项目，主题为环境保护，网页性质为Wiki站。主要功能包括用户注册、登录、文章发布、文章编辑、文章删除等，部分简单功能具有响应式布局，同时首页具有视差滚动功能。

## 团队介绍

- 吴宇铮：大一本科生，电子信息学院，本次负责前端开发、部分后端、部分数据库设计开发、网页设计、前后端联动、测试网页运行。
- 贺攀如（队长）：大一本科生，电子信息学院，本次负责搜集wiki资料。
- 胡雨飞：大一本科生，电子信息学院，本次负责部分数据库设计。
- 张顾峰：大一本科生，网络安全学院，本次负责部分后端开发。

零杯零组 **“实在想不出来叫什么队”** 的队员们，感谢你们的付出！——吴宇铮

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


首先，保证安装了 Node.js 环境、 Python3 环境和MongoDB 数据库(默认端口为27017)，然后安装依赖：

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

注意：请确保 所有环境都已按照上述步骤配置完毕。若仍然无法运行，请联系发送来的邮箱。

## 界面规格

菜单栏具有简单的响应式布局，**推荐使用标准比例**查看。

## 网页展示（以防操作不当或环境问题导致展示效果不佳）
![首页](/Showup/7974DC678ED0876C6B4ED0D326F86117.png)
![登录页面](/Showup/E7BACF19148073D45978FE367DF1DCB4.png)
![文章展示页面1](/Showup/0B1B133DEC80878BAD4DA5DECFABFA13.png)
![文章展示页面2](/Showup/B4262AF5DADFFEA19B364DFDD5E04E37.png)
![文章展示页面3](/Showup/D30770DFF89C16D8AA6BAD84761838ED.png)
![关于界面](/Showup/CAB445189EBC1DD14AD8ACD38F60BB27.png)

## 开发记录

### 已完成功能
1. 用户认证
实现了用户登录和注册功能，包括密码加密存储和验证。
用户登录状态通过 cookies 进行管理，使用 js-cookie 库操作 cookies。
2. 路由管理
使用 vue-router 管理前端路由，实现了首页、分类页面、联系我们页面以及登录注册页面的导航。
3. 文章展示
Category.vue 组件用于展示特定分类下的文章列表。
MarkdownEditor.vue 组件用于解析和展示 Markdown 格式的文章内容。
4. 后端接口
使用 Flask 和 MongoDB 搭建后端，实现了文章的增删改查功能。
通过 axios 发送请求与后端进行数据交互，包括获取文章列表、根据标题搜索文章等。
5. 前端界面
设计并实现了响应式的前端界面，包括导航栏、搜索栏和文章展示区域。
使用 Vue 3 的 <script setup> 语法简化组件代码。

### 待解决问题

1. 搜索栏功能不完整
当前搜索栏虽然能够发送搜索请求，但未能将搜索结果导向至结果页面。需要实现搜索结果的展示逻辑，并确保用户可以看到搜索结果。
2. 文章内容展示
文章内容的字体未来得及调整，感官上并不优秀，需要调整 CSS 以达到更好的阅读体验。
3. 性能优化
考虑实现文章列表的分页加载，以提高页面加载性能。
4. 错误处理
需要增加更详细的错误处理和用户反馈机制，以提升用户体验。
5. Markdown 编辑器
Markdown 编辑器的功能还不够完善，由于时间不足，最终决定弃置该组件。由于编辑器暂未实现，所以在初始化数据库时预先放入若干篇文章作为内容来返回。
6. SEO优化
目前网站的 SEO 优化还不够，需要进行 SEO 优化以提升网站的搜索排名。
7. wiki内容
目前网站的 wiki 内容还不够丰富，负责收集内容的队员不够了解wiki形式，需要进行内容的丰富。
8. Admin用户
目前网站只有普通用户，未来会创建一个超级管理员账户用于未来增添、删除文章。

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

