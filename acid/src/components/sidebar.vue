<template>
  <div id="sidebar" style="width: 100%">
    <!--<el-row class="tac" :gutter="20">-->
      <!--<el-col :span="12">-->
        <!--<h5>自定义颜色</h5>-->
        <!--<el-menu-->
          <!--default-active="2"-->
          <!--class="el-menu-vertical-demo"-->
          <!--@open="handleOpen"-->
          <!--@close="handleClose"-->
          <!--background-color="#545c64"-->
          <!--text-color="#fff"-->
          <!--active-text-color="#ffd04b">-->
          <!--<el-submenu index="1">-->
            <!--<template slot="title">-->
              <!--<i class="el-icon-location"></i>-->
              <!--<span>云海</span>-->
            <!--</template>-->
            <!--<el-menu-item-group>-->
              <!--<template slot="title">-->
                <!--<a v-link="{path:'/'}"></a>-->
              <!--</template>-->
              <!--<el-menu-item index="1-1">选项1</el-menu-item>-->
              <!--<el-menu-item index="1-2">选项2</el-menu-item>-->
            <!--</el-menu-item-group>-->
            <!--<el-menu-item-group title="所有图片">-->
              <!--<el-menu-item index="1-3">选项3</el-menu-item>-->
            <!--</el-menu-item-group>-->
          <!--</el-submenu>-->
          <!--<el-menu-item index="2">-->
            <!--<i class="el-icon-menu"></i>-->
            <!--<span slot="title">所有图片</span>-->
          <!--</el-menu-item>-->
          <!--<el-menu-item index="3" disabled>-->
            <!--<i class="el-icon-document"></i>-->
            <!--<span slot="title">所有视频</span>-->
          <!--</el-menu-item>-->
          <!--<el-menu-item index="4">-->
            <!--<i class="el-icon-setting"></i>-->
            <!--<span slot="title">私有</span>-->
          <!--</el-menu-item>-->
        <!--</el-menu>-->
      <!--</el-col>-->
    <!--</el-row>-->

    <el-row :gutter="30">
      <el-col :xs="4" :sm="6" :md="4" :lg="4">
        <div>
          <el-menu default-active="1" class="el-menu-vertical-demo" style="min-height:800px">
            <el-menu-item index="1"><i class="el-icon-message"></i>导航一</el-menu-item>
            <el-menu-item index="2"><i class="el-icon-menu"></i>导航二</el-menu-item>
            <el-menu-item index="3"><i class="el-icon-setting"></i>导航三</el-menu-item>
          </el-menu>
        </div>
      </el-col>
    </el-row>
      <!--<el-col :xs="20" :sm="20" :md="20" :lg="20">-->
        <!--<div>-->
          <!--<div style="border: 1px solid #A6A6A6; border-radius:6px; padding:5px; margin:2px; background-color: white">-->
            <!--<el-breadcrumb separator="/">-->
              <!--<el-breadcrumb-item v-for="item in breadcrumbItems">{{item}}</el-breadcrumb-item>-->
            <!--</el-breadcrumb>-->
          <!--</div>-->
        <!--</div>-->
      <!--</el-col>-->
  </div>
</template>

<script>
export default {
  name: 'sidebar',
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style scoped>
  #sidebar ,.tac{
    margin-left: 10px;
    border: #ffffff;
    color: #3edaca;
    line-height: 400px;
  }
</style>
