<template>
  <div id="home">
    <Header></Header>
    <div class="container">
      <div class="row">
        <div class="main">
          <!-- Banner -->
          <div class="banner">
            <el-carousel height="272px" indicator-position="none" :interval="2000">
              <el-carousel-item v-for="banner,key in banner_list" :key="key">
                <a :href="banner.link" v-if="banner.is_http" target="_blank"><img :src="banner.image"></a>
                <router-link :to="banner.link" v-else><img :src="banner.image"></router-link>
              </el-carousel-item>
            </el-carousel>
          </div>
          <div id="list-container">
            <!-- 文章列表模块 -->
            <ul class="note-list">
              <li :class="{'have-img':check_has_img(article.html_content)}" v-for="article in article_list">
                <router-link class="wrap-img" :to="`/article/${article.id}`" v-if="check_has_img(article.html_content)">
                  <img class="img-blur-done" :src="check_has_img(article.html_content)"/>
                </router-link>
                <div class="content">
                  <router-link class="title" :to="`/article/${article.id}`">{{article.name}}</router-link>
                  <p class="abstract">{{article.html_content|trip_html}}...</p>
                  <div class="meta">
                    <span class="jsd-meta" v-if="article.user.money"><img src="/static/image/paid1.svg" alt=""> 4.8</span>
                    <router-link class="nickname" :to="`/user/${article.user.id}`">{{article.user.nickname}}</router-link>
                    <a target="_blank" href="" v-if="article.comment_count>0">
                      <img src="/static/image/comment.svg" alt="">{{article.comment_count}}
                    </a>
                    <span v-if="article.like_count>0"><img src="/static/image/like.svg" alt=""> {{article.like_count}}</span>
                    <span v-if="article.reward_count>0"><img src="/static/image/shang.svg" alt=""> {{article.reward_count}}</span>
                  </div>
                </div>
              </li>
            </ul>
            <!-- 文章列表模块 -->
          </div>
          <a href="" v-if="!none_data" @click.stop.prevent="get_article" class="load-more">阅读更多</a>
        </div>
        <div class="aside">
          <!-- 推荐作者 -->
          <div class="recommended-author-wrap">
            <!---->
            <div class="recommended-authors">
              <div class="title">
                <span>推荐作者</span>
                <a class="page-change"><img class="icon-change" src="/static/image/exchange-rate.svg" alt="">换一批</a>
              </div>
              <ul class="list">
                <li>
                  <a href="" target="_blank" class="avatar">
                    <img src="/static/image/avatar.webp" />
                  </a>
                  <a class="follow" state="0"><img src="/static/image/follow.svg" alt="" />关注</a>
                  <a href="" target="_blank" class="name">董克平日记</a>
                  <p>写了807.1k字 · 2.5k喜欢</p>
                </li>
                <li>
                  <a href="" target="_blank" class="avatar">
                    <img src="/static/image/avatar.webp" />
                  </a>
                  <a class="follow" state="0"><img src="/static/image/follow.svg" alt="" />关注</a>
                  <a href="" target="_blank" class="name">董克平日记</a>
                  <p>写了807.1k字 · 2.5k喜欢</p>
                </li>

              </ul>
              <a href="" target="_blank" class="find-more">查看全部 ></a>
              <!---->
            </div>
          </div>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>
<script>
  import Header from "./common/Header";
  import Footer from "./common/Footer";
  export default {
      name:"Home",
      data(){
          return {
            banner_list:[],
            article_list:[],  // 文章列表
            is_request:false, // ajax请求状态，false表示没有进行ajax，true表示正在请求中
            page:0,           // 默认页码
            none_data: false,  // 是否到结束位置
          }
      },
      components:{
        Header,
        Footer,
      },
      created(){
          this.token = sessionStorage.user_token || localStorage.user_token;
          this.get_banner();
          this.get_article();
      },
      filters:{
          trip_html(data){
            let div = document.createElement("div");
            div.innerHTML = data;
            return div.innerText;
          }
      },
      methods:{
          check_has_img(data){
              if(/<img.*?>/.test(data)){
                  console.log(/<img.*?src="(.*?)".*?>/.exec(data)[1]);
                  return /<img.*?src="(.*?)".*?>/.exec(data)[1];
              }else{
                  return false;
              }
          },
          get_banner(){
              this.$axios.get(`${this.$settings.Host}/banner/`).then(response=>{
                  this.banner_list = response.data;
              }).catch(error=>{
                  this.$message.error("网络异常！获取轮播图失败！");
              })
          },
          get_article(){
              console.log(this.is_request);
              if( this.is_request ){
                  return ;
              }
              this.is_request=true;
              // 获取推送文章
              let headers={};
              if(this.token){
                  headers = {
                      Authorization:"jwt " + this.token,
                  }
              }
              let params={};
              if(this.page>0){
                  params={
                      page: this.page,
                  }
              }
              this.$axios.get(`${this.$settings.Host}/article/`,{
                  params,
                  headers,
              }).then(response=>{
                  // 合并数组
                  this.article_list = this.article_list.concat(response.data.results);
                  this.is_request=false;
                  if(response.data.next && response.data.next.length>0){
                      // 存在分页
                      if(/page=(\d+)/.test(response.data.next)){
                          let page = /page=(\d+)/.exec(response.data.next)[1];
                          if( (parseInt(this.page)+1) * response.data.results.length < response.data.count ){
                              this.page = page;
                          }else{
                              this.none_data = true;
                          }
                      }
                  }
              }).catch(error=>{
                  this.$message.error("网络异常无法获取推送内容！");
              });
          }
      }
  }
