<template>
  <div id="app">
    <sui-menu id="nav">
      <sui-menu-item 
        v-for="menu in processMenus( menus, isLogin, userInfo )" 
        v-bind:key="menu.id"
      >
        <router-link v-if="menu.link" v-bind:to="menu.link">{{menu.text}}</router-link>
        <span v-else>{{menu.text}}</span>
      </sui-menu-item>
    </sui-menu>
    <router-view />
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  data() {
    return {
      menus: [
        {
          "id": 0,
          "link": "/",
          "text": "Home",
          "activity": "always"
        },
        {
          "id": 1,
          "link": null,
          "text": "",
          "activity": "auth"
        },
        {
          "id": 2,
          "link": "/logout",
          "text": "Logout",
          "activity": "auth"
        },
        {
          "id": 3,
          "link": "/login",
          "text": "Login",
          "activity": "anon"
        },
        {
          "id": 4,
          "link": "/signup",
          "text": "Signup",
          "activity": "anon"
        }
      ]
    }
  },

  computed: {
    ...mapState(["isLogin", "userInfo"]),
  },

  methods: {
    processMenus ( menus, isLogin, userInfo ) {
      return (
        menus
        .filter( function (menu) {
          switch (menu.activity) {
            case "auth":
              return isLogin;
            case "anon":
              return !isLogin;
            case "always":
              return true;
            default:
              return false;
          }
        })
        .map( function (menu) {
          if (menu.id == 1) {
            menu.text = userInfo.username;
            return menu;
          } else {
            return menu;
          }
        })
      );
    }
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


#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
