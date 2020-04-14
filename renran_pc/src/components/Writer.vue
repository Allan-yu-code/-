<template>
  <div class="write" v-if="is_show_page">
    <div class="_2v5v5">
      <div class="_3zibT"><router-link to="/">回首页</router-link></div>
      <div class="_1iZMb">
        <div class="_33Zlg" @click="collection_form=true"><i class="fa fa-plus"></i><span>新建文集</span></div>
        <div class="_2G97m">
          <form class="M8J6Q" :class="collection_form?'_2a1Rp':'_1mU5v'">
            <input type="text" placeholder="请输入文集名..." v-model="collection_name" class="_1CtV4">
            <button type="submit" class="dwU8Q _3zXcJ _3QfkW" @click.stop.prevent="add_collection"><span>提 交</span></button>
            <button type="button" class="vIzwB _3zXcJ" @click.stop.prevent="collection_form=false"><span>取 消</span></button>
          </form>
        </div>
      </div>
      <ul class="_3MbJ4 _3t059">
        <li class="_3DM7w" :class="{_31PCv:current_collection==key}" @click.stop="current_collection=key;is_show_collection_menu=false;" :title="collection.name" v-for="collection,key in collection_list">
          <div class="_3P4JX _2VLy-" v-if="current_collection==key" @click.stop="is_show_collection_menu=!is_show_collection_menu">
            <i class="fa fa-gear"></i>
            <span>
              <ul class="_2V8zt _3FcHm _2w9pn" :class="{NvfK4:is_show_collection_menu}">
                <li class="_2po2r cRfUr" title="">
                  <span class="" @click.stop="edit_collection"><i class="fa fa-pencil-square-o _22XWG"></i>修改文集</span>
                </li>
                <li class="_2po2r cRfUr" title="">
                  <span class=""><i class="fa fa-trash-o _22XWG"></i>删除文集</span>
                </li>
              </ul>
            </span>
          </div>
          <span>{{collection.name}}</span>
        </li>
      </ul>
      <div style="height: 50px;"></div>
      <div role="button" class="h-5Am">
        <span class="ant-dropdown-trigger"><i class="fa fa-bars"></i><span>设置</span></span>
        <span class="Yv5Zx">遇到问题<i class="fa fa-question-circle-o"></i></span>
      </div>
    </div>
    <div class="rQQG7">
      <div class="_3revO _2mnPN">
        <div class="_3br9T">
          <div>
            <div class="_1GsW5" @click.stop="add_article(0)"><i class="fa fa-plus-circle"></i><span> 新建文章</span></div>
            <ul class="_2TxA-">
              <li class="_25Ilv" :class="{_33nt7:key==current_article}" @click.stop="current_article=key;" :title="article.name" v-for="article,key in article_list">
                <i class="_13kgp" :class="{_2m93u:article.is_public}"></i>
                <div class="_3P4JX poOXI" v-if="key==current_article" @click.stop="is_show_article_menu=!is_show_article_menu">
                  <i class="fa fa-gear"></i>
                  <span>
                    <ul class="_2V8zt _3FcHm _2w9pn" :class="{NvfK4:is_show_article_menu}">
                      <li class="_2po2r cRfUr" title="" v-if="!article.is_public" @click.stop="pub_article"><span class=""><i class="fa fa-share _22XWG"></i>直接发布</span></li>
                      <li class="_2po2r cRfUr" title="" v-if="!article.is_public"><span class=""><i class="fa fa-clock-o _22XWG"></i>定时发布</span></li>
                      <li class="_2po2r cRfUr" title="" v-if="!article.is_public"><span class="_20tIi"><i class="iconfont ic-paid _22XWG"></i>发布为付费文章</span></li>
                      <li class="_2po2r cRfUr" title="" v-if="article.is_public" @click.stop="pub_article"><span class=""><i class="fa fa-share _22XWG"></i>取消发布</span></li>
                      <li class="_2po2r cRfUr" title=""><span class=""><i class="iconfont ic-set _22XWG"></i>设置发布样式</span></li>
                      <li class="_3nZXj _2_WAp _3df2u _2po2r cRfUr" title=""><span class=""><i class="fa fa-folder-open _22XWG"></i>移动文章
                        <div class="_3x4X_">
                          <ul class="_2KzJx oGKRI _3DXDE _2w9pn">
                            <li class="_2po2r cRfUr" :title="collection.name" v-if="key!=current_collection" v-for="collection,key in collection_list" @click.stop="move_article(collection.id)"><span class="">{{collection.name}}</span></li>
                          </ul>
                        </div>
                      </span>
                      </li>
                      <li class="_2po2r cRfUr" title=""><span class=""><i class="fa fa-history _22XWG"></i>历史版本</span></li>
                      <li class="_2po2r cRfUr" title=""><span class=""><i class="fa fa-trash-o _22XWG"></i>删除文章</span></li>
                      <li class="_2po2r cRfUr" title=""><span class=""><i class="fa fa-ban _22XWG"></i>设置禁止转载</span></li>
                    </ul>
                  </span>
                </div>
                <span class="NariC">{{article.name}}</span>
                <span class="hLzJv">{{article.content|truncate}}</span>
                <span class="_29C-V" v-if="key==current_article">字数:{{article.content.length}}</span>
              </li>
