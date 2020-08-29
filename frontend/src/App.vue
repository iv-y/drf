<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <span v-if="isLogin">
        <span>{{userInfo.username}}</span> |
        <router-link to="/logout">Logout</router-link>
      </span>
      <span v-else>
        <router-link to="/login">Login</router-link> |
        <router-link to="/signup">Signup</router-link>
      </span>
    </div>
    <router-view />
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  
  computed: {
    ...mapState(["isLogin", "userInfo"])
  }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
