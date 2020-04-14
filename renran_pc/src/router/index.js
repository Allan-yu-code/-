import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home"
import Login from "../components/Login"
import Register from "../components/Register"
import QQCallBack from "../components/QQCallBack"
import Writer from "../components/Writer"
Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: '/',
      name: "Home",
      component: Home,
    },{
      path: '/login',
      name: "Login",
      component: Login,
    },{
      path: '/register',
      name: "Register",
      component: Register,
    },{
      path: '/oauth_callback.html',
      name: "QQCallBack",
      component: QQCallBack,
    },{
      path: '/writer',
      name: "Writer",
      component: Writer,
    },
  ]
})
