<template>
<footer class="container">
  <div class="row">
    <div class="main">
      <a target="_blank" href="">关于荏苒</a>
      <em> · </em>
      <a target="_blank" href="">联系我们</a>
      <em> · </em>
      <a target="_blank" href="">加入我们</a>
      <em> · </em>
      <a target="_blank" href="">帮助中心</a>
      <em> · </em>
      <a target="_blank" href="http://www.jianshu.com/p/cabc8fa39830">合作伙伴</a>
      <div class="icp">©2016-2019 广州荏苒信息科技有限公司 / 荏苒 / 粤ICP备16018329号-5 /</div>
    </div>
  </div>
</footer>
</template>

<script>
    export default {
        name: "Footer"
    }
</script>

<style scoped>
.container {
    width: 960px;
    margin-right: auto;
    margin-left: auto;
    padding-left: 15px;
    padding-right: 15px;
    margin-bottom: 20px;
    box-sizing: border-box;
}
.container:after, .container:before {
    content: " ";
    display: table;
}
footer .row {
    padding-top: 25px;
    box-sizing: border-box;
    margin-left: -15px;
    margin-right: -15px;
}
footer .main {
    padding-right: 0;
    font-size: 13px;
    color: #969696;
  width: 70.83333%;
}
footer .icp, footer .icp a {
    color: #c8c8c8;
}
footer .icp {
    margin-top: 10px;
    font-size: 12px;
}
footer .main a {
    color: #969696;
    display: inline-block;
}
.row:after {
    clear: both;
}
</style>
