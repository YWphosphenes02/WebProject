<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useCookies } from 'vue-cookies'

const [cookies] = useCookies()
const email = ref('')
const password = ref('')
const router = useRouter()
const host = "http://127.0.0.1:5000"

async function login() {
  try {
    const response = await axios.post(`${host}/login`, {
      email: email.value,
      password: password.value,
    })
    console.log('Login success:', response.data)
    // 将 token 存储到 cookies 中
    cookies.set('token', response.data.token, '2d'); // 设置 token 有效期为 2 天
    // 登录成功后导航到首页
    router.push('/')
  } catch (error) {
    console.error('Login error:', error)
    alert(error.response.data.error || '登录失败，请重试')
  }
}
</script>

<template>
  <div class="login-container">
    <h2 style="font-weight: bold;font-size: 40px;">登录</h2>
    <form @submit.prevent="login">
      <div>
        <label for="email">邮箱</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div>
        <label for="password">密码</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">登录</button>
    </form>
    <p>还没有账户？<router-link to="/register" style="color: #2a9f76;">注册</router-link></p>
  </div>
</template>

<style scoped>
.login-container {
  width: 700px;
  height: 500px;
  margin: 0 auto;
  color: #ffffff;
  padding: 90px;
  background-color: #ffffff3e;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

form div {
  margin-bottom: 15px;
}

input {
  width: 100%;
  padding: 8px;
  border-radius: 20px;
  border: 1px solid #ccc;
  color: #000000;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #00a8d7;
  color: #fff;
  border: none;
  border-radius: 20px;
  cursor: pointer;
}

button:hover {
  background-color: #008abf;
}
</style>