<!--              <li class="_25Ilv" title="2020-01-12">-->
<!--                <i class="_13kgp"></i>-->
<!--                <span class="NariC">2020-01-12</span>-->
<!--                <span class="hLzJv">题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？-->

<!--题目：企业发放的奖金根据利润提成</span>-->
<!--              </li>-->
            </ul>
            <div class="_2cVn3" @click.stop="add_article(1)"><i class="fa fa-plus"></i><span> 在下方新建文章</span></div>
          </div>
        </div>
      </div>
      <input type="text" class="_24i7u" value="2020-01-12">
      <div id="editor">
        <mavon-editor
          style="height: 100%"
          v-model="editorContent"
          :ishljs="true"
          ref=md
          @imgAdd="imgAdd"
          @imgDel="imgDel"
        ></mavon-editor>
      </div>
    </div>
  </div>
</template>
<script>
    import { mavonEditor } from 'mavon-editor'
    import 'mavon-editor/dist/css/index.css'
    import "../../static/font-awesome/css/font-awesome.css";
    export default {
        name: "Writer",
        data(){
            return {
                is_show_page: false, // 是否显示页面
                collection_list:[],  // 文集列表
                article_list:[],     // 文章列表
                current_collection: 0, // 当前选中的文集下标，默认为0
                current_article:0,     // 当前选中的文章下标，默认为0
                editorContent:"",
                img_file:[],
                collection_form:false,
                collection_name:"",
                is_show_collection_menu: false, // 是否显示文集的菜单
                is_show_article_menu: false, // 是否显示文章的菜单
                position: 0,  // 添加文章的位置，默认前面插入，值为0
            }
        },
        filters:{
           truncate(content){
               if(content === null){
                   return 0;
               }
               return content.substr(0,30);
           }
        },
        watch:{
            editorContent(){
                console.log(this.editorContent);
            },
            current_collection(){
                // 切换文集
                this.get_article_of_collection();
                // 关闭文章菜单
                this.is_show_article_menu = false;
            },
            current_article(){
                // 切换文章
                this.is_show_article_menu = false;
            }
        },
        created(){
            // 判断登录
            this.$settings.check_user_login(this,"警告","您尚未登录！", "跳转到登录", "/login");
            if(this.token){
                // 显示页面
                this.is_show_page = true;
                // 获取当前用户的文集列表
                this.get_collection();
            }
        },
        mounted(){
            if(this.is_show_page){
                document.querySelector("#editor").style.height = document.documentElement.clientHeight - document.querySelector("._24i7u").clientHeight + "px";
                // 点选页面其他位置，关闭菜单
                document.onclick = (event)=>{
                    // 关闭文集菜单
                    this.is_show_collection_menu = false;
                    // 关闭文章菜单
                    this.is_show_article_menu = false;
                }
            }
        },
        components: {
          mavonEditor
        },
        methods:{
          edit_collection(){
              // 修改文集
              this.is_show_collection_menu=false; // 关闭文集的操作菜单
              this.$prompt('请输入新文集名', '提示', {
                confirmButtonText: '保存',
                cancelButtonText: '取消',
                inputPattern: /.{1,}/,
                inputErrorMessage: '文集名称不能为空!',
                inputValue: this.collection_list[this.current_collection].name,
              }).then(({ value }) => {
                 // 点击确定,需要把当前文集名称提交到服务端进行修改
                 let collection_id = this.collection_list[this.current_collection].id;
                 this.$axios.put(`${this.$settings.Host}/article/collection/${collection_id}/`,{
                     name: value,
                 },{
                     headers:{
                         Authorization:"jwt " + this.token,
                     }
                 }).then(response=>{
                     // 服务端ajax请求操作成功，则客户端的name也要发生改变
                     this.collection_list[this.current_collection].name = value;
                 }).catch(error=>{
                     this.$message.error(error.response.data);
                 })
              }).catch(() => {

              });
          },
          add_collection(){
              // 添加文集
              if(this.collection_name.length<1){
                  this.$message.error("文集名称不能为空！");
                  return;
              }
              // 发送ajax请求
              this.$axios.post(`${this.$settings.Host}/article/collection/`,{
                  name: this.collection_name
              },{
                  headers:{
                      Authorization: "jwt " + this.token,
                  }
              }).then(response=>{
                  this.$message.success("添加文集成功!");
                  this.collection_name = "";
                  this.collection_form = false; // 隐藏添加文集的表单
                  // 把服务端中添加返回的文集信息,保存到collection_list中
                  this.collection_list.unshift(response.data);
              }).catch(error=>{
                  this.$message.error(error.response.data);
              });
          },
          get_collection(){
              // 获取用户的文集列表
              this.$axios.get(`${this.$settings.Host}/article/collection/`,{
                  headers:{
                      Authorization: "jwt " + this.token, // 必须在左边加上 "jwt "，空格！！！
                  }
              }).then(response=>{
                  this.collection_list = response.data;
                  // 获取当前选中文集的文章列表
                  this.get_article_of_collection();
              }).catch(error=>{
                  this.$message.error("对不起,无法获取当前用户的文集列表!");
              });
          },
          get_article_of_collection(){
              // 获取当前文集的文章列表
              this.$axios.get(`${this.$settings.Host}/article/collection/article/`,{
                  params:{
                      collection_id: this.collection_list[this.current_collection].id,
                  },
                  headers:{
                     Authorization:"jwt " + this.token,
                  }
              }).then(response=>{
                  this.article_list = response.data;
              }).catch(error=>{
                  this.$message.error(error.response.data.message);
              })
          },
          add_article(position){
              // 添加文章

              this.$axios.post(`${this.$settings.Host}/article/collection/article/`,{
                  collection: this.collection_list[this.current_collection].id,
                  name: this.get_datetime(),
                  position: position,
              },{
                  headers:{
                      Authorization: "jwt " + this.token,
                  }
              }).then(response=>{
                  this.$message.success("文章添加成功！");
                  // 给本地的aticle追加/插入新建的文章
                  if(position){
                      // 追加
                      this.article_list.push(response.data);
                  }else{
                      // 插入
                      this.article_list.unshift(response.data);
                  }
              }).catch(error=>{
                  this.$message.error("对不起，添加文章失败！");
              });
          },
          get_datetime(){
              // 获取客户端日期格式
              let datetime = new Date();
              let Y = datetime.getFullYear();
              let m = datetime.getMonth()+1;
              m = m<10?"0"+m:m;
              let d = datetime.getDate();
              d = d<10?"0"+d:d;
              return `${Y}-${m}-${d}`;
          },
          pub_article(){
              // 切换文章的发布状态
              let article = this.article_list[this.current_article];
              this.$axios.patch(`${this.$settings.Host}/article/public/${article.id}/`,{},{
                  headers:{
                      Authorization: "jwt "+this.token,
                  }
              }).then(response=>{
                  // 切换成功
                  article.is_public=!article.is_public;
                  // 关闭菜单
                  this.is_show_article_menu = false;
              }).catch(error=>{
                  this.$message.error("切换文章发布状态失败！");
              })
          },
          move_article(collection_id){
              // 移动文章
              this.is_show_article_menu = false;
              let article = this.article_list[this.current_article];
              this.$axios.put(`${this.$settings.Host}/article/public/${article.id}/`,{
                  collection_id, // collection_id: collection_id的简写,
              },{
                  headers:{
                      Authorization: "jwt "+this.token,
                  }
              }).then(response=>{
                  this.article_list.splice(this.current_article,1);
              }).catch(error=>{
                  this.$message.error("移动文章失败！");
              });
          },
          // 绑定@imgAdd event
          imgAdd(pos, $file){
              // 添加文件

          },
          imgDel(pos) {
              // 删除文件

          }
        }
    }
