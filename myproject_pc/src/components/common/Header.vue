<template>
  <div class="header">
    <nav class="navbar">
      <div class="width-limit">
        <!-- 左上方 Logo -->
        <a class="logo" href="/"><img src="/static/image/nav-logo.png" /></a>
        <!-- 右上角 -->
        <!-- 未登录显示登录/注册/写文章 -->
        <router-link class="btn write-btn" to="/writer"><img class="icon-write" src="/static/image/write.svg">写文章</router-link>
        <router-link class="btn sign-up" id="sign_up" to="/register">注册</router-link>
        <router-link class="btn log-in" id="sign_in" to="/login">登录</router-link>
        <div class="container">
          <div class="collapse navbar-collapse" id="menu">
            <ul class="nav navbar-nav">
              <li class="tab active">
                <a href="/">
                  <i class="iconfont ic-navigation-discover menu-icon"></i>
                  <span class="menu-text">首页</span>
                </a>
              </li>
              <li class="tab" v-for="nav in nav_list">
                <a :href="nav.link" v-if="nav.is_http">
                  <i class="iconfont ic-navigation-follow menu-icon"></i>
                  <span class="menu-text">{{nav.name}}</span>
                </a>
                <router-link :to="nav.link" v-else>
                  <i class="iconfont ic-navigation-follow menu-icon"></i>
                  <span class="menu-text">{{nav.name}}</span>
                </router-link>
                <ul class="dropdown-menu" v-if="nav.son_list.length>0">
                  <li v-for="son in nav.son_list">
                    <a :href="son.link" v-if="son.is_http" target="_blank"><i class="iconfont ic-comments"></i> <span>{{son.name}}</span></a>
                    <router-link :to="son.link" v-else><i class="iconfont ic-comments"></i> <span>{{son.name}}</span></router-link>
                  </li>
                </ul>
              </li>
              <li class="search">
                <form target="_blank" action="/search" accept-charset="UTF-8" method="get">
                  <input type="text" name="q" id="q" value="" autocomplete="off" placeholder="搜索" class="search-input">
                  <a class="search-btn" href="javascript:void(0)"></a>
                </form>
              </li>
            </ul>
          </div>
        </div>

        <!-- 如果用户登录，显示下拉菜单 -->
      </div>
    </nav>
  </div>
</template>

<script>
    export default {
        name: "Header",
        data(){
            return {
                nav_list:[
                    {
                        link:"",
                        son_list:[]
                    }
                ],
            }
        },
        created(){
            this.get_nav();
        },
        methods:{
            get_nav(){
                this.$axios.get(`${this.$settings.Host}/nav/header/`).then(response=>{
                    this.nav_list = response.data;
                }).catch(error=>{
                    this.$message.error("网络异常，无法获取头部导航信息！");
                })
            }
        }
    }
</script>

<style scoped>
.header{
  height: 56px;
}
.container {
    width: 960px;
    margin-right: auto;
    margin-left: auto;
    padding-left: 15px;
    padding-right: 15px;
}
.container:after, .container:before {
    content: " ";
    display: table;
}
.container:after {
    clear: both;
}
.navbar {
    background-color: #fff;
    border-color: #f0f0f0;
    top: 0;
    border-width: 0 0 1px;
    border-radius: 0;
}
.navbar-nav {
    float: left;
    margin: 0;
}
.navbar:after, .navbar:before {
    content: " ";
    display: table;
    box-sizing: border-box;
}
.nav:after, .nav:before {
    content: " ";
    display: table;
}
nav .width-limit {
    min-width: 768px;
    max-width: 1440px;
    margin: 0 auto;
}
nav .logo {
    float: left;
    height: 56px;
    padding: 0;
}
nav .logo img {
    height: 100%;
    vertical-align: middle;
    border: 0;
}
.btn {
    display: inline-block;
    margin-bottom: 0;
    font-weight: 400;
    text-align: center;
    vertical-align: middle;
    touch-action: manipulation;
    cursor: pointer;
    background-image: none;
    border: 1px solid transparent;
    white-space: nowrap;
    padding: 6px 12px;
    font-size: 14px;
    line-height: 1.42857;
    border-radius: 4px;
}
nav .write-btn {
    float: right;
    width: 100px;
    height: 24px;
    line-height: 24px;
    margin: 8px 12px 0;
    border-radius: 20px;
    font-size: 15px;
    color: #fff;
    background-color: #ea6f5a;
    text-decoration: none;
}
nav .log-in, nav .log-in:hover {
    color: #969696;
}
nav .log-in {
    float: right;
    margin: 11px 6px 0 10px;
    font-size: 15px;
}
nav .sign-up {
    float: right;
    width: 80px;
    height: 24px;
    line-height: 24px;
    margin: 9px 5px 0 15px;
    border: 1px solid rgba(236,97,73,.7);
    border-radius: 20px;
    font-size: 15px;
    color: #ea6f5a;
    background-color: transparent;
}
nav .icon-write {
    margin-right: 3px;
    width: 19px;
    height: 19px;
    vertical-align: middle;
}
nav .menu-text{
    font-size: 17px;
}
nav .active a{
  color: #ea6f5a;
}
nav .menu-icon {
    width: 20px;
    height: 20px;
    vertical-align: baseline;
    margin-right: 3px;
}
.tab:hover .dropdown-menu{
  display: block;
}
.dropdown-menu{position:absolute;top:100%;left:0;z-index:1000;display:none;
  float:left;min-width:120px;padding:5px 0;margin:2px 0 0;list-style:none;
  font-size:14px;text-align:left;background-color:#fff;border:1px solid #ccc;
  border:1px solid rgba(0,0,0,.15);border-radius:4px;
  box-shadow:0 6px 12px rgba(0,0,0,.175);
  background-clip:padding-box}
