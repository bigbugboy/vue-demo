<template>
  <div>
    <!-- 头部 -->
    <div class="header">折叠</div>
    
    <!-- 内容 -->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
    name: "Content",

}
</script>

<style scoped>
.header{
  height: 50px;
  background-color: skyblue;
  color: red;
  line-height: 50px;
}

</style>