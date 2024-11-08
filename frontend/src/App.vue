<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const isSearchExpanded = ref(false)
const searchQuery = ref('')
const host = "http://127.0.0.1:5000"

// 用于保存登录状态
const isLoggedIn = ref(false)

function toggleSearch() {
  isSearchExpanded.value = !isSearchExpanded.value
}

function collapseSearch() {
  isSearchExpanded.value = false
}

// 搜索功能
async function performSearch() {
  if (searchQuery.value) {
    try {
      const response = await axios.get(`${host}/search`, { params: { keyword: searchQuery.value } })
      console.log('Search results:', response.data)
    } catch (error) {
      console.error('Error searching:', error)
    }
  }
}

// 检查用户登录状态
async function checkLoginStatus() {
  try {
    const response = await axios.get(`${host}/check-login`)
    isLoggedIn.value = response.data.loggedIn
  } catch (error) {
    console.error('Error checking login status:', error)
  }
}

// 登出功能
async function logout() {
  try {
    await axios.post(`${host}/logout`)  // 调用后端登出 API
    isLoggedIn.value = false  // 更新状态为未登录
  } catch (error) {
    console.error('Error logging out:', error)
  }
}

// 页面加载时检查登录状态
onMounted(() => {
  checkLoginStatus()
})

</script>

<template>
  <div id="app">
    <nav class="navbar">
      <div class="nav-center">
        <ul class="nav-menu">
          <li class="menu-item">
            <router-link to="/">首页</router-link>
            <ul class="dropdown">
              <li><router-link to="/brief-introduction">概览</router-link></li>
              <li><router-link to="/category/news">新闻</router-link></li>
            </ul>
          </li>
          <li class="menu-item">
            <router-link to="#">资源类型</router-link>
            <ul class="dropdown">
              <li><router-link :to="{ path: '/category/water' }">水资源</router-link></li>
              <li><router-link :to="{ path: '/category/forest' }">森林资源</router-link></li>
              <li><router-link :to="{ path: '/category/minerals' }">矿产资源</router-link></li>
            </ul>
          </li>
          <li class="menu-item">
            <router-link to="#">保护行动</router-link>
            <ul class="dropdown">
              <li><router-link :to="{ path: '/category/international' }">国际合作</router-link></li>
              <li><router-link :to="{ path: '/category/policy' }">政府政策</router-link></li>
              <li><router-link :to="{ path: '/category/community' }">社区参与</router-link></li>
            </ul>
          </li>
          <li class="menu-item">
            <router-link to="/contact">联系我们</router-link>
          </li>
        </ul>

        <div class="search-container">
          <img src="../src/assets/image/search-icon.png" class="search-icon" @click="toggleSearch" />
          <input 
            type="text" 
            class="search-input" 
            :class="{ expanded: isSearchExpanded }" 
            @blur="collapseSearch" 
            placeholder="搜索..." 
            v-model="searchQuery" 
            @keydown.enter="performSearch" 
          />
        </div>
      </div>

      <!-- 根据登录状态动态显示登录/注销 -->
      <ul class="nav-right">
        <li v-if="!isLoggedIn" class="menu-item"><router-link to="/login">登录</router-link></li>
        <li v-if="!isLoggedIn" class="menu-item"><router-link to="/register">注册</router-link></li>
        <li v-if="isLoggedIn" class="menu-item"><a @click="logout">登出</a></li>
      </ul>
    </nav>

    <transition name="fade" mode="out-in">
      <router-view></router-view>
    </transition>
  </div>
</template>

<style>
/* 设置蓝绿渐变的背景 */
body {
  background: linear-gradient(to right, #3fb775, #00a8d7); 
  min-height: 100vh;
  margin: 0;
  padding: 0;
}

/* 设置导航栏 */
.navbar {
  position: fixed; 
  top: 0; 
  left: 0; 
  right: 0;
  background-color: rgba(255, 255, 255, 0.3);
  padding: 10px 0;
  display: flex;
  justify-content: space-between; 
  z-index: 1000; 
}

.nav-center {
  display: flex;
  flex-grow: 1; /* 允许此部分扩展以居中 */
  justify-content: center; /* 将子元素居中 */
}

.nav-right {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
}
.nav-menu {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
}
/* 搜索栏容器 */
.search-container {
  display: flex;
  align-items: center;
}

.search-icon {
  width: 32px;
  height: 32px;
  cursor: pointer;
}

.search-input {
  width: 0;
  opacity: 0;
  transition: width 0.3s ease, opacity 0.3s ease;
  border: none;
  border-radius: 20px;
  padding: 5px 10px;
  margin-left: 10px;
}

.search-input.expanded {
  width: 150px;
  opacity: 1;
}

.search-input:focus {
  outline: none;
  border: 1px solid #00a8d7; /* 设置搜索框的边框样式 */
}

/* 导航栏菜单项样式 */
.navbar .menu-item {
  position: relative;
  margin-right: 20px;
}

.navbar .menu-item a {
  text-decoration: none;
  color: rgb(255, 255, 255);
  padding: 10px 20px;
  display: block;
  border-radius: 20px; /* 圆角按钮 */
  transition: background-color 0.3s ease;
}

.navbar .menu-item a:hover {
  background-color: rgba(255, 255, 255, 0.2);
}

/* 设置悬停时显示下拉菜单 */
.menu-item .dropdown {
  display: none;
  position: absolute;
  top: 40px; /* 子菜单出现在按钮下方 */
  left: 0;
  background-color: rgba(255, 255, 255, 0.475);
  border-radius: 10px;
  padding: 5px;
}

.menu-item .dropdown li {
  margin: 0;
}

.menu-item .dropdown li a {
  color: #047f79;
  padding: 5px 15px;
  display: block;
  text-align: left;
  border-radius: 10px;
  transition: background-color 0.3s ease;
}

.menu-item .dropdown li a:hover {
  background-color: rgba(0, 161, 64, 0.393); /* 子菜单悬停效果 */
}

/* 当悬停时显示下拉菜单 */
.menu-item:hover .dropdown {
  display: block;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter, .fade-leave-to /* .fade-leave-active 在 Vue 2.x 中 */ {
  opacity: 0;
}

/* 保证整个页面的内容居中 */
#app {
  text-align: center;
  display: flex;
  flex-direction: column; 
  align-items: center; 
  justify-content: center; 
  min-height: 100vh; 
  padding-top: 41px; 
  width: 100%; 
}

/* 响应式布局 */
@media screen and (max-width: 768px) {
  .navbar ul {
    flex-direction: column; 
    padding: 10px;
  }

  .navbar .menu-item {
    margin-bottom: 10px; 
    margin-right: 0;
  }

  .navbar .menu-item a {
    padding: 10px 15px; 
  }
}

@media screen and (max-width: 480px) {
  .navbar ul {
    padding: 5px;
  }

  .navbar .menu-item a {
    padding: 8px 12px; 
    font-size: 14px; 
  }
}
</style>