</script>

<style scoped>
  body *{
    box-sizing: border-box;
  }
  .write{
    position: absolute;
    top: 0;
    right: 0;
    left: 0;
    bottom: 0;
    margin: 0;
  }
  ._2v5v5 {
    position: relative;
    height: 100%;
    overflow-y: auto;
    background-color: #404040;
    color: #f2f2f2;
    z-index: 100;
    width: 16.66666667%;
    display: block;
    flex: 0 0 auto;
    float: left;
    padding-right: 0;
    padding-left: 0;
    min-height: 1px;
  }
  ._3zibT {
    padding: 30px 18px 5px;
    text-align: center;
    font-size: 14px;
  }
  ._3zibT a {
    display: block;
    font-size: 15px;
    padding: 9px 0;
    color: #ec7259;
    border: 1px solid rgba(236,114,89,.8);
    border-radius: 20px;
    -webkit-transition: border-color .2s ease-in;
    -o-transition: border-color .2s ease-in;
    transition: border-color .2s ease-in;
  }
  ._1iZMb {
    padding: 0 15px;
    margin-top: 20px;
    margin-bottom: 10px;
    font-size: 14px;
    line-height: 1.5;
  }
  ._1iZMb ._33Zlg {
    cursor: pointer;
    color: #f2f2f2;
    transition: color .2s cubic-bezier(.645,.045,.355,1);
    font-size: 14px;
  }
  ._1iZMb ._33Zlg .fa+span {
    margin-left: 4px;
  }
  ._1iZMb ._2G97m {
    overflow: hidden;
  }
  ._1iZMb ._2a1Rp {
    height: 85px;
    opacity: 1;
    margin-top: 10px;
    transition: all .2s ease-out;
    overflow: hidden;
  }
  ._1CtV4 {
    width: 100%;
    height: 35px;
    color: #ccc;
    background-color: #595959;
    border: 1px solid #333;
    padding: 4px 6px;
    font-size: 14px;
    line-height: 20px;
    outline: 0;
    overflow: visible;
    margin: 10px 0 0;
    margin-bottom: 10px;
  }