</script>

<style scoped>
.banner img{
  max-height: 100%;
  max-width: 100%;
}
.container{
    width: 960px;
    margin-right: auto;
    margin-left: auto;
    padding-left: 15px;
    padding-right: 15px;
    box-sizing: border-box;
}
.container:after, .container:before {
    content: " ";
    display: table;
}
.row {
    margin-left: -15px;
    margin-right: -15px;
}
.row:after, .row:before {
    content: " ";
    display: table;
}
.main {
    padding-top: 30px;
    padding-right: 0;
    position: relative;
    min-height: 1px;
    padding-left: 15px;
    width: 66.66667%;
    float: left;
    box-sizing: border-box;
}
.main .banner{
    width: 640px;
    height: 272px;
}
.note-list {
    margin: 0;
    padding: 0;
    list-style: none;
}
.note-list li {
    position: relative;
    width: 100%;
    margin: 0 0 15px;
    padding: 15px 2px 20px 0;
    border-bottom: 1px solid #f0f0f0;
    word-wrap: break-word;
    line-height: 20px;
}
.note-list li.have-img {
    min-height: 140px;
}
.note-list .have-img .wrap-img {
    position: absolute;
    top: 50%;
    margin-top: -60px;
    right: 0;
    width: 150px;
    height: 100px;
}
.note-list .have-img .wrap-img img {
    width: 100%;
    height: 100%;
    border-radius: 4px;
    border: 1px solid #f0f0f0;
    vertical-align: middle;
}
.main .note-list .have-img .content {
    padding-right: 165px;
    box-sizing: border-box;
}
.note-list .title {
    margin: -7px 0 4px;
    display: inherit;
    font-size: 18px;
    font-weight: 700;
    line-height: 1.5;
    color: #333;
}
.note-list .title:hover{
    text-decoration: underline;
}
.note-list .abstract {
    margin: 0 0 8px;
    font-size: 13px;
    line-height: 24px;
    color: #999;
}
.note-list .meta {
    padding-right: 0!important;
    font-size: 12px;
    font-weight: 400;
    line-height: 20px;
}
.note-list .meta span {
    margin-right: 10px;
    color: #b4b4b4;
}

.jsd-meta {
    color: #ea6f5a!important;
}
.note-list .meta a, .note-list .meta a:hover {
    transition: .1s ease-in;
}
.note-list .meta a {
    margin-right: 10px;
    color: #b4b4b4;
}
.note-list .meta img{
    width: 15px;
    vertical-align: middle;
}

.main .load-more {
    width: 100%;
    border-radius: 20px;
    background-color: #a5a5a5;
    margin: 30px auto 60px;
    padding: 10px 15px;
    text-align: center;
    font-size: 15px;
    color: #fff;
    display: block;
    line-height: 1.42857;
    box-sizing: border-box;
}
.main .load-more:hover {
    background-color: #9b9b9b;
}
.aside {
    padding: 30px 0 0;
    margin-left: 4.16667%;
    width: 29.16667%;
    float: left;
    position: relative;
    min-height: 1px;
    box-sizing: border-box;
}
.recommended-authors {
    margin-bottom: 20px;
    padding-top: 0;
    font-size: 13px;
    text-align: center;
}
.recommended-authors .title {
    text-align: left;
}
.recommended-authors .title span {
    font-size: 14px;
    color: #969696;
}
.recommended-authors .title .page-change {
    float: right;
    display: inline-block;
    font-size: 16px;
    color: #969696;
}
.icon-change{
    width: 16px;
    vertical-align: middle;
}
.recommended-authors .list {
    margin: 0 0 20px;
    text-align: left;
    list-style: none;
}
.recommended-authors .list li {
    margin-top: 15px;
    line-height: 20px;
}
.recommended-authors .list .avatar {
    float: left;
    width: 48px;
    height: 48px;
    margin-right: 10px;
}

.avatar {
    width: 24px;
    height: 24px;
    display: block;
    cursor: pointer;
}
.avatar img {
    width: 100%;
    height: 100%;
    border: 1px solid #ddd;
    border-radius: 50%;
}
.follow{
    font-size: 14px;
    color: #42c02e;
    border-color: #42c02e;
    font-weight: 400;
    line-height: normal;
}
.follow img{
    width: 14px;
}
.recommended-authors .list .follow, .recommended-authors .list .follow-cancel, .recommended-authors .list .follow-each, .recommended-authors .list .following {
    float: right;
    margin-top: 5px;
    padding: 0;
    font-size: 13px;
    color: #42c02e;
    box-sizing: border-box;
}
.recommended-authors .list .name {
    padding-top: 5px;
    margin-right: 60px;
    font-size: 14px;
    display: block;
    box-sizing: border-box;
}
.recommended-authors .list p {
    font-size: 12px;
    color: #969696;
    margin: 0 0 10px;
    box-sizing: border-box;
}
.recommended-authors .find-more {
    position: absolute;
    padding: 7px 7px 7px 12px;
    left: 0;
    width: 100%;
    font-size: 13px;
    color: #787878;
    background-color: #f7f7f7;
    border: 1px solid #dcdcdc;
    border-radius: 4px;
}
.row:after {
    clear: both;
}
.el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
}
</style>
