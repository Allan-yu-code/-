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

        article.is_public = not article.is_public
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