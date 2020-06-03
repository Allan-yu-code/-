<template>
  <div class="_21bLU4 _3kbg6I" @click.stop="is_show_reward_window=false;">
   <Header></Header>
   <div class="_3VRLsv" role="main">
    <div class="_gp-ck">
     <section class="ouvJEz">
      <h1 class="_1RuRku">{{article.name}}</h1>
      <div class="rEsl9f">
       <div class="_2mYfmT">
        <router-link to="" class="_1OhGeD"><img class="_13D2Eh" :src="article.user.avatar" alt="" /></router-link>
        <div style="margin-left: 8px;">
         <div class="_3U4Smb">
          <span class="FxYr8x"><a class="_1OhGeD" href="">{{article.user.nickname}}</a></span>
          <button type="button" class="_3kba3h _1OyPqC _3Mi9q9 _34692-" @click="focus_author(false)" v-if="article.focus"><span @mouseover="focus_text='取消关注'" @mouseout="focus_text='已关注'">{{focus_text}}</span></button>
          <button type="button" class="_3kba3h _1OyPqC _3Mi9q9 _34692-" @click="focus_author(true)" v-else><span @mouseover="focus_text2='关注'" @mouseout="focus_text2='未关注'">{{focus_text2}}</span></button>
         </div>
         <div class="s-dsoj">
          <time>{{article.updated_time|timeformat}}</time>
          <span>字数 {{article.content.length}}</span>
          <span>阅读 {{article.read_count}}</span>
         </div>
        </div>
       </div>
      </div>
      <article class="_2rhmJa" v-html="article.html_content">
      </article>
      <div></div>
      <div class="_1kCBjS">
       <div class="_18vaTa">
        <div class="_3BUZPB">
         <div class="_2Bo4Th" role="button" tabindex="-1" aria-label="给文章点赞">
          <i aria-label="ic-like" class="anticon">
           <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
            <use xlink:href="#ic-like"></use>
           </svg></i>
         </div>
         <span class="_1LOh_5" role="button" tabindex="-1" aria-label="查看点赞列表">8人点赞<i aria-label="icon: right" class="anticon anticon-right">
           <svg viewbox="64 64 896 896" focusable="false" class="" data-icon="right" width="1em" height="1em" fill="currentColor" aria-hidden="true">
            <path d="M765.7 486.8L314.9 134.7A7.97 7.97 0 0 0 302 141v77.3c0 4.9 2.3 9.6 6.1 12.6l360 281.1-360 281.1c-3.9 3-6.1 7.7-6.1 12.6V883c0 6.7 7.7 10.4 12.9 6.3l450.8-352.1a31.96 31.96 0 0 0 0-50.4z"></path>
           </svg></i></span>
        </div>
        <div class="_3BUZPB">
         <div class="_2Bo4Th" role="button" tabindex="-1">
          <i aria-label="ic-dislike" class="anticon">
           <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
            <use xlink:href="#ic-dislike"></use>
           </svg></i>
         </div>
        </div>
       </div>
       <div class="_18vaTa">
        <a class="_3BUZPB _1x1ok9 _1OhGeD" href="/nb/38290018" target="_blank" rel="noopener noreferrer"><i aria-label="ic-notebook" class="anticon">
          <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
           <use xlink:href="#ic-notebook"></use>
          </svg></i><span>随笔</span></a>
        <div class="_3BUZPB ant-dropdown-trigger">
         <div class="_2Bo4Th">
          <i aria-label="ic-others" class="anticon">
           <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
            <use xlink:href="#ic-others"></use>
           </svg></i>
         </div>
        </div>
       </div>
      </div>
      <div class="_19DgIp" style="margin-top:24px;margin-bottom:24px"></div>
      <div class="_13lIbp">
       <div class="_191KSt">
        &quot;小礼物走一走，来简书关注我&quot;
       </div>
       <button type="button" class="_1OyPqC _3Mi9q9 _2WY0RL _1YbC5u" @click.stop="is_show_reward_window=true;"><span>赞赏支持</span></button>
       <span class="_3zdmIj">还没有人赞赏，支持一下</span>
      </div>
      <div class="d0hShY">
       <a class="_1OhGeD" href="/u/a70487cda447" target="_blank" rel="noopener noreferrer"><img class="_27NmgV" src="https://upload.jianshu.io/users/upload_avatars/18529254/.png?imageMogr2/auto-orient/strip|imageView2/1/w/100/h/100/format/webp" alt="  " /></a>
       <div class="Uz-vZq">
        <div class="Cqpr1X">
         <a class="HC3FFO _1OhGeD" href="/u/a70487cda447" title="書酱" target="_blank" rel="noopener noreferrer">書酱</a>
         <span class="_2WEj6j" title="你读书的样子真好看。">你读书的样子真好看。</span>
        </div>
        <div class="lJvI3S">
         <span>总资产0</span>
         <span>共写了78.7W字</span>
         <span>获得6,072个赞</span>
         <span>共1,308个粉丝</span>
        </div>
       </div>
       <button data-locale="zh-CN" type="button" class="_1OyPqC _3Mi9q9"><span>关注</span></button>
      </div>
     </section>
     <div id="note-page-comment">
      <div class="lazyload-placeholder"></div>
     </div>
    </div>
    <aside class="_2OwGUo">
     <section class="_3Z3nHf">
      <div class="_3Oo-T1">
       <a class="_1OhGeD" href="/u/a70487cda447" target="_blank" rel="noopener noreferrer"><img class="_3T9iJQ" src="https://upload.jianshu.io/users/upload_avatars/18529254/.png?imageMogr2/auto-orient/strip|imageView2/1/w/90/h/90/format/webp" alt="" /></a>
       <div class="_32ZTTG">
        <div class="_2O0T_w">
         <div class="_2v-h3G">
          <span class="_2vh4fr" title="書酱"><a class="_1OhGeD" href="/u/a70487cda447" target="_blank" rel="noopener noreferrer">書酱</a></span>
         </div>
         <button data-locale="zh-CN" type="button" class="tzrf9N _1OyPqC _3Mi9q9 _34692-"><span>关注</span></button>
        </div>
        <div class="_1pXc22">
         总资产0
        </div>
       </div>
      </div>
      <div class="_19DgIp"></div>
     </section>
     <div>
      <div class="">
       <section class="_3Z3nHf">
        <h3 class="QHRnq8 QxT4hD"><span>推荐阅读</span></h3>
        <div class="cuOxAY" role="listitem">
         <div class="_3L5YSq" title="这些话没人告诉你，但必须知道的社会规则">
          <a class="_1-HJSV _1OhGeD" href="/p/a3e56a0559ff" target="_blank" rel="noopener noreferrer">这些话没人告诉你，但必须知道的社会规则</a>
         </div>
         <div class="_19haGh">
          阅读 5,837
         </div>
        </div>
        <div class="cuOxAY" role="listitem">
         <div class="_3L5YSq" title="浙大学霸最美笔记曝光：真正的牛人，都“变态”到了极致">
          <a class="_1-HJSV _1OhGeD" href="/p/d2a3724e2839" target="_blank" rel="noopener noreferrer">浙大学霸最美笔记曝光：真正的牛人，都“变态”到了极致</a>
         </div>
         <div class="_19haGh">
          阅读 12,447
         </div>
        </div>
        <div class="cuOxAY" role="listitem">
         <div class="_3L5YSq" title="征服一个女人最好的方式：不是讨好她，而是懂得去折腾她">
          <a class="_1-HJSV _1OhGeD" href="/p/f6acf67f039b" target="_blank" rel="noopener noreferrer">征服一个女人最好的方式：不是讨好她，而是懂得去折腾她</a>
         </div>
         <div class="_19haGh">
          阅读 5,311
         </div>
        </div>
        <div class="cuOxAY" role="listitem">
         <div class="_3L5YSq" title="告别平庸的15个小方法">
          <a class="_1-HJSV _1OhGeD" href="/p/cff7eb6b232b" target="_blank" rel="noopener noreferrer">告别平庸的15个小方法</a>
         </div>
         <div class="_19haGh">
          阅读 7,040
         </div>
        </div>
        <div class="cuOxAY" role="listitem">
         <div class="_3L5YSq" title="轻微抑郁的人，会说这3句“口头禅”，若你一个不占，偷着乐吧">
          <a class="_1-HJSV _1OhGeD" href="/p/2a0ca1729b4b" target="_blank" rel="noopener noreferrer">轻微抑郁的人，会说这3句“口头禅”，若你一个不占，偷着乐吧</a>
         </div>
         <div class="_19haGh">
          阅读 16,411
         </div>
        </div>
       </section>
      </div>
     </div>
    </aside>
   </div>

    <div class="_23ISFX-body" v-if="is_show_reward_window" @click.stop="is_show_reward_window=true">
     <div class="_3uZ5OL">
      <div class="_2PLkjk">
       <img class="_2R1-48" src="https://upload.jianshu.io/users/upload_avatars/9602437/8fb37921-2e4f-42a7-8568-63f187c5721b.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/100/h/100/format/webp" alt="" />
       <div class="_2h5tnQ">
        给作者送糖
       </div>
      </div>
      <div class="_1-bCJJ">
       <div class="LMa6S_" :class="reward_info.money==num?'_1vONvL':''" @click="reward_info.money=num" v-for="num in reward_list"><span>{{num}}</span></div>
      </div>
      <textarea class="_1yN79W" placeholder="给Ta留言..." v-model="reward_info.content"></textarea>
      <div class="_1_B577">选择支付方式</div>
      <div class="_1-bCJJ">
       <div class="LMa6S_ _3PA8BN" :class="reward_info.pay_type==type?'_1vONvL':''" @click="reward_info.pay_type=type" v-for="type in pay_type_list"><span>{{type}}</span></div>
      </div>
      <button type="button" class="_3A-4KL _1OyPqC _3Mi9q9 _1YbC5u" @click="payhandler"><span>确认支付</span><span> ￥</span>{{reward_info.money}}</button>
     </div>
    </div>

   <Footer></Footer>
  </div>
