<template>
  <div id="boardpost">
    <h3>#{{boardPost.id}} "{{boardPost.title}}"</h3>
    <h4>By {{boardPost.author_str}}</h4>
    <div>
      {{ boardPost.content }}
    </div>
    <h4>Replies</h4>
    <sui-container>
      <sui-container v-for="reply in boardReplies" v-bind:key="reply.id">
        #{{boardPost.id}}>{{reply.reply_order}}
        By {{reply.author_str}}
        "{{reply.content}}"
        ++{{reply.liked_user_count}}
      </sui-container>
    </sui-container>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: "BoardList",
  props: [
    'pk'
  ],

  computed: {
    ...mapState(["boardPost", "boardReplies"])
  },

  methods: {
    ...mapActions(["boardGetDetail"])
  },

  created () {
    this.boardGetDetail(this.pk);
  }
}
</script>