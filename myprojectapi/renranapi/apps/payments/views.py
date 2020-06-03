from django.shortcuts import render
import random
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.utils import timezone as datetime
from django.conf import settings
from .models import Reward
from article.models import Article
from alipay import AliPay
from django.db import transaction


# Create your views here.
class AliPayAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @classmethod
    def alipay(cls):
        # 初始化sdk对象
        app_private_key_string = open(settings.ALIAPY["app_private_key_path"]).read()
        alipay_public_key_string = open(settings.ALIAPY["alipay_public_key_path"]).read()
        alipay = AliPay(
            appid=settings.ALIAPY["appid"],
            app_notify_url=settings.ALIAPY["app_notify_url"],  # 默认回调url
            app_private_key_string=app_private_key_string,
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            alipay_public_key_string=alipay_public_key_string,
            sign_type=settings.ALIAPY["sign_type"],
            debug=settings.ALIAPY["debug"]  # 默认False
        )
        return alipay

    def post(self, request):
        """生成支付的链接地址"""
        # 创建打赏记录
        user = request.user
        trade_no = datetime.now().strftime("%Y%m%d%H%M%S") + ("%06d" % user.id) + ("%06d" % random.randint(1, 999999))
        try:
            article = Article.objects.get(pk=request.data.get("article_id"),is_public=True,is_show=True,is_delete=False)
        except Article.DoesNotExist:
            return Response({"message":"对不起，当前打上的文章不存在！"}, status=status.HTTP_400_BAD_REQUEST)

        reward = Reward.objects.create(
            user=user,
            money=request.data.get("money"),
            article=article,
            status=False,
            trade_no=trade_no,
            out_trade_no=None,
            reward_type=request.data.get("type"),
            message=request.data.get("message"),
        )
        if reward.reward_type == 1:
            """支付宝支付"""

            # 生成支付地址
            order_string = self.alipay().api_alipay_trade_page_pay(
                out_trade_no=reward.trade_no,           # 订单号
                total_amount=float(reward.money),       # 订单金额
                subject="打赏文章《%s》" % article.name,  # 订单标题
                return_url=settings.ALIAPY["return_url"], # 同步回调地址
                notify_url=settings.ALIAPY["notify_url"]  # 异步回调地址
            )

            url = settings.ALIAPY["gateway_url"] + order_string

        else:
            url = ""

        return Response(url)

from rest_framework.views import APIView
from django.http.response import HttpResponse
from rest_framework import status
import logging

logger = logging.getLogger("django")

class AliPayResultAPIView(APIView):
    def get(self,request):
        """处理同步支付结果"""
        data = request.query_params.dict()
        signature = data.pop("sign")
        success = AliPayAPIView.alipay().verify(data, signature)
        if success:
            """结果正确"""
            data,status_code=self.result(data)
            return Response(data,status_code)
        else:
            return Response({"message": "参数异常，支付失败！"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        """处理异步支付结果"""
        data = request.data.dict()
        signature = data.pop("sign")
        success = AliPayAPIView.alipay().verify(data, signature)
        if success and data["trade_status"] in ("TRADE_SUCCESS", "TRADE_FINISHED" ):
            # 赞赏处理
            data,status = self.result(data)
            if status==200:
                """处理成功"""
                return HttpResponse("success")
            else:
                """处理失败，记录日志"""
                logger.error("支付宝异步通知处理失败！支付宝返回信息：%s" % data)
                return HttpResponse("fail")

    def result(self,data):
        with transaction.atomic():
            # 设置事务的回滚点,用于指定在事务失败时,在哪一部分的SQL语句无效
            save_id = transaction.savepoint()
            try:
                # 修改打赏记录的状态为已付款
                reward = Reward.objects.get(
                    trade_no=data.get("out_trade_no"),
                    status=False,
                )
                reward.status = True
                reward.out_trade_no = data.get("trade_no")
                reward.save()

                # 增加文章的打赏人数
                reward.article.reward_count += 1
                reward.article.save()

                # 给文章作者的资产增加打赏的资金
                reward.article.user.money = int((reward.article.user.money + reward.money) * 100) / 100
                reward.article.user.save()

                # 参考打赏，实现一个资金流水记录[专门显示在钱包位置]
            except Reward.DoesNotExist:
                transaction.savepoint_rollback(save_id)
                return {"message": "订单已经完成了，请不要重复刷新本次页面"}, status.HTTP_400_BAD_REQUEST
            except:
                transaction.savepoint_rollback(save_id)
                return {"message": "支付结果处理有误！"}, status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "支付处理成功!", "article": reward.article.id}, status.HTTP_200_OK