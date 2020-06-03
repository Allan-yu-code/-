import xadmin

from .models import ArticleCollection
class ArticleCollectionModelAdmin(object):
    """文集"""
    list_display = ["id","name"]
    list_editable = ["name"]
xadmin.site.register(ArticleCollection,ArticleCollectionModelAdmin)


from .models import Article
class ArticleModelAdmin(object):
    """文章"""
    list_display=["id","name"]
xadmin.site.register(Article, ArticleModelAdmin)