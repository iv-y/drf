<template>
  <div class="formContainer">
    <a class="bold">&nbsp;&nbsp;Signup</a>
    <form class="login-box">
      <p>ID</p>
      <input type="text" v-model="username" name="username" label="Input ID" />
      <p>e-mail</p>
      <input type="text" v-model="email" name="email" label="Input e-mail" />
      <p>password</p>
      <input type="password" v-model="password1" name="userpassword1" label="Input Password" />
      <p>password check</p>
      <input type="password" v-model="password2" name="userpassword2" label="Password Check" />
      <br />
    </form>

    <div class="login-btn">
      <input 
        type="submit"
        class="button"
        name="submit"
        @click="signup({username, email, password1, password2})"
        value="Signup!"
      />
    </div>
  </div>
</template>


<script>
import { mapActions } from "vuex";

export default {
  data() {
    return {
      username: null,
      email: null,
      password1: null,
      password2: null
    };
  },
  methods: {
    ...mapActions(["signup"])
  }
}
</script>