<template>
  <div id="navigation">
    <header class="header">
      <div class="title">
        <a href="#">
          <img src="#" alt="" class="title-img">
          <div class="title-name">
            <h3>sfsfs</h3>
          </div>
        </a>
      </div>
      <div class="navbar">
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal">
          <el-menu-item index="1" >云之舞台</el-menu-item>
          <el-submenu index="2">
            <template slot="title">......</template>
            <el-menu-item index="2-1">选项1</el-menu-item>
            <el-menu-item index="2-2">选项2</el-menu-item>
            <el-menu-item index="2-3">选项3</el-menu-item>
            </el-submenu>
        </el-menu>
      </div>
      <div class="login register">
        <router-link to="/login">
          <el-tag type="success">登陆</el-tag>
        </router-link>
        <router-link to="/register">
        <el-tag type="info">注册</el-tag>
        </router-link>
      </div>
    </header>
  </div>
</template>

<script>

export default {
  // 组件名
  name: 'navigation',
  data () {
    return {
      activeIndex: '1',
      activeIndex2: '1',
      title: 'AcidSmog'
    }
  }
}
</script>
<style scoped>
  .title {
    color: #3edaca;
    position: relative;
    float: left;
  }
  .navbar {
    position: relative;
    display: block;
    float: left;
  }
</style>
