<template>
  <div class="about">
    <h1>This is an about page</h1>
    <span v-if="isLogin"> {{userInfo.username}} </span>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  
  computed: {
    ...mapState(["isLogin", "userInfo"])
  }

}
</script>
