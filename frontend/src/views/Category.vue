<template>
  <div>
    <h1>{{ categoryTitle }} 的文章</h1>
    <div class="output" v-html="content"></div>
    <div v-if="articles.length">
      <!-- <div v-for="article in articles" :key="article._id">
        <h2>{{ article.title }}</h2> 
        <p>{{ article }}</p>
        <MarkdownEditor :content="article.content" /> 
      </div> -->
    </div>
    <div v-else>
      <p>没有找到相关的内容。</p>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';
import MarkdownEditor from './MarkdownEditor.vue'; 
import { Base64 } from 'js-base64';
import { marked } from 'marked'
const host = "http://127.0.0.1:5000";
const article_markdown = ref("")

export default {
  // components: {
  //   MarkdownEditor
  // },
  props: ['name'], // 接收从路由传递的参数
  data() {
    return {
      articles: [] // 存储搜索结果
    };
  },
  computed: {
    categoryTitle() {
      const categoryMap = {
        news: '新闻',
        water: '水资源',
        forest: '森林资源',
        minerals: '矿产资源',
        international: '国际合作',
        policy: '政府政策',
        community: '社区参与'
      };
      return categoryMap[this.name] || '未知类别';
    },
    content() {
      const output = marked(article_markdown.value)
      return output
    }
  },
  mounted() {
    this.fetchArticles(this.name); // 使用类别名称作为关键词进行搜索
  },
  methods: {
    async fetchArticles(keyword) {
      try {
        
        const response = await axios.get(`${host}/get_articles_by_category?category=${keyword}`); 
        console.log(Base64.decode(response.data[0]['content']))
        article_markdown.value = Base64.decode(response.data[0]['content']); // 解码 Markdown 内容
      } catch (error) {
        console.error('搜索文章失败:', error);
      }
    }
  }
};
</script>

<style>
/* 设置整体背景和字体颜色 */
body {
  background: linear-gradient(to right, #3fb775, #00a8d7); 
  min-height: 100vh;
  margin: 0;
  padding: 0;
  color: black; /* 设置默认字体颜色为黑色 */
}

/* 设置文章内容区域样式 */
.output {
  max-width: 80%; /* 设置最大宽度 */
  margin: 0 auto; /* 居中显示 */
  padding: 20px;
  box-sizing: border-box;
  color: black; /* 确保文章内容字体颜色为黑色 */
}

/* 设置标题和段落样式 */
h1, h2 {
  color: rgba(0, 0, 0, 0.865); /* 标题字体颜色 */
  font-weight: bold; /* 加粗标题 */
}

p {
  color: black; /* 段落字体颜色 */
}

/* 设置链接样式 */
a {
  color: #4500b3; /* 修改链接颜色 */
  text-decoration: none; /* 去除下划线 */
}

a:hover {
  color: #35008b; /* 鼠标悬浮时链接颜色 */
  text-decoration: underline; /* 鼠标悬浮时添加下划线 */
}
</style>