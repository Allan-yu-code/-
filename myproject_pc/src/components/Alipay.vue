<template>

</template>

<script>
    export default {
        name: "Alipay",

        created(){
            this.resultHandler();
        },
        methods:{
            resultHandler(){
                this.token = sessionStorage.user_token || localStorage.user_token;
                // 支付结果转发服务器
                if(this.$route.query.out_trade_no){
                  // 转发支付结果到服务端
                  this.$axios.get(`${this.$settings.Host}/payments/alipay/result/`+location.search,{
                    headers:{
                      Authorization: "jwt " + this.token,
                    }
                  }).then(response=>{
                    this.$message.success(response.data.message);
                    this.$router.push(`/article/${response.data.article}`);
                  }).catch(error=>{
                    this.$message.error("支付结果处理有误！请及时联系客服工作人员！");
                  });
                }
            }
        }
    }
</script>

<style scoped>

</style>
