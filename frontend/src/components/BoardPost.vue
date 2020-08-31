<template>
  <div id="boardpost">
    <h3>#{{boardPost.id}} "{{boardPost.title}}"</h3>
    <h4>By {{boardPost.author_str}}</h4>
    <div>
      {{ boardPost.content }}
    </div>
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
    ...mapState(["boardPost"])
  },

  methods: {
    ...mapActions(["boardGetDetail"])
  },

  created () {
    this.boardGetDetail(this.pk);
  }
}
</script>