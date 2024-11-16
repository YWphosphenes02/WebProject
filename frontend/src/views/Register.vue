<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import Cookies from 'js-cookie'

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
    const response = await axios({
      method: 'post',
      url: `${host}/register`,
      data: {
        'email': email.value,
        'password': password.value
      },
      withCredentials: false
    })
    console.log('Register success:', response.data)
    if (response.data.token) {
      Cookies.set('token', response.data.token, { expires: 2 }); // 设置 token 有效期为 2 天
      router.push('/login')
    }
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

@media screen and (max-width: 768px) {
  .register-container {
    width: 90%;
    height: auto;
    padding: 50px;
  }
}
</style>
