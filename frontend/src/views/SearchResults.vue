<template>
    <div>
      <h1>搜索结果</h1>
      <ul>
        <li v-for="article in articles" :key="article._id">
          <h2>{{ article.title }}</h2>
          <p>{{ article.content }}</p>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      articles: Array,
    },
  };
  </script>