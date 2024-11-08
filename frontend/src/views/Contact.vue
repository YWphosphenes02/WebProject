<template>
    <div class="shell" id="shell" ref="shell">
      <div class="header">
        <h2 class="title">联系我们</h2>
        <h3 class="subtitle">我们的故事......</h3>
      </div>
      <div class="timeline">
        <!-- 循环渲染时间轴项目 -->
        <div
          v-for="(item, index) in items"
          :key="index"
          :class="['item', { 'item--active': activeIndex === index, 'item--left': index % 2 === 0, 'item--right': index % 2 === 1 }]"
          :data-text="item.title"
        >
          <div class="content">
            <img :src="item.img"  alt="" class="img" />
            <h2 class="content-title" style="font-size: 44px;">{{ item.year }}</h2>
            <p class="content-desc">{{ item.desc }}</p>
          </div>
        </div>
      </div>
    </div>
</template>
  
<script setup>
  import { ref, onMounted, onBeforeUnmount } from 'vue';
  
  // 模拟的时间轴项目数据
  const items = ref([
    {
      img: "https://s21.ax1x.com/2024/11/04/pArjE6J.png",
      year: "01 关于我们",
      desc: "我们创建了这个wiki，希望用我们的努力，帮助更多的人保护环境。同时，我们在线上线下多次举办环境保护活动......"
    },
    {
      img: "https://s21.ax1x.com/2024/11/04/pArjPYT.jpg",
      year: "02 在行动",
      desc: "保护环境的路上，我们需要勇气和毅力。迄今为止，我们的团队已经达到100人，线下环境保护宣讲正在逐步推行，正有更多的人加入我们......"
    },
    {
      img: "https://s21.ax1x.com/2024/11/04/pArjifU.jpg",
      year: "03 联系方式",
      desc: "Email: example@example.com"
    },
    {
      img: "https://s21.ax1x.com/2024/11/04/pArjm01.png",
      year: "04 加入我们",
      desc: "这是一个崭新的开始，让我们共同书写未来。"
    }
  ]);
  
  // 定义当前激活的项目索引
  const activeIndex = ref(0);
  // 引用shell DOM元素
  const shell = ref(null);
  
  // 页面挂载时执行
  onMounted(() => {
    // 设置初始背景图为第一个项目的图片
    shell.value.style.backgroundImage = `url(${items.value[0].img})`;
  
    // 监听滚动事件
    window.addEventListener('scroll', handleScroll);
  });
  
  // 页面销毁前移除滚动事件监听
  onBeforeUnmount(() => {
    window.removeEventListener('scroll', handleScroll);
  });
  
  // 滚动处理逻辑
  function handleScroll() {
    const pos = window.scrollY;
    items.value.forEach((item, index) => {
      const element = document.querySelectorAll('.item')[index];
      const min = element.offsetTop;
      const max = element.offsetHeight + element.offsetTop;
  
      // 如果当前滚动位置在当前项目的最小和最大高度之间
      if (pos >= min && pos <= max) {
        activeIndex.value = index;
        shell.value.style.backgroundImage = `url(${item.img})`;
      }
  
      // 处理最后一个项目激活状态
      if (index === items.value.length - 1 && pos > min + element.offsetHeight + 4 ) {
        activeIndex.value = index;
        shell.value.style.backgroundImage = `url(${item.img})`;
      }
    });
  }
</script>
  
<style>
  * {
    padding: 0;
    margin: 0;
  }
  
  .shell {
    width: 166vh;
    height: 210vh;
    top: -2vh;
    position: relative;
    padding: 60px 0;
    transition: 0.3s ease 0s;
    background-attachment: fixed;
    background-size: cover;
  }
  
  .shell::before {
    position: absolute;
    left: 0;
    top: 0;
    width: 166vh;
    height: 210vh;
    background: rgba(99, 99, 99, .8);
    content: "";
  }
  
  .header {
    width: 100%;
    text-align: center;
    margin-bottom: 80px;
    position: relative;
  }
  
  .title {
    color: #fff;
    font-size: 46px;
    font-weight: normal;
    margin: 0;
  }
  
  .timeline {
    display: flex;
    margin: 0 auto;
    flex-wrap: wrap;
    flex-direction: column;
    max-width: 700px;
    position: relative;
  }
  
  .content-title {
    font-weight: normal;
    font-size: 66px;
    margin: -10px 0 0 0;
    transition: 0.4s;
    padding: 0 10px;
    box-sizing: border-box;
    color: #fff;
  }
  
  .content-desc {
    margin: 0;
    font-size: 15px;
    box-sizing: border-box;
    color: rgba(255, 255, 255, .7);
    line-height: 25px;
  }
  
  .timeline::before {
    position: absolute;
    left: 50%;
    width: 2px;
    height: 130vh;
    margin-left: -1px;
    content: "";
    background: rgba(255, 255, 255, .07);
  }
  
  .item {
    padding: 40px 0;
    opacity: 0.3;
    filter: blur(2px);
    transition: 0.5s;
    box-sizing: border-box;
    width: calc(50% - 40px);
    display: flex;
    position: relative;
    transform: translateY(-80px);
  }
  
  .item--active {
    opacity: 1;
    transform: translateY(0);
    filter: blur(0px);
  }
  
  .item--active::before {
    top: 50%;
    transition: 0.3s all 0.2s;
    opacity: 1;
  }
  
  .item--active .content-title {
    margin: -50px 0 20px 0;
  }
  
  .item--left {
  align-self: flex-start;
  padding-right: 40px;
  }

  .item--right {
    align-self: flex-end;
    padding-left: 40px;
  }

  .img {
    max-width: 100%;
    box-shadow: 0 10px 15px rgba(0, 0, 0, .4);
  }
  
  .subtitle {
    color: rgba(255, 255, 255, .5);
    font-size: 1rem;
    letter-spacing: 5px;
    margin: 10px 0 0 0;
    font-weight: normal;
  }
  
  @media only screen and (max-width: 767px) {
    .item {
      align-self: baseline !important;
      width: 100%;
      padding: 0 30px 150px 80px;
    }
  
    .timeline::before {
      left: 40px;
    }
  }
</style>
  