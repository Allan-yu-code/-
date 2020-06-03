<template>
    <div id="writed">
      <div class="_3PLTX">
        <div class="_2Mx1k">
          <div class="_3CoyQ">
            <router-link :to="`/article/${article_id}`" class="_2-ZiM">{{article_name}}</router-link>
            <br>
            <router-link :to="`/article/${article_id}`" class="_2ajaT">发布成功，点击查看文章</router-link>
          </div>
          <ul class="zelSB">
            <li class="_35P4c"><i class="fa fa-weibo"></i>微博</li>
            <li class="_1c1Eo"><i class="fa fa-wechat"></i>微信</li>
            <li class="_1HWk1"><i class="fa fa-link"></i>复制链接</li>
            <li class="_3FrjS _3Qjz6 _2_WAp _2po2r cRfUr" title="">
              <span class="">更多分享</span>
            </li>
          </ul>
        </div>
        <div class="_3Q2EW" @click="$router.back()">×</div>
        <div class="_1s967"></div>
        <div class="_2w_E5">
          <div class="_23R_O">
            <div class="_1WCUC">
              <i class="fa fa-search fa-2x"></i><input type="text" placeholder="搜索专题">
            </div>
            <div class="_3dZoJ">向专题投稿，让文章被更多人发现</div>
          </div>
          <div>
            <div class="_18jMg">
              <h3>我管理的专题<a href="">新建</a></h3>
              <ul class="_1hEmG">
                <li v-for="special,key in my_special_list">
                  <a v-if="special.status==-1" @click="post_article(my_special_list,key)">收录</a>
                  <a v-else>已收录</a>
                  <img alt="png" :src="special.image">
                  <span class="_1CN24" :title="special.name">{{special.name}}</span>
                </li>
              </ul>
            </div>
            <div class="_18jMg">
              <h3>最近投稿</h3>
              <ul class="_1hEmG">
                <li>
                  <a data-collection-id="83" data-post-text="投稿" data-posting-text="投稿中" data-posted-text="等待审核">投稿</a>
                  <img alt="png" src="https://upload.jianshu.io/collections/images/83/1.jpg">
                  <span class="_1CN24" title="摄影">摄影</span>
                </li>
              </ul>
            </div>
            <div class="_18jMg">
              <h3>推荐专题</h3>
              <div>
                <ul class="_1hEmG">
                  <li class="_3GDE6">
                    <img alt="png" src="https://upload.jianshu.io/collections/images/83/1.jpg">
                    <span class="_1CN24">摄影<em>154.8K篇文章，2575.1K人关注</em></span>
                    <a data-collection-id="83" data-post-text="投稿" data-posting-text="投稿中" data-posted-text="等待审核">投稿</a>
                  </li>
                  <li class="_3GDE6">
                    <img alt="png" src="https://upload.jianshu.io/collections/images/95/1.jpg">
                    <span class="_1CN24">故事<em>192.2K篇文章，1920.7K人关注</em></span>
                    <a data-collection-id="95" data-post-text="投稿" data-posting-text="投稿中" data-posted-text="等待审核">投稿</a>
                  </li>
                </ul>
                <div class="_27pBl">没有更多了 </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
    export default {
        name: "PostArticle",
        data(){
           return {
             token: "",
             my_special_list:[],
             article_id: 0,     // 文章ID
             article_name:"",   // 文章标题
           }
        },
        created() {
            this.token = this.$settings.check_user_login(this);
            // 从本地存储中提取当前文章的ID和标题
            this.article_id   = sessionStorage.current_article_id;
            this.article_name = sessionStorage.current_article_name;
            this.get_my_special_list();
        },
        methods:{
          get_my_special_list(){
            // 获取我管理的专题列表
            this.$axios.get(`${this.$settings.Host}/article/special/`,{
              params:{
                // 需要发送当前文章ID到后端，方便判断专题和文章之间的绑定关系
                article_id: this.article_id,
              },
              headers:{
                Authorization: "jwt " + this.token,
              }
            }).then(response=>{
              this.my_special_list = response.data;
            }).catch(error=>{
              this.$message.error("对不起，获取专题列表失败！");
            });
          },
          post_article(special_list,key){
              // 文章投稿
              let special_id = special_list[key].id;
              this.$axios.post(`${this.$settings.Host}/article/post/`,{
                  article_id: this.article_id,
                  special_id: special_id,
              },{
                  headers:{
                      Authorization: "jwt " + this.token,
                  }
              }).then(response=>{
                  // 更新收录状态
                  special_list[key].status=response.data.status;
                  this.$message.success(response.data.message);
              }).catch(error=>{
                  this.$message.error("投稿失败!");
              });
          },
        }
    }
