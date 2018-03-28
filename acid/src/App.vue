<template>
  <!--入口-->
  <div id="app">
    <el-container style="height: 100%">
      <el-aside style="border-right: #a0fcff">
        <!--命名视图-->
        <router-view class="view three" name="sidebar"></router-view>
      </el-aside>
      <el-container>
        <el-header>
          <router-view class="view two" name="navi"></router-view>
        </el-header>
        <el-main>
          <!--<div class="action-bar">-->
            <!--<div class="operate-bar">-->
              <!--<el-button type="primary" plain>删除</el-button>-->
              <!--<span> </span>-->
              <!--<el-button type="success" round>发布按钮</el-button>-->
            <!--</div>-->
            <!--<div class="display-bar"></div>-->
          <!--</div>-->
          <!--命名视图-->
          <router-view class="view one"></router-view>
        </el-main>
        <el-footer>Footer</el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
  }
}
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 20px;
  }

  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }

  .el-container:nth-child(7) .el-aside + .sidebar{
    line-height: 320px;
  }

</style>
