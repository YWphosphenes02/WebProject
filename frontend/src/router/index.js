import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';       
import Category from '../views/Category.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import BriefIntroduction from '../views/BriefIntroduction.vue'
import Contact from '../views/Contact.vue'; 

const routes = [
  { path: '/', component: Home },
  { path: '/category/:name', component: Category, props: true },
  { path: '/brief-introduction', component: BriefIntroduction},
  {path: '/login',name: 'Login',component: Login,},
  {path: '/register',name: 'Register',component: Register,}, 
  {path: '/contact',name: 'Contact',component: Contact,},
  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
