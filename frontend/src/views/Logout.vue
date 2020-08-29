<template>
  <div class="formContainer">

    <div class="logout-btn" v-if="isLogin">
      <input 
        type="submit"
        class="button"
        name="submit"
        @click="logout()"
        value="Logout!"
      />
    </div>
    <div v-else>
      You must log in to log out.
    </div>

  </div>

</template>


<script>
import { mapState, mapActions } from "vuex";

export default {

  computed: {
    ...mapState(["isLogin", "isLoginError"])
  },

  methods: {
    ...mapActions(["logout"])
  }
}
</script>