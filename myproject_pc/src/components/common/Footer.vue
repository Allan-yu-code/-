<template>
<footer class="container">
  <div class="row">
    <div class="main">
      <span :key="key" v-for="nav,key in nav_list">
        <a :href="nav.link" target="_blank"  v-if="nav.is_http">{{nav.name}}</a>
        <router-link :to="nav.link" v-else>{{nav.name}}</router-link>
        <em> · </em>
      </span>
      <div class="icp"></div>
    </div>
  </div>
</footer>
</template>

<script>
    export default {
        name: "Footer",
        data(){
            return {
                nav_list:[],
            }
        },
        created(){
            this.get_nav();
        },
        methods:{
            get_nav(){
                this.$axios.get(`${this.$settings.Host}/nav/footer/`).then(response=>{
                    this.nav_list = response.data;
                }).catch(error=>{
                    this.$message.error("无法获取脚步导航信息");
                })
            }
        }
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
