<template>
  <div class="formContainer">

    <form class="login-box">
      <p>ID</p>
      <input type="text" v-model="username" name="username" label="Input ID" />
      <p>PW</p>
      <input type="password" v-model="password" name="userpassword" label="Input Password" />
      <br />
    </form>

    <div class="login-btn">
      <input 
        type="submit"
        class="button"
        name="submit"
        @click="login({username, password})"
        value="Login!"
      />

      <div class="login-btn-txt">
        <a>Find ID/PW |</a>
        <a class="bold">
          <router-link to="/signup"> &nbsp;&nbsp;Sign up</router-link>
        </a>
      </div>

    </div>

  </div>

</template>


<script>
import { mapState, mapActions } from "vuex";

export default {

  data() {
    return {
      username: null,
      password: null
    };
  },

  computed: {
    ...mapState(["isLogin", "isLoginError"])
  },

  methods: {
    ...mapActions(["login"])
  }
}
</script>