<script setup>
import { marked } from 'marked'
import { debounce } from 'lodash-es'
import { ref, computed } from 'vue'

const props = defineProps({
  content: String
});

const input = ref(props.content);

const output = computed(() => marked(input.value));

const update = debounce((e) => {
  input.value = e.target.value;
}, 100);
</script>

<template>
  <div class="editor">
    <textarea class="input" :value="input" @input="update"></textarea>
    <div class="output" v-html="output"></div>
  </div>
</template>

<style>
body {
  margin: 0;
  width: 100%;
}

.editor {
  height: 100vh;
  display: flex;
}

.input,
.output {
  overflow: auto;
  text-align: left;
  box-sizing: border-box;
  padding: 40px;
  color: #ffffffdb;
  font-size: 2.7ch;
}

.input {
  border: none;
  border-right: 1px solid #ccc;
  resize: none;
  outline: none;
  background-color: #f6f6f6;
  font-size: 17px;
  font-family: 'Monaco', courier, monospace;
  padding: 20px;
}

code {
  color: #f66;  
}

a {
  color: #4861efce; /* 修改链接颜色 */
  text-decoration: none; /* 去除下划线 */
}

a:hover {
  color: #004a9f; 
  text-decoration: underline; 
}

</style>