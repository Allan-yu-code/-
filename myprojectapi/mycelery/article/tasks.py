from mycelery.main import app
from article.models import Article
from datetime import datetime
@app.task(name="interval_pub_article")
def interval_pub_article():
    """定时发布文章"""
    article_list = Article.objects.exclude(pub_date=None)
    for article in article_list:
        pub_date_timestamp = int(article.pub_date.timestamp())
        current_timestamp = int(datetime.now().timestamp() +8 * 60 * 60)
        if pub_date_timestamp <= current_timestamp:
            article.pub_date = None
            article.is_public = True
            # todo 添加Feed流推送
            article.save()