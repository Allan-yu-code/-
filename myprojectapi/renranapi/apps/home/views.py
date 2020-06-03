from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Banner
from django.utils import timezone as datetime
from .serializers import BannerModelSerializer
from renranapi.settings import constants
class BannerListAPIView(ListAPIView):
    serializer_class = BannerModelSerializer
    queryset = Banner.objects.filter(
        is_show=True,
        is_delete=False,
        start_time__lte=datetime.now(),
        end_time__gte=datetime.now()
    ).order_by("orders", "-id")[:constants.HOME_BANNER_LENGTH]


from .models import Nav
from .serializers import NavModelSerializer
class NavHeaderListAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True, is_delete=False, option=1,pid=None).order_by("orders","-id")[:constants.HEADER_NAV_LENGTH]
    serializer_class = NavModelSerializer

class NavFooterListAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True, is_delete=False, option=2,pid=None).order_by("orders","-id")[:constants.FOOTER_NAV_LENGTH]
    serializer_class = NavModelSerializer


from article.models import Article
from .serializers import ArticleModelSerializer
from .paginations import HomeArticlePageNumberPagination
from users.models import User
from renranapi.utils.tablestore import OTS
from renranapi.settings import constants
class ArticleListAPIView(ListAPIView):
    serializer_class = ArticleModelSerializer
    pagination_class = HomeArticlePageNumberPagination

    def get_queryset(self):
        user = self.request.user
        queryset1 = []
        feed_list = []
        my_history_article = []
        ots = OTS()
        if isinstance(user, User):
            """登录用户"""
            # 获取未读池中上一次阅读的主键ID
            result = ots.get_last_id(user.id)
            last_sequence_id=result.get("last_sequence_id")
            my_history_article=[] # 当前用户的浏览器历史
            # 根据上一次推送的主键ID拉去Feed流
            if last_sequence_id is not None:
                import json
                last_id = json.loads(last_sequence_id)
                sequence_id = last_id.get("sequence_id")
                sender_id = last_id.get("sender_id")
                message_id = last_id.get("message_id")
                new_last_id,feed_list = ots.pull_feed(user.id,sequence_id,sender_id,message_id,limit=constants.HOME_ARTICLE_LENGTH)
            else:
                new_last_id,feed_list = ots.pull_feed(user.id,limit=constants.HOME_ARTICLE_LENGTH)

            # 更新未读池中的最后主键ID
            ots.update_last_id(user.id, new_last_id, last_sequence_id)

            """根据用户过往的行为，在数据量不足的情况下推荐内容"""
            if len(feed_list) < constants.HOME_ARTICLE_LENGTH:
                # 1. 获取当前用户最近阅读的文章ID[按时间查询2周内, 按数据量10篇文章]
                ots = OTS()
                my_history_article = ots.get_last_article(user.id)

                # 2. 查询具有相同特征的其他用户
                recomment_user_list = ots.get_recomment_user(user.id, my_history_article)

                # 3. 把其他用户查看过的文章提取出来
                recomement_article_list = ots.get_user_article(recomment_user_list,my_history_article)

                # 4. 和上面Feed流推送的数据量组合成1页
                feed_list+=recomement_article_list
                feed_list=feed_list[:constants.HOME_ARTICLE_LENGTH]

            # 过滤掉已经推送Feeed流过的文章
            feed_list = ots.filter_article_list(user.id, feed_list)
            queryset1 = Article.objects.filter(is_public=True,id__in=feed_list)

            # 把推荐过的数据设置为is_push为 1
            if len(feed_list) > 0:
                ots.update_article_push_status(user.id, feed_list)

        """未登录用户或推荐文章数量不足一页"""
        if len(queryset1) >= constants.HOME_ARTICLE_LENGTH:
            queryset = queryset1
        else:
            queryset2 = Article.objects.exclude( id__in=my_history_article ).filter(is_public=True).order_by("-reward_count", "-comment_count", "-like_count", "-id")
            queryset = queryset2

        return queryset