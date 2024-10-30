import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios';

// 将 axios 添加为全局属性
const app = createApp(App)
app.config.globalProperties.$axios = axios;

app.use(router)
app.mount('#app')
