from rest_framework import serializers
from .models import Banner
class BannerModelSerializer(serializers.ModelSerializer):
    """轮播图序列化器"""
    class Meta:
        model = Banner
        fields = ["image","link","is_http"]

from .models import Nav
class NavModelSerializer(serializers.ModelSerializer):
    """导航菜单序列化器"""
    class Meta:
        model = Nav
        fields = ["name","link","is_http","son_list"]

from article.models import Article
from users.models import User
class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id","nickname"]
        model = User
class ArticleModelSerializer(serializers.ModelSerializer):
    user = AuthorModelSerializer()
    class Meta:
        model = Article
        fields = ["id","name","html_content","user","like_count","reward_count","comment_count"]