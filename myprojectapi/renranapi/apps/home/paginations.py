from rest_framework.pagination import PageNumberPagination
from renranapi.settings import constants
class HomeArticlePageNumberPagination(PageNumberPagination):
    """首页推送文章的分页器"""
    page_query_param = "page"                   # 地址上面代表页码的参数名
    max_page_size = 20                          # 每一页显示的最大数据量
    page_size = constants.HOME_ARTICLE_LENGTH   # 默认每一页显示的数据量
    page_size_query_param = "size"              # 地址上面代表数据量的参数名