</template>

<script>
    import Header from "./common/Header";
    import Footer from "./common/Footer";
    export default {
        name: "Article",
        components:{
          Header,
          Footer,
        },
        data(){
            return {
                token: "",
                article_id: 0,
                focus_text:"已关注",
                focus_text2: "未关注",
                article: {
                    content:"",
                    user:{},
                    collection:{},
                },
                is_show_reward_window:false, // 控制赞赏窗口的显示隐藏
                reward_list:[2,5,10,20,50,100],  // 赞赏的金额
                pay_type_list: ["支付宝","余额支付"], // 赞赏的支付方式
                reward_info:{  // 赞赏的表单信息
                    money: 2,
                    content:"",
                    pay_type:"支付宝",
                }
            }
        },
        created(){
            this.token = sessionStorage.user_token || localStorage.user_token;
            this.article_id = this.$route.params.id;
            this.get_article();
        },
        filters:{
            timeformat(time){
                if(time){
                  return time.split(".")[0].replace("T"," ")
                }else{
                  return time;
                }
            }
        },
        methods:{
            get_article(){
                // 获取文章详情信息
                this.$axios.get(`${this.$settings.Host}/article/retrieve/${this.article_id}/`,{
                    headers:{
                        Authorization: "jwt " + this.token,
                    }
                }).then(response=>{
                    this.article = response.data;
                }).catch(error=>{
                    this.$message.error("当前文章已删除!");
                    this.$router.go(-1);
                });
            },
            payhandler(){
                // 赞赏支付的处理
                // 验证登录
                if(!this.token){
                  this.$settings.check_user_login(this,"打赏失败","您尚未登录，无法进行打赏！","跳转到登录","/login");
                  return ;
                }
                // 发起请求，获取支付链接
                let pay_type = "";
                if(this.reward_info.pay_type === "支付宝"){
                    pay_type = 1;
                }else{
                    pay_type = 2;
                }
                this.$axios.post(`${this.$settings.Host}/payments/alipay/`, {
                  "money": this.reward_info.money,
                  "article_id": this.article_id,
                  "type": pay_type,
                  "message": this.reward_info.content,
                },{
                    headers:{
                      Authorization: "jwt " + this.token
                    }
                }).then(response=>{
                  // 跳转到支付页面
                  this.$message.success("跳转支付页面中...请稍候");
                  setTimeout(()=>{
                    location.href = response.data;
                  },2000);
                 }).catch(error=>{
                  this.$message.error("无法发起赞赏！");
                });
            },
            focus_author(focus){
                // 关注或取消关注
                this.$settings.check_user_login(this,"警告","您尚未登录！","跳转到登录", "/login");
                this.$axios.post(`${this.$settings.Host}/article/focus/`,{
                    author_id: this.article.user.id,
                    focus: focus
                },{
                    headers:{
                        Authorization: "jwt " + this.token,
                    }
                }).then(response=>{
                   this.article.focus=focus;
                }).catch(error=>{
                   this.$message.error("网络错误！关注或取消关注失败！");
                });
            }
        }
    }
