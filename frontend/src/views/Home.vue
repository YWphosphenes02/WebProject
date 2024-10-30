<template>
    <div class="parallax-container">
      <!-- 背景层-->
      <div class="parallax-background">
        <div class="background-image" style="top: 0%; left: 0%;">
          <img src="../assets/image/hill1.png" />
        </div>
        <div class="background-image" style="top: 0%; left: 0%;">
          <img src="../assets/image/hill2.png" />
        </div>
        <div class="background-image" style="top: 0%; left: 0%;">
          <img src="../assets/image/hill3.png" />
        </div>
      </div>
  
      <!-- 中景层-->
      <div class="parallax-midground">
        <h1 class="welcome-text"style="font-weight: bolder;text-shadow: 1px 1px 2px rgba(0,30,20,0.5);font-weight: bold;">欢迎来到自然资源保护 Wiki。</h1>
        <img src="../assets/image/hill4.png" class="midground-image" style="top: 0%; left: 0%;">
        <img src="../assets/image/hill5.png" class="midground-image" style="top: 0%; left: 0%;">
        <img src="../assets/image/tree.png" class="midground-image" style="top: 0%; left: 0%;">
      </div>
  
      <!-- 近景层-->
      <div class="parallax-foreground">
        <img src="../assets/image/plant.png" class="foreground-image" style="top: 0%; left: 0%;">
        <img src="../assets/image/leaf.png" class="foreground-image" style="top: 0%; left: 0%;">
      </div>
  
     
      <div class="importance-text" ref="importanceText" id="importanceText">
        <h2>为什么环境保护很重要？</h2><br>
        <p>环境保护关系到地球的可持续发展。通过保护自然资源和减少污染，<br>我们正在努力确保子孙后代能够享有清洁的空气、水和食物。</p><br>
        <button onclick="window.location.href='../Category/water'" class="btn-importance" style="width: 100px; height: 50px;border-radius: 30px;color:white;background-color:rgba(200,255,230,0.3);border:none;font-size:16px;cursor:pointer;">了解更多</button>
      </div>
    </div>
  </template>
  
  <style>
  /* 容器样式 */
  .parallax-container {
    position: absolute;
    width: 166vh;
    height: 200vh; 
    overflow: hidden;
  }
  
  /* 背景层 */
  .parallax-background {
  position: absolute;
  top: 50vh;
  left: 0;
  width: 100%;
  height: 100vh;
  z-index: -3;
  background-size: cover; 
  background-position: center; 
  background-repeat: no-repeat; 
}

  
  /* 背景图片容器 */
  .background-image {
    position: absolute;
    top: 50vh;
    left: 0;
    width: 100%;
    height: 100vh;
    z-index: -2;
  }
  
  /* 背景图片 */
  .background-image img {
    width: 100%;
    height: 100vh;
  }
  
  /* 中景层 */
  .parallax-midground {
    position: absolute;
    top: 50vh;
    left: 0;
    width: 100%;
    height: 100vh;
    z-index: -2;
    transform: translateY(0);
  }
  
  /* 欢迎文字 */
  .welcome-text {
    position: fixed;
    z-index: 2;
    top: 30%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: rgb(255, 255, 255);
    font-size: 3rem;
  }
  
  /* 中景图片 */
  .midground-image {
    position: absolute;
    width: 100%;
    height: 100vh;
    z-index: 1; 
  }
  
  /* 近景层 */
  .parallax-foreground {
    position: absolute;
    top: 35vh;
    left: 0;
    width: 100%;
    height: 100vh;
    z-index: -1;
  }
  
  /* 近景图片 */
  .foreground-image {
    position: absolute;
    width: 100%;
    height: 200vh;
    z-index: 3; 
  }
  

  
  /* 重要性介绍文字*/
  .importance-text {
    opacity: 0;
    transition: opacity 1s ease-in-out;
    padding: 1500px 20px;
    text-align: center;
    color: #ffffff;
    z-index: -1;
  }

  .importance-text.btn-importance:hover {
    background-color: rgba(200,255,230,0.8);
  }

  
  .importance-text.visible {
    opacity: 80%;
  }

  

  @media screen and (max-width: 768px) {
    .welcome-text{
       font-size: 2rem;
    }
  }
  </style>
  
  <script>
  export default {
    mounted() {
      window.addEventListener('scroll', this.handleScroll);
      this.$emit('setImportanceRef', this.$refs.importanceText);
    },
    beforeDestroy() {
      window.removeEventListener('scroll', this.handleScroll);
    },
    methods: {
      handleScroll() {
        const scrollPosition = window.pageYOffset;
  
        // 视差效果：背景层
        const background = document.querySelector('.parallax-background');
        background.style.transform = `translateY(${scrollPosition * 0.5}px)`;
  
        // 中景层
        const midground = document.querySelector('.parallax-midground');
        midground.style.transform = `translateY(${scrollPosition * 0.3}px)`;
  
        // 文字淡入
        const importanceText = this.$refs.importanceText;
        if (scrollPosition > 450) {
          importanceText.classList.add('visible');
        } else {
          importanceText.classList.remove('visible');
        }
        // 控制箭头显示
        if (scrollPosition + windowHeight >= totalHeight || scrollPosition > 100) {
          this.showArrows = false; // 滑动到底部或者超过100px时隐藏箭头
        } else {
          this.showArrows = true; // 在顶部时显示箭头
        }
      }
    }
  }
  
  </script>
  