<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const router = useRouter()
const host = "http://127.0.0.1:5000"

async function register() {
  if (password.value !== confirmPassword.value) {
    alert('密码不一致')
    return
  }

  try {
    const response = await axios.post(`${host}/register`, {
      email: email.value,
      password: password.value,
    })
    console.log('Register success:', response.data)
    // 将token存储到cookies中
    if (response.headers['set-cookie']) {
      const cookies = response.headers['set-cookie'].map(cookie => cookie.split(';')[0]).join('; ')
      document.cookie = cookies
    }
    // 注册成功后导航到登录页面
    router.push('/login')
  } catch (error) {
    console.error('Register error:', error)
    alert(error.response.data.error || '注册失败，请重试')
  }
}
</script>

<template>
  <div class="register-container">
    <h2 style="font-weight: bold;font-size: 40px;">注册</h2>
    <form @submit.prevent="register">
      <div>
        <label for="email">邮箱</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div>
        <label for="password">密码</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <div>
        <label for="confirmPassword">确认密码</label>
        <input type="password" id="confirmPassword" v-model="confirmPassword" required />
      </div>
      <button type="submit">注册</button>
    </form>
    <p>已有账户？<router-link to="/login" style="color: #2a9f76;">登录</router-link></p>
  </div>
</template>

<style scoped>
.register-container {
  width: 700px;
  height: 500px;
  margin: 0 auto;
  color: #ffffff;
  padding: 90px;
  background-color: #ffffff3e;
  border-radius: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

form div {
  margin-bottom: 15px;
}

input {
  width: 100%;
  padding: 8px;
  border-radius: 20px;
  border: 1px solid #cccccc;
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
