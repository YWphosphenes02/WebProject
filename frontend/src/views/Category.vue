<template>
  <div>
    <h1>{{ categoryTitle }} 的文章</h1>
    <div v-if="articles.length">
      <div v-for="article in articles" :key="article._id">
        <h2>{{ article.title }}</h2> <!-- 根据后端字段，使用 title 显示文章标题 -->
        <MarkdownEditor :content="article.content" /> <!-- 使用 MarkdownEditor 显示 Markdown 内容 -->
      </div>
    </div>
    <div v-else>
      <p>没有找到相关的内容。</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import MarkdownEditor from './MarkdownEditor.vue'; // 确保路径正确

const host = "http://127.0.0.1:5000";

export default {
  components: {
    MarkdownEditor
  },
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
        const response = await axios.get(`${host}/get_articles_by_category?keyword=${keyword}`); 
        this.articles = response.data;
      } catch (error) {
        console.error('搜索文章失败:', error);
      }
    }
  }
};
</script>