.dropdown-menu.pull-right{right:0;left:auto}
.dropdown-menu .divider{
  height:1px;margin:9px 0;overflow:hidden;background-color:#e5e5e5}
.dropdown-menu>li>a{display:block;padding:3px 20px;clear:both;font-weight:400;
  line-height:1.42857;color:#333;white-space:nowrap}
.dropdown-menu>li>a:focus,.dropdown-menu>li>a:hover{
  text-decoration:none;color:#262626;background-color:#f5f5f5}
.dropdown-menu>.active>a,.dropdown-menu>.active>a:focus,.dropdown-menu>.active>a:hover{
  color:#fff;text-decoration:none;outline:0;background-color:#337ab7}
.dropdown-menu>.disabled>a,.dropdown-menu>.disabled>a:focus,.dropdown-menu>.disabled>a:hover{
  color:#777
}
.dropdown-menu>.disabled>a:focus,.dropdown-menu>.disabled>a:hover{
  text-decoration:none;background-color:transparent;background-image:none;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false);cursor:not-allowed}
.open>.dropdown-menu{display:block}.open>a{outline:0}.dropdown-menu-right{left:auto;right:0}.dropdown-menu-left{left:0;right:auto}.dropdown-header{display:block;padding:3px 20px;font-size:12px;line-height:1.42857;color:#777;white-space:nowrap}.dropdown-backdrop{position:fixed;left:0;right:0;bottom:0;top:0;z-index:990}.pull-right>.dropdown-menu{right:0;left:auto}.dropup .caret,.navbar-fixed-bottom .dropdown .caret{border-top:0;border-bottom:4px dashed;border-bottom:4px solid\9;content:""}.dropup .dropdown-menu,.navbar-fixed-bottom .dropdown .dropdown-menu{top:auto;bottom:100%;margin-bottom:2px}
.navbar-right .dropdown-menu-left{left:0;right:auto}
.dropdown-menu{
  width:150px;margin-top:-1px;border-radius:0 0 4px 4px
}
.dropdown-menu li{margin:0}
.dropdown-menu a{height:auto;padding:10px 20px;line-height:30px}
.dropdown-menu a:hover{background-color:#f5f5f5}
.dropdown-menu i{margin-right:15px;font-size:22px;color:#ea6f5a;
  vertical-align:middle
}
.dropdown-menu span{vertical-align:middle}
.dropdown-menu .badge{position:absolute;right:15px;margin-top:7px}

nav .nav .tab a {
    height: 56px;
    line-height: 26px;
    padding: 15px;
    background: none;
}
nav .navbar-nav li {
    margin-right: 10px;
    float: left;
    position: relative;
    display: block;
    box-sizing: border-box;
    height: 56px;
    line-height: 56px;
}
.navbar-nav {
    float: left;
    margin: 0;
}
nav form {
    position: relative;
    top: 9px;
    margin: 0 0 20px;
    box-sizing: border-box;
    line-height: 20px;
}
nav form .search-input {
    padding: 0 40px 0 20px;
    height: 38px;
    font-size: 14px;
    border: 1px solid #eee;
    border-radius: 40px;
    background: #eee;
    transition: width .5s;
    width: 240px;
    outline: none;
}
nav form .search-input:focus {
    width: 320px;
    outline: none;
}
.navbar-default .navbar-collapse, .navbar-default .navbar-form {
    border-color: #e7e7e7;
    padding-left: 0;
    padding-right: 0;
    box-sizing: border-box;
    width: auto;
    border-top: 0;
    box-shadow: none;
}
.navbar {
    background-color: #fff;
    top: 0;
    border-radius: 0;
    position: fixed;
    right: 0;
    left: 0;
    z-index: 1030;
    min-height: 50px;
    margin-bottom: 20px;
    border-bottom: 1px solid #f0f0f0;
}
nav {
    height: 56px;
}
.navbar:after, .navbar:before {
    content: " ";
    display: table;
}
nav form .search-btn {
    position: absolute;
    display: block;
    top: 0;
    right: 10px;
    width: 30px;
    height: 30px;
    padding: 0;
    margin: 5px -1px 0 0;
    background: transparent url("../../../static/image/search-focus.svg") no-repeat 6px 6px;
    background-size: 20px;
}
nav form .search-input:focus~a{
    border-radius: 50%;
    background-color: #696969;
    background-image: url("../../../static/image/search-blur.svg");
}
nav .sign-up:hover {
    color: #ec6149;
    border-color: #ec6149;
    background-color: rgba(236,97,73,.05);
}
nav .write-btn:focus, nav .write-btn:hover {
    color: #fff;
    background-color: #ec6149;
}
</style>
