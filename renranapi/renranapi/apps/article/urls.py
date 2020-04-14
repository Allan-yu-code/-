from django.urls import path,re_path
from . import views
urlpatterns = [
    path("collection/", views.CollecionAPIView.as_view()),
    re_path("^collection/(?P<pk>\d+)/$", views.CollecionAPIView.as_view()),
    path("collection/article/", views.ArticleOfCollectionAPIView.as_view()),
    re_path("^public/(?P<pk>\d+)/$", views.ArticleAPIView.as_view()),
]