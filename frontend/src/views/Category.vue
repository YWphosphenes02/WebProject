<template>
  <div>
    <h1>{{ categoryTitle }} 的文章</h1>
    <div v-if="articles.length">
      <div v-for="article in articles" :key="article._id">
        <h2>{{ article.title }}</h2> <!-- 根据后端字段，使用 title 显示文章标题 -->
        <p v-html="article.content_html"></p> <!-- 使用 v-html 显示 HTML 格式化后的内容 -->
      </div>
    </div>
    <div v-else>
      <p>没有找到相关的内容。</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
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
    }
  },
  mounted() {
    this.fetchArticles(this.name); // 使用类别名称作为关键词进行搜索
  },
  methods: {
    async fetchArticles(keyword) {
      try {
        const response = await axios.get(`http://localhost:5000/api/wiki/search?keyword=${keyword}`); // 修改为后端端口5000
        this.articles = response.data; // 后端返回文章列表
      } catch (error) {
        console.error('搜索文章失败:', error);
      }
    }
  }
};
</script>
