// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false

// 引入自定义配置对象作为组件vm对象的属性
import settings from "./settings"
Vue.prototype.$settings = settings;

// 引入全局初始化样式表
import "../static/css/reset.css";

// elementUI 导入
import ElementUI from 'element-ui';
import "element-ui/lib/theme-chalk/index.css";
// 调用插件
Vue.use(ElementUI);

// 导入腾讯防水墙验证码
import "../static/js/TCaptcha";


import axios from 'axios'; // 从node_modules目录中导入包
// 允许ajax发送请求时附带cookie，设置为不允许
axios.defaults.withCredentials = false;
Vue.prototype.$axios = axios; // 把axios对象挂载组件vm对象中

// 引入网站的图标样式
import "../static/css/iconfont.css";

// 注册mavon-editor组件
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
Vue.use(mavonEditor);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
// new Vue后面不要写任何的代码，不管用，系统不识别！！！！
