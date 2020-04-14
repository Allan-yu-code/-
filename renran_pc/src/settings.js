export default {
  Host:"http://api.renran.cn:8000", // ajax的服务端地址
  Website: "荏苒网",
  TC_captcha:{　// 防水墙验证码配置
    app_id: "2072894469",
  },
  check_user_login(vm,title="警告",content="您尚未登录！", confirm_text="跳转到首页", confirm_url="/"){
    // 验证用户是否已经登录了
    vm.token = localStorage.user_token || sessionStorage.user_token;
    if(vm.token){
      // 已经登录
      return vm.token;
    }else{
      // 没有登录
     vm.$confirm(content, title, {
        confirmButtonText: confirm_text,
        cancelButtonText: '返回上一页',
        type: 'warnning'
      }).then(() => {
        vm.$router.push(confirm_url);
      }).catch(() => {
        vm.$router.go(-1);
      });
    }
  }
}
