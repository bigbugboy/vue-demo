<template>
  <el-menu default-active="/" class="el-menu-vertical-demo" background-color="#545c64" text-color="#fff" router
    active-text-color="#ffd04b">
    <el-menu-item index="/">
      <i class="el-icon-menu"></i>
      <span slot="title">首页</span>
    </el-menu-item>
    <el-menu-item index="/news">
      <i class="el-icon-menu"></i>
      <span slot="title">新闻</span>
    </el-menu-item>
    <el-menu-item index="3" disabled>
      <i class="el-icon-document"></i>
      <span slot="title">账号</span>
    </el-menu-item>
    <el-menu-item index="4">
      <i class="el-icon-setting"></i>
      <span slot="title">案例</span>
    </el-menu-item>
  </el-menu>
</template>

<script>
export default {
  name: "Menu",
  data() {
    return {

    }
  },
  // methods: {
  //   handleSelect(key, keyPath) {
  //     this.$router.push({name: key})
  //   }
  // },

}
</script>

<style scoped>
.el-menu-vertical-demo {
  width: 200px;
  min-height: 400px;
}
.el-menu{
  border-right: none;
}
</style>