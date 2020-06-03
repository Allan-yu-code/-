# Create your views here.

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import ArticleCollection
from .serializers import CollectionModelSerializer

class CollecionAPIView(ListAPIView,CreateAPIView, UpdateAPIView):
    serializer_class = CollectionModelSerializer
    permission_classes = [IsAuthenticated]  # 必须是登陆用户才能访问过来

    def get_queryset(self):
        user = self.request.user
        ret = ArticleCollection.objects.filter(user=user).order_by("orders", "-id")
        if len(ret) < 1:
            # 如果没有文集, 给用户默认创建2个文集
            collection1 = ArticleCollection.objects.create(
                user=user,
                name="日记本",
                orders=1,
            )

            collection2 = ArticleCollection.objects.create(
                user=user,
                name="随笔",
                orders=2,
            )

            ret = [
                collection1,
                collection2,
            ]

        return ret

from rest_framework.generics import ListAPIView
from .serializers import ArticleModelSerializer
from .models import Article
from rest_framework.response import Response
from rest_framework import status
class ArticleOfCollectionAPIView(ListAPIView, CreateAPIView):
    """文集下的文章"""
    serializer_class = ArticleModelSerializer
    permission_classes = [IsAuthenticated]  # 必须是登陆用户才能访问过来

    def list(self, request,  *args, **kwargs):
        user = request.user
        collection_id = request.query_params.get("collection_id")
        try:
            ArticleCollection.objects.get(pk=collection_id)
        except ArticleCollection.DoesNotExist:
            return Response({"message":"错误的文集ID"}, status=status.HTTP_400_BAD_REQUEST)

        queryset = Article.objects.filter(user=user,collection_id=collection_id).order_by("orders", "-id")
        queryset = self.filter_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

from rest_framework.views import APIView
class ArticleAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self,request,pk):
        """切换文章的发布状态"""
        try:
            article = Article.objects.get(user=request.user,pk=pk)
        except Article.DoesNotExist:
            return Response({"message":"当前文章不存在！"}, status=status.HTTP_400_BAD_REQUEST)

        # 判断如果是取消发布，则取消定时发布
        # 1. 定时发布
        if article.is_public == False and article.pub_date is not None:
            # 原来定时发布的，现在取消
            article.pub_date = None
        elif article.is_public == False and article.pub_date is None:
            # 原来没有发布的，现在立即发布
            article.is_public = True
            # 添加Feed流推送
            ots = OTS()
            follow_list = ots.get_follow_list(article.user.id)
            ret = ots.push_feed(article.user.id, follow_list, article.id)

        elif article.is_public == True:
            # 原来发布的，现在取消
            article.is_public = False

        article.save()

        return Response(status=status.HTTP_200_OK)

    def put(self,request,pk):
        """移动文章"""
        try:
            article = Article.objects.get(user=request.user, pk=pk)
        except Article.DoesNotExist:
            return Response({"message": "当前文章不存在！"}, status=status.HTTP_400_BAD_REQUEST)

        collection_id = request.data.get("collection_id")
        try:
            collection = ArticleCollection.objects.get(user=request.user, pk=collection_id)
        except ArticleCollection.DoesNotExist:
            return Response({"message": "当前文集不存在！"}, status=status.HTTP_400_BAD_REQUEST)

        article.collection = collection
        article.save()

        return Response(status=status.HTTP_200_OK)

class ArticleIntervalAPIView(UpdateAPIView):
    """定时发布文章"""
    permission_classes = [IsAuthenticated]
    def put(self,request,pk):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response("对不起,当前文章不存在!", status=status.HTTP_400_BAD_REQUEST)

        pub_date = request.data.get("pub_date")
        article.pub_date = pub_date
        article.save()
        return Response("操作成功!")

class ArticleInfoAPIView(APIView):
    """文章内容保存视图接口"""
    permission_classes = [IsAuthenticated]
    def put(self,request,pk):
        try:
            article = Article.objects.get(pk=pk,user=request.user)
        except Article.DoesNotExist:
            return Response("对不起,当前文章不存在!", status=status.HTTP_400_BAD_REQUEST)

        name = request.data.get("name")
        content = request.data.get("content")
        html_content = request.data.get("html_content")
        if len(name) > 1:
            article.name = name
        if len(content) > 1:
            article.content = content
        if len(html_content) > 1:
            article.html_content = html_content
        article.save()
        return Response(status=status.HTTP_200_OK)

