from rest_framework import serializers
from .models import ArticleCollection
class CollectionModelSerializer(serializers.ModelSerializer):
    """文集序列化器"""
    class Meta:
        model = ArticleCollection
        fields = ["id","name"]

    def validate_name(self, name):
        """验证数据"""
        # 如果当前有用户曾经过同一个文集,则报错
        # print(self.context)  # 字典  {request:对象,view:对象,data_format: 字符串}
        user = self.context["request"].user
        ret = ArticleCollection.objects.filter(user=user, name=name).all()
        if len(ret)>0:
            raise serializers.ValidationError("对不起, 当前文集名称已经被使用!~")

        return name

    def create(self, validated_data):
        """添加数据"""
        try:
            collection = ArticleCollection.objects.create(
                name=validated_data.get("name"),
                user=self.context["request"].user,
                orders=0,
            )
            return collection
        except:
            raise serializers.ValidationError("对不起, 添加文集失败!~")

    def update(self, instance, validated_data):
        """更新数据"""
        instance.name = validated_data.get("name")
        instance.save()
        return instance

from .models import Article
class ArticleModelSerializer(serializers.ModelSerializer):
    """文章模型序列化器"""
    position = serializers.IntegerField(write_only=True, default=0, allow_null=True, label="添加文章的位置", help_text="在文章列表的前面插入添加则为0, 在文章列表的后面追加添加则为1")
    class Meta:
        model = Article
        fields = ["id","position","name","content","html_content","collection","pub_date","is_public"]
        read_only_fields = ["id","content","html_content","pub_date","is_public"]

    def validate(self, data):
        name = data.get("name")
        if len(name)<1:
            raise serializers.ValidationError("对不起，文章标题不能为空！")

        return data

    def create(self, validated_data):
        """添加文章"""
        try:
            article = Article.objects.create(
                name=validated_data.get("name"),
                user=self.context["request"].user,
                content="",
                html_content="",
                collection=validated_data.get("collection"),
                is_public=False,
                is_show=True,
                orders=0
            )
        except:
            raise serializers.ValidationError("对不起，文章添加失败！")

        if validated_data.get("position"):
            """
            如果用户设置在文章列表后面追加添加文章，则让文章的排序值跟着id来变化越来越大
            排序值越大的文章，越往后排列
            """
            article.orders = article.id
            article.save()

        return article