</script>

<style scoped>
*,:after,:before {
	box-sizing: border-box;
}

a:hover {
	color: #fa9e87
}

a:active {
	color: #c75342
}

a:active,a:hover {
	text-decoration: none;
	outline: 0
}

a[disabled] {
	color: rgba(0,0,0,.25);
	cursor: not-allowed;
	pointer-events: none
}

img {
	vertical-align: middle;
	border-style: none
}

svg:not(:root) {
	overflow: hidden
}
[role=button],a,area,button,input:not([type=range]),label,select,summary,textarea {
	-ms-touch-action: manipulation;
	touch-action: manipulation
}

button,input,optgroup,select,textarea {
	margin: 0;
	color: inherit;
	font-size: inherit;
	font-family: inherit;
	line-height: inherit
}

button,input {
	overflow: visible
}

button,select {
	text-transform: none
}[type=reset],[type=submit],button,html [type=button] {
	-webkit-appearance: button
}[type=button]::-moz-focus-inner,[type=reset]::-moz-focus-inner,[type=submit]::-moz-focus-inner,button::-moz-focus-inner {
	padding: 0;
	border-style: none
}

input[type=checkbox],input[type=radio] {
	-webkit-box-sizing: border-box;
	box-sizing: border-box;
	padding: 0
}

