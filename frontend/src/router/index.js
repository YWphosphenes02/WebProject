import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';        // 路径指向 views 文件夹
import Category from '../views/Category.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import BriefIntroduction from '../views/BriefIntroduction.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/category/:name', component: Category, props: true },
  { path: '/brief-introduction', component: BriefIntroduction},
  {path: '/login',name: 'Login',component: Login,},
  {path: '/register',name: 'Register',component: Register,}, 
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
