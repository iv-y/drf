<template>
  <div class="post">
    <BoardPost v-bind:pk="pk" />
  </div>
</template>

<script>
import { mapState } from "vuex";
import BoardPost from "@/components/BoardPost.vue";

export default {
  props: [
    "pk"
  ],
  computed: {
    ...mapState(["isLogin", "userInfo", "boardPost"])
  },

  components: {
    BoardPost
  }
}
</script>