input[type=date],input[type=datetime-local],input[type=month],input[type=time] {
	-webkit-appearance: listbox
}

textarea {
	overflow: auto;
	resize: vertical
}

fieldset {
	min-width: 0;
	margin: 0;
	padding: 0;
	border: 0
}

legend {
	display: block;
	width: 100%;
	max-width: 100%;
	margin-bottom: .5em;
	padding: 0;
	color: inherit;
	font-size: 1.5em;
	line-height: inherit;
	white-space: normal
}

progress {
	vertical-align: baseline
}

::selection {
	color: #fff;
	background: #ec7259
}

.anticon {
	display: inline-block;
	color: inherit;
	font-style: normal;
	line-height: 0;
	text-align: center;
	text-transform: none;
	vertical-align: -.125em;
	text-rendering: optimizeLegibility;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale
}

.anticon>* {
	line-height: 1
}

.anticon svg {
	display: inline-block
}

.anticon:before {
	display: none
}

.anticon .anticon-icon {
	display: block
}

.anticon[tabindex] {
	cursor: pointer
}

._3Vh8Z9-info ._3Vh8Z9-notice-content .anticon,._3Vh8Z9-loading ._3Vh8Z9-notice-content .anticon {
	color: #0681d0
}

._3Vh8Z9-success ._3Vh8Z9-notice-content .anticon {
	color: #42c02e
}

._3Vh8Z9-warning ._3Vh8Z9-notice-content .anticon {
	color: #fa0
}

._3Vh8Z9-error ._3Vh8Z9-notice-content .anticon {
	color: #f50
}


._1OyPqC {
	position: relative;
	flex-shrink: 0;
	display: inline-flex;
	justify-content: center;
	align-items: center;
	border-radius: 50px;
	touch-action: manipulation;
	cursor: pointer;
	background-image: none;
	white-space: nowrap;
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
	transition: all .2s cubic-bezier(.645,.045,.355,1);
	font-size: 14px;
	padding: 4px 12px;
	color: #969696;
	background-color: #fff;
	border: 1px solid #999
}

._1OyPqC+._1OyPqC,._1OyPqC>.anticon+span,._1OyPqC>span+.anticon {
	margin-left: 8px
}

._1OyPqC:focus,._1OyPqC:hover {
	color: #7d7d7d;
	background-color: #fff;
	border-color: #999
}

._1OyPqC:active {
	color: #636363;
	background-color: #fff;
	border-color: #999
}

body.reader-night-mode ._1OyPqC {
	color: #b3b3b3;
	background-color: #3d3d3d;
	border-color: #999
}

body.reader-night-mode ._1OyPqC:focus,body.reader-night-mode ._1OyPqC:hover {
	color: #ccc;
	background-color: #3d3d3d;
	border-color: #999
}

body.reader-night-mode ._1OyPqC:active {
	color: #e6e6e6;
	background-color: #3d3d3d;
	border-color: #999
}

._3Mi9q9,._3Mi9q9[disabled]:hover {
	color: #ec7259;
	background-color: #fff;
	border-color: #ec7259
}

._3Mi9q9:focus,._3Mi9q9:hover {
	color: #ec7259;
	background-color: #fef8f7;
	border-color: #ec7259
}

._3Mi9q9:active {
	color: #ec7259;
	background-color: #fdf1ee;
	border-color: #ec7259
}

body.reader-night-mode ._3Mi9q9,body.reader-night-mode ._3Mi9q9[disabled]:hover {
	color: #ec7259;
	background-color: #3d3d3d;
	border-color: #ec7259
}

body.reader-night-mode ._3Mi9q9:focus,body.reader-night-mode ._3Mi9q9:hover {
	color: #ec7259;
	background-color: #46403f;
	border-color: #ec7259
}

body.reader-night-mode ._3Mi9q9:active {
	color: #ec7259;
	background-color: #4f4240;
	border-color: #ec7259
}

._3Mi9q9._2SIRy5:before {
	content: "";
	position: absolute;
	border-radius: inherit;
	border: 0 solid #ec7259;
	animation: ZAhfCQ .3s ease-out forwards
}

._3Mi9q9._1YbC5u,._3Mi9q9._1YbC5u[disabled]:hover {
	color: #fff;
	background-color: #ec7259;
	border-color: #ec7259
}

._3Mi9q9._1YbC5u:focus,._3Mi9q9._1YbC5u:hover {
	color: #fff;
	background-color: #ed7961;
	border-color: #ec7259
}