</script>

<style scoped>
::selection {
  color: #fff;
  background: #1890ff;
}
.writed{
  width: 100%;
  height: 100%;
  max-width: 100vw;
  max-height: 100vh;
  color: rgba(0,0,0,.65);
  font-size: 14px;
  font-variant: tabular-nums;
  line-height: 1.5;
}
.writed *{
  box-sizing: border-box;
}
._3PLTX{
      position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: #fff;
    z-index: 1010;
    overflow-y: auto;
}
._3PLTX ._2Mx1k {
    background-color: #f2f2f2;
    padding-bottom: 110px;
}
._3PLTX ._2Mx1k ._3CoyQ {
    padding: 80px 0 40px;
    text-align: center;
}
._3PLTX ._2Mx1k ._3CoyQ ._2-ZiM {
    display: inline-block;
    height: 40px;
    font-size: 28px;
    font-weight: 500;
    color: #333;
    margin-bottom: 24px;
}
._3PLTX ._2Mx1k ._3CoyQ ._2ajaT {
    font-size: 16px;
    font-weight: 600;
    color: #42c02e;
}
._3PLTX ._2Mx1k ._3CoyQ ._2ajaT:before {
    content: "";
    display: inline-block;
    width: 18px;
    height: 10px;
    border: 3px solid #42c02e;
    border-width: 0 0 4px 4px;
    transform: rotate(-45deg);
    transition: 0s;
    position: relative;
    bottom: 4px;
    right: 8px;
}
._3PLTX ._2Mx1k .zelSB {
    text-align: center;
    color: #fff;
    font-size: 14px;
}
._3PLTX ._2Mx1k .zelSB>li {
    display: inline-block;
    width: 124px;
    line-height: 38px;
    border-radius: 100px;
    margin: 0 15px;
    cursor: pointer;
    padding: 0;
    text-align: center;
}
._3PLTX ._2Mx1k .zelSB li._35P4c {
    background-color: #e05244;
}
._3PLTX ._2Mx1k .zelSB>li i {
    margin-right: 5px;
}
._3PLTX ._2Mx1k .zelSB li._1c1Eo {
    background-color: #07b225;
}
._3PLTX ._2Mx1k .zelSB li._1HWk1 {
    background-color: #3194d0;
}
._2po2r {
    padding: 10px 20px;
    line-height: 20px;
    white-space: nowrap;
    text-align: left;
    position: relative;
    border-bottom: 1px solid #d9d9d9;
}
.cRfUr {
    border-bottom: 1px solid #d9d9d9;
}
._2po2r:last-child {
    border-radius: 0 0 4px 4px;
    border-bottom: 0;
}
._3PLTX ._2Mx1k .zelSB>li {
    display: inline-block;
    width: 124px;
    line-height: 38px;
    border-radius: 100px;
    margin: 0 15px;
    cursor: pointer;
    padding: 0;
    text-align: center;
}
._3PLTX ._2Mx1k .zelSB li._3Qjz6 {
    background-color: #a7a7a7;
    position: relative;
}
._3PLTX ._3Q2EW {
    position: fixed;
    top: 50px;
    right: 100px;
    font-size: 30px;
    font-weight: 700;
    padding: 5px;
    cursor: pointer;
}
._3PLTX ._1s967 {
    height: 40px;
    border-radius: 50% 50% 0 0/100% 100% 0 0;
    background-color: #fff;
    margin-top: -40px;
}
._3PLTX ._2w_E5 {
    margin: 40px auto 0;
    width: 700px;
    font-size: 14px;
}
._3PLTX ._2w_E5 ._23R_O {
    margin-bottom: 36px;
}
._3PLTX ._2w_E5 ._23R_O ._1WCUC {
    float: right;
    border: 1px solid #d9d9d9;
    position: relative;
    width: 200px;
    height: 34px;
    border-radius: 17px;
    padding: 5px 20px 5px 30px;
}
._3PLTX ._2w_E5 ._23R_O ._1WCUC i {
    position: absolute;
    left: 10px;
    top: 50%;
    margin-top: -8px;
    font-size: 16px;
    color: #ccc;
}
._3PLTX ._2w_E5 ._23R_O ._1WCUC input {
    line-height: 24px;
    height: 24px;
    width: 100%;
    font-size: 14px;
    background-color: transparent;
}
._3PLTX ._2w_E5 ._23R_O ._3dZoJ {
    font-size: 16px;
    font-weight: 500;
    line-height: 38px;
}
._3PLTX ._2w_E5 ._18jMg {
    position: relative;
    margin-bottom: 50px;
}
._3PLTX ._2w_E5 ._18jMg h3 {
    margin-bottom: 0;
    height: 40px;
    line-height: 40px;
    padding: 0 6px 0 14px;
    background-color: #f2f2f2;
    font-size: 14px;
}
._3PLTX ._2w_E5 a {
    color: #42c02e;
}
._3PLTX ._2w_E5 ._18jMg h3 a {
    margin-left: 15px;
}
._3PLTX ._2w_E5 ._18jMg ._1hEmG {
    position: relative;
    margin: 1px 0 0 1px;
    zoom: 1;
    min-height: 72px;
}
._3PLTX ._2w_E5 ._18jMg ._1hEmG:after, ._3PLTX ._2w_E5 ._18jMg ._1hEmG:before {
    content: " ";
    display: table;
}
._3PLTX ._2w_E5 ._18jMg ._1hEmG li {
    float: left;
    width: 234px;
    border: 1px solid #f2f2f2;
    position: relative;
    margin: -1px 0 0 -1px;
    list-style-type: none;
}
._3PLTX ._2w_E5 a {
    color: #42c02e;
}
._3PLTX ._2w_E5 ._18jMg ._1hEmG li a {
    position: absolute;
    top: 24px;
    right: 15px;
}
img {
    vertical-align: middle;
    border-style: none;
}
._3PLTX ._2w_E5 ._18jMg ._1hEmG li img {
    position: absolute;
    left: 15px;
    height: 40px;
    width: 40px;
    top: 15px;
    border-radius: 10%;
}
._3PLTX ._2w_E5 ._18jMg ._1hEmG li ._1CN24 {
    display: block;
    font-weight: 700;
    color: #595959;
    width: 100%;
    padding: 0 60px 0 75px;
    line-height: 70px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
._3PLTX ._2w_E5 ._23R_O ._1WCUC input {
  line-height: 24px;
  height: 24px;
  width: 100%;
  font-size: 14px;
  background-color: transparent;
  outline: none;
  border: 0;
}
._3PLTX ._2w_E5 ._23R_O ._1WCUC i {
    position: absolute;
    left: 10px;
    top: 50%;
    margin-top: -8px;
    font-size: 16px;
    color: #ccc;
}
._3PLTX ._2w_E5 ._23R_O ._1WCUC {
    float: right;
    border: 1px solid #d9d9d9;
    position: relative;
    width: 200px;
    height: 34px;
    border-radius: 17px;
    padding: 5px 20px 5px 30px;
}
._3PLTX ._2w_E5 ._18jMg ._1hEmG ._3GDE6 {
    width: 49.85666666%;
}
._3PLTX ._2w_E5 ._18jMg ._1hEmG li img {
    position: absolute;
    left: 15px;
    height: 40px;
    width: 40px;
    top: 15px;
    border-radius: 10%;
}
img {
    vertical-align: middle;
    border-style: none;
}
._3PLTX ._2w_E5 ._18jMg ._1hEmG li ._1CN24 {
    display: block;
    font-weight: 700;
    color: #595959;
    width: 100%;
    padding: 0 60px 0 75px;
    line-height: 70px;
    overflow: hidden;
    -o-text-overflow: ellipsis;
    text-overflow: ellipsis;
    white-space: nowrap;
}
._1hEmG a{
  cursor: pointer;
}
._3PLTX ._2w_E5 ._18jMg ._1hEmG ._3GDE6 ._1CN24 {
    display: block;
    padding: 18px 65px 16px;
    line-height: 1;
}
._3PLTX ._2w_E5 ._18jMg ._1hEmG ._3GDE6 ._1CN24 em {
    font-weight: 400;
    font-style: normal;
    color: #999;
    display: block;
    margin-top: 8px;
    font-size: 12px;
}
._3PLTX ._2w_E5 a {
    color: #42c02e;
}
._3PLTX ._2w_E5 ._18jMg ._1hEmG li a {
    position: absolute;
    top: 24px;
    right: 15px;
}
._3PLTX ._2w_E5 ._18jMg ._1hEmG:after {
  clear: both;
  visibility: hidden;
  font-size: 0;
  height: 0;
}
._3PLTX ._27pBl {
    padding: 30px 0;
    text-align: center;
}
._3PLTX ._2w_E5 ._18jMg ._1hEmG ._3GDE6 ._1CN24 {
    display: block;
    padding: 18px 65px 16px;
    line-height: 1;
}
</style>
