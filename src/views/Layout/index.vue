<template>
  <div>
    <!-- 左侧导航菜单 -->
    <div class="menu">
      <Menu></Menu>
    </div>
    <!-- 右侧内容区 -->
    <div class="content">
      <Content></Content>
    </div>


  </div>
</template>

<script>
import Menu from "./Menu.vue"
import Content from "./Content.vue"

export default {
  name: "Layout",
  components: { Menu, Content },


}
</script>

<style scoped>
.menu{
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  width: 200px;
  background-color: #545c64;
}

.content{
  padding-left: 200px;
}

</style>