._3Mi9q9._1YbC5u:active {
	color: #fff;
	background-color: #ee806a;
	border-color: #ec7259
}

body.reader-night-mode ._3Mi9q9._1YbC5u,body.reader-night-mode ._3Mi9q9._1YbC5u[disabled]:hover {
	color: #fff;
	background-color: #ec7259;
	border-color: #ec7259
}

body.reader-night-mode ._3Mi9q9._1YbC5u:focus,body.reader-night-mode ._3Mi9q9._1YbC5u:hover {
	color: #fff;
	background-color: #ed7961;
	border-color: #ec7259
}

body.reader-night-mode ._3Mi9q9._1YbC5u:active {
	color: #fff;
	background-color: #ee806a;
	border-color: #ec7259
}

._3tVfGA {
	color: #999
}

._3tVfGA hr {
	margin: 16px 0;
	border: none;
	border-top: 1px solid #eee
}

body.reader-night-mode ._3tVfGA hr {
	border-color: #2f2f2f
}

.PY53UF:hover>i {
	visibility: visible;
	opacity: 1
}

.PY53UF>span {
	margin-right: 4px;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap
}

.PY53UF>i {
	font-size: 12px;
	visibility: hidden;
	opacity: 0
}


._3VRLsv {
	box-sizing: content-box;
	width: 1000px;
	padding-left: 16px;
	padding-right: 16px;
	margin-left: auto;
	margin-right: auto
}

._3Z3nHf,.ouvJEz {
	background-color: #fff;
	border-radius: 4px;
	margin-bottom: 10px
}

body.reader-night-mode ._3Z3nHf,body.reader-night-mode .ouvJEz {
	background-color: #3d3d3d
}

._3kbg6I {
	background-color: #f9f9f9
}

body.reader-night-mode ._3kbg6I {
	background-color: #2d2d2d
}

._3VRLsv {
	display: flex;
	justify-content: center;
	align-items: flex-start;
	min-height: calc(100vh - 66px);
	padding-top: 10px;
	font-size: 16px
}

._gp-ck {
	flex-shrink: 0;
	width: 730px;
	margin-bottom: 24px;
	margin-right: 10px
}

.ouvJEz {
	padding: 24px
}

._2OwGUo {
	flex-shrink: 0;
	width: 260px
}

._3Z3nHf {
	padding: 16px
}

.QxT4hD {
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 16px;
	padding-left: 12px;
	border-left: 4px solid #ec7259;
	font-size: 18px;
	font-weight: 500;
	height: 20px;
	line-height: 20px
}

._3Fatyw>i {
	font-size: 18px;
	margin-right: 4px
}

.nnghRR>p {
	margin-bottom: 0
}


.LtPwLP>div {
	min-height: 100px;
	flex-grow: 1
}

.LtPwLP img {
	width: 150px;
	height: 100px;
	border-radius: 4px;
	border: 1px solid #f2f2f2;
	flex-shrink: 0
}

._3nj4GN>span {
	margin-left: 8px;
	line-height: 20px
}

._3nj4GN .anticon {
	font-size: 22px
}

.rEsl9f {
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 32px;
	font-size: 13px
}

.s-dsoj {
	display: flex;
	color: #969696
}

.s-dsoj>:not(:last-child) {
	margin-right: 10px
}

._3tCVn5 i {
	margin-right: .5em
}

._2mYfmT {
	display: flex;
	align-items: center
}

._13D2Eh {
	display: block;
	border-radius: 50%;
	border: 1px solid #eee;
	min-width: 48px;
	min-height: 48px;
	width: 48px;
	height: 48px
}

body.reader-night-mode ._13D2Eh {
	border-color: #2f2f2f
}

._3U4Smb {
	display: flex;
	align-items: center;
	margin-bottom: 6px
}

.FxYr8x {
	font-size: 16px;
	font-weight: 500;
	margin-right: 8px
}

._3kba3h {
	padding: 2px 9px
}

._2rhmJa code,._2rhmJa pre,._2rhmJa pre[class*=language-] {
	font-family: Consolas,Monaco,"Andale Mono","Ubuntu Mono",monospace;
	font-size: 12px
}

._2rhmJa {
	font-weight: 400;
	line-height: 1.8;
	margin-bottom: 20px
}


._2rhmJa h1,._2rhmJa h2,._2rhmJa h3,._2rhmJa h4,._2rhmJa h5,._2rhmJa h6 {
	margin-bottom: 16px
}

._2rhmJa h1 {
	font-size: 26px
}

._2rhmJa h2 {
	font-size: 24px
}

._2rhmJa h3 {
	font-size: 22px
}

._2rhmJa h4 {
	font-size: 20px
}

._2rhmJa h5 {
	font-size: 18px
}