._3zXcJ {
    position: relative;
    display: inline-block;
    text-align: center;
    height: 30px;
    line-height: 20px;
    padding: 4px 12px;
    border: 1px solid transparent;
    border-radius: 15px;
    font-size: 14px;
    font-weight: 500;
    -ms-touch-action: manipulation;
    touch-action: manipulation;
    cursor: pointer;
    background-image: none;
    white-space: nowrap;
    user-select: none;
    transition: all .2s cubic-bezier(.645,.045,.355,1);
    text-transform: none;
    color: #42c02e;
    border-color: #42c02e;
    margin-left: 4px;
    background-color: #404040;
  }
  ._3x4X_{
    right: 100%;
    top: 0;
    position: absolute;
  }
  .vIzwB {
    color: #999;
    outline: 0;
  }
  ._1iZMb ._1mU5v {
    height: 0;
    opacity: 0;
    margin-top: 0;
  }
  ._1iZMb ._2a1Rp {
    height: 85px;
    opacity: 1;
    margin-top: 10px;
  }
  ._1iZMb ._1mU5v, ._1iZMb ._2a1Rp {
    transition: all .2s ease-out;
  }
  .vIzwB, .vIzwB:focus, .vIzwB:hover {
    background-color: #404040;
    border-color: transparent;
  }
  .dwU8Q {
      margin-left: 4px;
      background-color: #404040;
  }
