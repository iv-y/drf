<template>
  <div id="boardlist">
    <div id="boardlist-refresh-btn">
      <input 
        type="submit"
        class="button"
        name="submit"
        @click="boardRefresh()"
        value="Refresh Posts"
      />
    </div>
    <div v-for="post in boardPosts" v-bind:key="post.id">
      <h4>
        #{{post.id}} 
        "<a v-bind:href="'/post/'.concat(post.id.toString())">{{post.title}}</a>"
        by {{post.author_str}}
        ++{{post.liked_user_count}}
      </h4>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: "BoardList",
  props: {
  },

  computed: {
    ...mapState(["boardPosts"])
  },

  methods: {
    ...mapActions(["boardRefresh"])
  },

  created () {
    this.boardRefresh();
  }
}
</script>