._2rhmJa h6 {
	font-size: 16px
}

._2rhmJa p {
	margin-bottom: 20px;
	word-break: break-word
}

._2rhmJa hr {
	margin: 0 0 20px;
	border: 0;
	border-top: 1px solid #eee!important
}

body.reader-night-mode ._2rhmJa hr {
	border-color: #2f2f2f!important
}

._2rhmJa blockquote {
	padding: 20px;
	background-color: #fafafa;
	border-left: 6px solid #e6e6e6;
	word-break: break-word;
	font-size: 16px;
	font-weight: normal;
	line-height: 30px;
	margin: 0 0 20px
}

body.reader-night-mode ._2rhmJa blockquote {
	background-color: #595959;
	border-color: #262626
}

._2rhmJa blockquote h1:last-child,._2rhmJa blockquote h2:last-child,._2rhmJa blockquote h3:last-child,._2rhmJa blockquote h4:last-child,._2rhmJa blockquote h5:last-child,._2rhmJa blockquote h6:last-child,._2rhmJa blockquote li:last-child,._2rhmJa blockquote ol:last-child,._2rhmJa blockquote p:last-child,._2rhmJa blockquote ul:last-child {
	margin-bottom: 0
}

._2rhmJa blockquote .image-package {
	width: 100%;
	margin-left: 0
}

._2rhmJa ol,._2rhmJa ul {
	word-break: break-word;
	margin: 0 0 20px 20px
}

._2rhmJa ol li,._2rhmJa ul li {
	line-height: 30px
}

._2rhmJa ol li ol,._2rhmJa ol li ul,._2rhmJa ul li ol,._2rhmJa ul li ul {
	margin-top: 16px
}

._2rhmJa ol {
	list-style-type: decimal
}

._2rhmJa ul {
	list-style-type: disc
}

._2rhmJa code {
	padding: 2px 4px;
	border: none;
	vertical-align: middle;
	white-space: pre-wrap
}

._2rhmJa :not(pre) code {
	color: #c7254e;
	background-color: #f2f2f2
}

body.reader-night-mode ._2rhmJa :not(pre) code {
	background-color: #262626
}

._2rhmJa pre,._2rhmJa pre[class*=language-] {
	word-wrap: normal;
	word-break: break-all;
	white-space: pre;
	overflow-x: scroll;
	overscroll-behavior-x: contain;
	margin-top: 0;
	margin-bottom: 20px;
	border-radius: 4px;
	z-index: 0;
	padding: 1em;
	line-height: 1.5;
	color: #ccc;
	background: #2d2d2d
}

._2rhmJa pre[class*=language-] code,._2rhmJa pre code {
	padding: 0;
	background-color: transparent;
	color: inherit;
	white-space: pre;
	vertical-align: unset
}

._2rhmJa table {
	width: 100%;
	margin-bottom: 20px;
	border-collapse: collapse;
	border: 1px solid #eee;
	border-left: none;
	word-break: break-word
}

body.reader-night-mode ._2rhmJa table,body.reader-night-mode ._2rhmJa table td,body.reader-night-mode ._2rhmJa table th {
	border-color: #2f2f2f
}

._2rhmJa table td,._2rhmJa table th {
	padding: 8px;
	border: 1px solid #eee;
	line-height: 20px;
	vertical-align: middle
}

._2rhmJa table th {
	font-weight: bold
}

._2rhmJa table thead th {
	vertical-align: middle;
	text-align: inherit
}

._2rhmJa table tr:nth-of-type(2n) {
	background-color: hsla(0,0%,70.2%,.15)
}

._2rhmJa table .image-package {
	width: 100%;
	margin-left: 0
}

._2rhmJa img {
	max-width: 100%
}

._2rhmJa .image-package {
	width: 100%;
	margin: 0;
	padding-bottom: 25px;
	text-align: center;
	font-size: 0
}

._2rhmJa .image-package img {
	max-width: 100%;
	width: auto;
	height: auto;
	vertical-align: middle;
	border: 0
}

body.reader-night-mode ._2rhmJa .image-package img {
	opacity: .85
}

._2rhmJa .image-package .image-container {
	position: relative;
	z-index: 95;
	background-color: #e6e6e6;
	transition: background-color .1s linear;
	margin: 0 auto
}

body.reader-night-mode ._2rhmJa .image-package .image-container {
	background-color: #595959
}

._2rhmJa .image-package .image-container-fill {
	z-index: 90
}

._2rhmJa .image-package .image-container .image-view {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	overflow: hidden
}

._2rhmJa .image-package .image-container .image-view-error {
	cursor: pointer;
	color: grey
}

body.reader-night-mode ._2rhmJa .image-package .image-container .image-view-error {
	color: #b3b3b3
}