._3t059 {
    position: relative;
    z-index: 0;
    background-color: #8c8c8c;
}
._3MbJ4 {
    margin-bottom: 0;
}
._3DM7w {
    position: relative;
    line-height: 40px;
    list-style: none;
    font-size: 15px;
    color: #f2f2f2;
    background-color: #404040;
    padding: 0 15px;
    cursor: pointer;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
}
._31PCv {
    background-color: #666;
    border-left: 3px solid #ec7259;
    padding-left: 12px;

}
._3DM7w ._2VLy- {
    float: right;
}
._3P4JX {
    font-size: 16px;
    width: 40px;
    text-align: center;
    position: relative;
    min-height: 30px;
    max-height: 50px;
}
._3DM7w span {
    display: block;
    margin-right: 20px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
._2w9pn {
    font-size: 14px;
    -webkit-box-shadow: 0 5px 10px rgba(0,0,0,.2);
    box-shadow: 0 5px 10px rgba(0,0,0,.2);
    list-style: none;
    background-color: #fff;
    color: #595959;
    border-radius: 6px;
}
._3P4JX ul._2V8zt {
    display: none;
    position: absolute;
    z-index: 99;
    right: 0;
}
._3P4JX ul._3FcHm {
    top: 100%;
}
._2po2r {
    padding: 10px 20px;
    line-height: 20px;
    white-space: nowrap;
    text-align: left;
    position: relative;
    border-bottom: 1px solid #d9d9d9;
}
._3DM7w:hover, .JUBSP {
    background-color: #666;
}
.h-5Am {
    display: block;
    width: 16.66666667%;
    position: fixed;
    bottom: 0;
    height: 50px;
    line-height: 50px;
    font-size: 15px;
    padding-left: 15px;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    z-index: 150;
    background-color: #404040;
}
.cRfUr {
    border-bottom: 1px solid #d9d9d9;
}
._2po2r:last-child {
    border-radius: 0 0 4px 4px;
    border-bottom: 0;
}
._2po2r:first-child {
    border-radius: 4px 4px 0 0;
}
._2po2r ._22XWG {
    margin-right: 5px;
}
._2po2r:hover {
    background-color: #666;
    color: #fff;
}
._3DM7w span {
    display: block;
    margin-right: 20px;
    overflow: hidden;
    -o-text-overflow: ellipsis;
    text-overflow: ellipsis;
    white-space: nowrap;
}
._3P4JX ul.NvfK4 {
    display: block;
}
._3P4JX ul._2V8zt:before {
    position: absolute;
    right: 12px;
    content: "";
    display: inline-block;
}
._3P4JX ul._3FcHm:before {
    border-left: 9px solid transparent;
    border-right: 9px solid transparent;
    border-bottom: 9px solid #fff;
    top: -9px;
}
.h-5Am .ant-dropdown-trigger {
    display: inline-block;
    color: #999;
    cursor: pointer;
    -webkit-transition: color .2s cubic-bezier(.645,.045,.355,1);
    -o-transition: color .2s cubic-bezier(.645,.045,.355,1);
    transition: color .2s cubic-bezier(.645,.045,.355,1);
}
.h-5Am .fa+span {
    margin-left: 4px;
}
.h-5Am .Yv5Zx {
    float: right;
    margin-right: 15px;
    color: #999;
    cursor: pointer;
  }
  .h-5Am .Yv5Zx i {
      margin-left: 5px;
  }
  .rQQG7{
    height: 100%;
    display: block;
    width: 40%;
    border-right: 1px solid #d9d9d9;
  }
  ._3revO {
    overflow-y: scroll;
    height: 100%;
    position: relative;
  }
  ._3br9T {
    position: relative;
    transition: opacity .3s cubic-bezier(.645,.045,.355,1);
    opacity: 1;
  }
  ._1GsW5 {
    line-height: 20px;
    font-size: 15px;
    font-weight: 400;
    padding: 20px 0 20px 25px;
    cursor: pointer;
    color: #595959;
  }
  ._1GsW5:hover {
    color: #262626;
  }
  ._2TxA- {
    position: relative;
    margin-bottom: 0;
    background-color: #efe9d9;
    border-top: 1px solid #d9d9d9;
  }
  ._25Ilv {
    position: relative;
    height: 90px;
    color: #595959;
    background-color: #fff;
    margin-bottom: 0;
    padding: 15px 10px 15px 60px;
    box-shadow: 0 0 0 1px #d9d9d9;
    border-left: 5px solid transparent;
    list-style: none;
    line-height: 60px;
    cursor: pointer;
    user-select: none;
  }
  ._25Ilv ._2m93u {
    background: url(/static/image/sprite.9d24217.png) no-repeat -50px -25px;
    background-size: 250px;
    position: absolute;
    top: 30px;
    left: 20px;
    width: 22px;
    height: 30px;
  }
  ._1tqbw, ._25Ilv:hover, ._33nt7 {
    background-color: #e6e6e6;
  }
  ._25Ilv ._2m93u {
    background: url(/static/image/sprite.9d24217.png) no-repeat -50px -25px;
    background-size: 250px;
    position: absolute;
    top: 30px;
    left: 20px;
    width: 22px;
    height: 30px;
  }
  ._3P4JX {
    font-size: 16px;
    width: 40px;
    text-align: center;
    position: relative;
    min-height: 30px;
    max-height: 50px;
}
  ._25Ilv .poOXI {
    float: right;
}
  ._33nt7 {
    border-left-color: #ec7259;
  }
  ._25Ilv .hLzJv, ._25Ilv .NariC {
    display: block;
    height: 30px;
    line-height: 30px;
    margin-right: 40px;
    overflow: hidden;
    -o-text-overflow: ellipsis;
    text-overflow: ellipsis;
    white-space: nowrap;
    font-size: 18px;
    font-family: sans-serif;
}
  ._2TxA- {
    position: relative;
    margin-bottom: 0;
    background-color: #efe9d9;
    border-top: 1px solid #d9d9d9;
}
  ._3P4JX ul._2V8zt {
    display: none;
    position: absolute;
    z-index: 99;
    right: 0;
}
  ._3P4JX ul._3FcHm {
    top: 100%;
}
  ._2w9pn {
    font-size: 14px;
    box-shadow: 0 5px 10px rgba(0,0,0,.2);
    list-style: none;
    background-color: #fff;
    color: #595959;
    border-radius: 6px;
}
  ._3P4JX ul.NvfK4 {
    display: block;
}
  ._3P4JX ul._3FcHm:before {
    border-left: 9px solid transparent;
    border-right: 9px solid transparent;
    border-bottom: 9px solid #fff;
    top: -9px;
}
  ._3P4JX ul._2V8zt:before {
    position: absolute;
    right: 12px;
    content: "";
    display: inline-block;
}
._25Ilv ._13kgp {
    position: absolute;
    top: 30px;
    left: 20px;
    width: 22px;
    height: 30px;
    background: url(/static/image/sprite.9d24217.png) no-repeat 0 -25px;
    background-size: 250px;
}
._25Ilv ._13kgp {
    position: absolute;
    top: 30px;
    left: 20px;
    width: 22px;
    height: 30px;
    background: url(/static/image/sprite.9d24217.png) no-repeat 0 -25px;
    background-size: 250px;
}
._25Ilv ._2m93u {
    background: url(/static/image/sprite.9d24217.png) no-repeat -50px -25px;
    background-size: 250px;
}
._25Ilv ._29C-V {
    position: absolute;
    bottom: 2px;
    left: 5px;
    font-size: 9px;
    line-height: 16px;
    color: #595959;
}
._2cVn3 {
    line-height: 30px;
    padding: 20px 0 20px 25px;
    cursor: pointer;
    color: #999;
    margin-bottom: 80px;
}
._24i7u {
    flex-shrink: 0;
    padding: 0 80px 10px 40px;
    margin-bottom: 0;
    border: none;
    font-size: 30px;
    font-weight: 400;
    line-height: 30px;
    box-shadow: none;
    color: #595959;
    background-color: transparent;
    outline: none;
    border-radius: 0;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    position: absolute;
    top: 0;
    right: 0;
    width: 60%;
}
  #editor {
    margin: auto;
    width: 60%;
    position: absolute;
    right: 0;
    top: 44px;
    height: 580px;
  }
  ._2_WAp ._2KzJx, ._2_WAp ._3x4X_ {
    position: absolute;
    right: 100%;
    top: 0;
    display: none;
  }
  ._2_WAp:hover ._2KzJx, ._2_WAp:hover ._3x4X_ {
    display: block;
  }


</style>
