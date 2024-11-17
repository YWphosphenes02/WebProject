<template>
  <div>
    <h1>{{ categoryTitle }} 的文章</h1>
    <div class="output" v-html="content"></div>
    <div v-if="articles.length"></div>
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
    },
    content() {
      const output = marked(article_markdown.value)
      return output
    }
  },
  watch: {
    // 监听路由参数变化
    name(newName, oldName) {
      console.log(`路由参数从 ${oldName} 更新为 ${newName}`);
      this.fetchArticles(newName);
    },
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