._2rhmJa .image-package .image-container .image-view-error:after {
	content: "\56FE\7247\83B7\53D6\5931\8D25\FF0C\8BF7\70B9\51FB\91CD\8BD5";
	position: absolute;
	top: 50%;
	left: 50%;
	width: 100%;
	transform: translate(-50%,-50%);
	color: inherit;
	font-size: 14px
}

._2rhmJa .image-package .image-container .image-view img.image-loading {
	opacity: .3
}

._2rhmJa .image-package .image-container .image-view img {
	transition: all .15s linear;
	z-index: 95;
	opacity: 1
}

._2rhmJa .image-package .image-caption {
	min-width: 20%;
	max-width: 80%;
	min-height: 43px;
	display: inline-block;
	padding: 10px;
	margin: 0 auto;
	border-bottom: 1px solid #eee;
	font-size: 13px;
	color: #999
}

._2rhmJa .image-package .image-caption:empty {
	display: none
}

body.reader-night-mode ._2rhmJa .image-package .image-caption {
	border-color: #2f2f2f
}

._2rhmJa .math-block[mathimg="1"] {
	display: block;
	margin: 1em auto
}

._2rhmJa .math-inline[mathimg="1"] {
	display: inline;
	margin: 0 3px;
	vertical-align: middle
}

._2rhmJa .math-block[mathimg="1"],._2rhmJa .math-inline[mathimg="1"] {
	max-width: 100%
}

body.reader-night-mode ._2rhmJa .math-block[mathimg="1"],body.reader-night-mode ._2rhmJa .math-inline[mathimg="1"] {
	filter: invert(.8)
}

._3GbnS5 {
	padding: 0;
	line-height: 1.5;
	position: relative;
	width: 100%;
	height: 1px;
	margin: 20px 0;
	border: none;
	border-top: #b3b3b3;
	display: table;
	white-space: nowrap;
	text-align: center
}

._3GbnS5:after,._3GbnS5:before {
	content: "";
	display: table-cell;
	position: relative;
	top: 50%;
	left: 0;
	width: 50%;
	border-top: 1px solid;
	border-top-color: inherit;
	transform: scaleY(.5) translateY(50%);
	transform-origin: 50% 50% 0;
	transform-origin: initial
}

._2Lt-af {
	display: inline-block;
	padding: 0 12px;
	font-size: 14px;
	font-weight: normal;
	text-align: center;
	white-space: nowrap;
	color: #b3b3b3;
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none
}

._2Lt-af>a {
	margin-left: .5em
}

._19DgIp {
	width: 100%;
	height: 1px;
	margin: 16px 0;
	background-color: #eee
}

body.reader-night-mode ._19DgIp {
	background-color: #2f2f2f
}

._1kCBjS {
	justify-content: space-between;
	font-size: 14px;
	color: #969696;
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none
}

._1kCBjS,._3BUZPB,._18vaTa {
	display: flex;
	align-items: center
}

._3BUZPB>span {
	margin-left: 8px
}

._3BUZPB:not(:last-child) {
	margin-right: 12px
}

._2Bo4Th {
	display: flex;
	align-items: center;
	justify-content: center;
	width: 40px;
	height: 40px;
	color: #969696;
	border: 1px solid #eee;
	border-radius: 50%;
	font-size: 18px;
	cursor: pointer
}

body.reader-night-mode ._2Bo4Th {
	border-color: #2f2f2f
}


._1LOh_5 {
	cursor: pointer
}

._1LOh_5 .anticon {
	font-size: 12px
}

._1x1ok9 {
	cursor: pointer
}

._1x1ok9 .anticon {
	font-size: 16px
}

._1yN79W {
	background-color: #f2f2f2
}

._1yN79W:-ms-input-placeholder {
	color: #999
}

._1yN79W::-ms-input-placeholder {
	color: #999
}

._1yN79W::placeholder {
	color: #999
}

body.reader-night-mode ._1yN79W {
	background-color: #333
}

._3uZ5OL {
	text-align: center;
	padding: 48px 64px;
  ext-align: center;
  padding: 48px 64px;
  width: 50%;
  position: fixed;
  top: 0;
  height: 540px;
  border-radius: 5px;
  left: 0;
  right: 0;
  bottom: 0;
  background: #eee;
  z-index: 999;
  margin: auto;
}

._2PLkjk {
	display: flex;
	justify-content: center;
	align-items: center;
	margin-bottom: 24px
}

._2R1-48 {
	min-width: 50px;
	min-height: 50px;
	width: 50px;
	height: 50px;
	border-radius: 50%;
	border: 1px solid #eee
}

._2h5tnQ {
	font-size: 24px;
	font-weight: 500;
	margin-left: 16px
}

._1-bCJJ {
	flex-wrap: wrap
}

