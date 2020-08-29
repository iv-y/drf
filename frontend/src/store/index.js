import Vue from "vue";
import Vuex from "vuex";

import router from "../router";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({

  state: {
    userInfo: null,
    isLogin: false,
    isLoginError: false
  },

  mutations: {
    loginSuccess(state, payload) {
      state.isLogin = true;
      state.isLoginError = false;
      state.userInfo = payload;
    },
    loginError(state) {
      state.isLogin = false;
      state.isLoginError = false;
      state.userInfo = null;
    },
    logout(state){
      state.isLogin = false;
      state.isLoginError = false;
      state.userInfo = null;
    }
  },

  actions: {
    login(dispatch, loginObj) {
      // login --> return the token
      // loginObj : get {email, password}
      axios
        .post("http://ssal.sparcs.org:57570/api/rest-auth/login/", loginObj)
        .then(res => {
          // a sucessful access gives id and token
          let token = res.data.token;
          // save the token at the local storage
          localStorage.setItem("access_token", token);
          this.dispatch("getMemberInfo");
          router.push({name: "Home"});
          // DEBUG!!!
          // console.log(res);
        })
        .catch( () => {
          alert("Check your e-mail and password.");
        });
    },

    logout({commit}) {
      commit("logout");
      router.push({name: "Home"});
    },

    signup(dispatch, loginObj) {
      // login --> return the token
      axios
        .post("http://ssal.sparcs.org:57570/api/rest-auth/registration/", loginObj)
        .then( () => {
          alert("Sign up complete.");
          router.push({name: "Login"});
          // DEBUG!!!
          // console.log(res);
        })
        .catch( () => {
          alert("Check your e-mail and password.");
        });
    },

    getMemberInfo({commit}) {
      let token = localStorage.getItem("access_token");
      let config = {
        headers: {
          // https://stackoverflow.com/a/33737293
          "Authorization": "JWT ".concat(token)
        }
      };
      // token --> get member data
      // refresh(F5) --> get member data with only the token
      axios
        .get("http://ssal.sparcs.org:57570/api/userself/", config)
        .then(response => {
          let userInfo = {
            pk: response.data.id,
            username: response.data.username,
            email: response.data.email,
          };
          commit("loginSuccess", userInfo);
        })
        .catch( () => {
          alert("Check your e-mail and password.");
        });
    }
  },

  modules: {}

});