<template>
  <div class="header">
    <nav class="navbar">
      <div class="width-limit">
        <!-- 左上方 Logo -->
        <a class="logo" href="/"><img src="/static/image/nav-logo.png" /></a>
        <!-- 右上角 -->
        <!-- 未登录显示登录/注册/写文章 -->
        <a class="btn write-btn" target="_blank" href="/writer"><img class="icon-write" src="/static/image/write.svg">写文章</a>
        <a class="btn sign-up" id="sign_up" href="/register">注册</a>
        <a class="btn log-in" id="sign_in" href="/login">登录</a>
        <div class="container">
          <div class="collapse navbar-collapse" id="menu">
            <ul class="nav navbar-nav">
              <li class="tab active">
                <a href="/">
                  <img class="menu-icon" src="/static/image/menu.svg">
                  <span class="menu-text">首页</span>
                </a>
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
        name: "Header"
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
    color: #ea6f5a;
}
nav .menu-icon {
    width: 20px;
    height: 20px;
    vertical-align: sub;
    margin-right: 3px;
}
nav .nav .tab a {
    height: 56px;
    line-height: 26px;
    padding: 15px;
    color: #ea6f5a;
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