._1-bCJJ,.LMa6S_ {
	display: flex;
	justify-content: center
}

.LMa6S_ {
	align-items: center;
	width: 162.5px;
	height: 56px;
	font-size: 16px;
	color: #969696;
	margin-bottom: 12px;
	margin-right: 12px;
	border-radius: 10px;
	border: 1px solid #eee;
	cursor: pointer;
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none
}

body.reader-night-mode .LMa6S_ {
	border-color: #2f2f2f
}

.LMa6S_._1vONvL {
	color: #ec7259
}

.LMa6S_._1vONvL,body.reader-night-mode .LMa6S_._1vONvL {
	border-color: #ec7259
}

.LMa6S_._1sSZ6C {
	cursor: not-allowed;
	color: #969696;
	opacity: .5
}

.LMa6S_>i {
	font-size: 20px
}

.LMa6S_>span {
	font-size: 28px;
	font-style: italic
}

.LMa6S_:nth-child(3n) {
	margin-right: 0
}

.LMa6S_:nth-last-child(-n+3) {
	margin-bottom: 0
}

.LMa6S_:last-child {
	margin-right: 0
}

._2ByDWa>span {
	font-size: 16px;
	font-style: normal;
	opacity: 1
}

._2ByDWa>input {
	position: absolute;
	top: 50%;
	left: 50%;
	width: 100%;
	height: 36px;
	margin: 0 auto;
	text-align: center;
	transform: translate(-50%,-50%);
	background-color: transparent;
	opacity: 0;
	cursor: pointer
}

._2ByDWa>input::-webkit-inner-spin-button,._2ByDWa>input::-webkit-outer-spin-button {
	display: none
}

._2ByDWa._1vONvL>span {
	opacity: 0
}

._2ByDWa._1vONvL>input {
	opacity: 1;
	cursor: text
}

._3PA8BN>i {
	font-size: 30px
}

._3PA8BN>span {
	font-size: 16px;
	font-style: normal;
	margin-left: 4px
}

._3PA8BN,._3PA8BN._1vONvL {
	color: #404040
}

body.reader-night-mode ._3PA8BN,body.reader-night-mode ._3PA8BN._1vONvL {
	color: #b3b3b3
}

._1yN79W {
	display: block;
	width: 100%;
	height: 80px;
	resize: none;
	margin-top: 12px;
	padding: 12px;
	border: none;
	border-radius: 10px
}

._1_B577 {
	font-size: 15px;
	margin: 12px 0
}

._3A-4KL {
	margin-top: 24px;
	font-size: 18px;
	font-weight: normal;
	padding: 10px 48px
}

.d0hShY {
	display: flex;
	align-items: center;
	background-color: #fafafa;
	border-radius: 4px;
	padding: 12px 16px
}

body.reader-night-mode .d0hShY {
	background-color: #333
}

._27NmgV {
	border-radius: 50%;
	border: 1px solid #eee;
	min-width: 50px;
	min-height: 50px;
	width: 50px;
	height: 50px
}

body.reader-night-mode ._27NmgV {
	border-color: #2f2f2f
}

.Uz-vZq {
	flex-grow: 1;
	margin: 0 12px;
	overflow: hidden
}

.Cqpr1X {
	display: flex;
	align-items: center;
	margin-bottom: 2px
}

.HC3FFO {
	flex-shrink: 0;
	font-size: 16px;
	font-weight: 500
}
._3GlyHK,.HC3FFO {
	margin-right: 6px
}
._2WEj6j {
	font-size: 14px;
	color: #666;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap
}
.lJvI3S {
	font-size: 14px;
	color: #969696
}
.lJvI3S>span {
	margin-right: 12px
}
.lJvI3S>span:last-child {
	margin-right: 0
}
._3MbC71>span {
	margin-right: 6px
}
._14FSyQ,.H4XBOO>img {
	width: 24px;
	height: 24px;
	min-width: 24px;
	min-height: 24px;
	border-radius: 50%;
	border: 2px solid #fff
}
body.reader-night-mode .H4XBOO>img {
	border-color: #3d3d3d
}
._13lIbp {
	display: flex;
	flex-direction: column;
	align-items: center;
	margin: 40px 0 32px
}

._191KSt {
	font-size: 16px;
	font-weight: 500;
	margin-bottom: 16px
}
._3zdmIj {
	color: #666;
	margin-top: 24px
}

._37OvKa>i {
	color: #ec7259;
	font-size: 20px;
	margin-right: 8px
}


._3S34Y_>img {
	width: 144px;
	height: 144px;
	margin-bottom: 12px
}

._2JdSds>span {
	margin-left: 2px;
	pointer-events: none
}

._3yPTTQ>i {
	font-size: 16px;
	margin-right: 4px
}

</style>