from .models import ArticleImage
from .serializers import ArticleImageModelSerializer
class ArticleImageAPIView(CreateAPIView):
    """文章图片上传接口"""
    queryset = ArticleImage.objects.all()
    serializer_class = ArticleImageModelSerializer
    permission_classes = [IsAuthenticated]

from .models import Special,SpecialArticle
from .serializers import SpecialModelSerializer
class SpecialListAPIView(ListAPIView):
    serializer_class = SpecialModelSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset= Special.objects.filter(manager_list__user=user,manager_list__is_delete=False, manager_list__is_show=True).order_by("orders","-id")
        # 接受当前发布的文章ID，和每一个专题进行关系的判断，是否收录了当前文章
        article_id = request.query_params.get("article_id")
        for special in queryset:
            try:
                ret = SpecialArticle.objects.get(article_id=article_id,special=special)
                special.status = ret.status
            except SpecialArticle.DoesNotExist:
                special.status=-1 # 没有投稿/收录记录

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

from .models import Special,SpecialArticle
class PostArticleAPIView(APIView):
    """文章投稿的api接口"""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """文章投稿"""
        user = request.user
        article_id = request.data.get("article_id")
        special_id = request.data.get("special_id")

        # 验证文章是否存在
        try:
            article = Article.objects.get(user=user, pk=article_id)
        except Article.DoesNotExist:
            return Response({"message":"对不起, 当前文章不存在!"}, status=status.HTTP_400_BAD_REQUEST)

        # 验证专题是否存在
        try:
            special = Special.objects.get(pk=special_id)
        except Special.DoesNotExist:
            return Response({"message":"对不起, 当前专题不存在!"}, status=status.HTTP_400_BAD_REQUEST)

        # 判断当前文章是否向专题投稿
        try:
            special_article = SpecialArticle.objects.get(special=special, article=article)
            if special_article.status == 0 or special_article.status == 1:
                return Response({"message":"对不起, 当前文章已经投稿了，或在审核中!"}, status=status.HTTP_400_BAD_REQUEST)
            elif special_article.status == 2:
                return Response({"message":"对不起, 当前文章已经被收录，不能重复投稿!"}, status=status.HTTP_400_BAD_REQUEST)
            elif special_article.status == 3:
                """之前审核没通过，继续投稿"""
                special_article.status=1
                special_article.save()
                return Response({"message":"文章重新投稿成功!","status":1}, status=status.HTTP_200_OK)

        except SpecialArticle.DoesNotExist:
            special_article = SpecialArticle.objects.create(
                special=special,
                article=article,
                status=1,
            )

            if special.user == user:
                """如果当前投稿用户是当前专题的管理员，则默认跳过审核阶段"""
                special_article.status = 2
                special_article.user = user
                return Response({"message": "投稿成功!","status":2}, status=status.HTTP_200_OK)

            return Response({"message":"投稿成功!","status":1}, status=status.HTTP_200_OK)

from rest_framework.generics import RetrieveAPIView
from .serializers import ArticleInfoModelSerializer
from users.models import User
from renranapi.utils.tablestore import OTS
class ArticleRetrieveAPIView(RetrieveAPIView):
    """文章详情信息"""
    serializer_class = ArticleInfoModelSerializer
    queryset = Article.objects.filter(is_public=True)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        visitor = request.user # 如果客户端有发送jwt，并且jwt是正确有效的，request.user就能获取到当前登录访问者
        author  = instance.user
        # 访问者是否关注了文章作者的状态，默认没有关注
        instance.focus = False
        if isinstance(visitor,User):
            """如果用户已经登录了，则判断用户是否关注了文章作者"""
            #　根据主键ID查询tablestore的1条数据
            ots = OTS()
            ret = ots.check_user_focus(author.id, visitor.id)
            if len(ret) > 0:
                """存在关注记录"""
                instance.focus = True

            # tablestore添加用户的阅读记录
            ots.update_article_read_status(visitor.id, instance.id)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from users.models import User
from rest_framework.response import Response
from rest_framework import status
class UserFocusAPIView(APIView):
    """关注和取消关注"""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # 关注者[粉丝]
        user = request.user
        # 作者
        author_id = request.data.get("author_id")

        try:
            author = User.objects.get(pk=author_id)
        except User.DoesNotExist:
            return Response({"message": "对不起, 您关注的作者不存在!"}, status=status.HTTP_400_BAD_REQUEST)

        # 获取关注状态[False表示取消关注,True表示关注]
        focus = request.data.get("focus")
        ots = OTS()
        ots.focus_author(author_id, user.id, focus)
        return Response({"message":"OK"})