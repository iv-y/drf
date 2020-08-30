<template>
  <div class="home">
    <!--
      <img alt="Vue logo" src="../assets/logo.png" />
      <HelloWorld msg="Welcome to Your Vue.js App" />
    -->
    <h2>DRF Vue simple board</h2>
    <BoardList />
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";
import BoardList from "@/components/BoardList.vue";

export default {
  name: "Home",
  components: {
    BoardList
  }
};
</script>
