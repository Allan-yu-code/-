from django.urls import path,re_path
from . import views
urlpatterns = [
    path("collection/", views.CollecionAPIView.as_view()),
    re_path("^collection/(?P<pk>\d+)/$", views.CollecionAPIView.as_view()),
    path("collection/article/", views.ArticleOfCollectionAPIView.as_view()),
    re_path("^public/(?P<pk>\d+)/$", views.ArticleAPIView.as_view()),
    re_path("^interval/(?P<pk>\d+)/$", views.ArticleIntervalAPIView.as_view()),
    re_path("^(?P<pk>\d+)/$", views.ArticleInfoAPIView.as_view()),
    path("image/", views.ArticleImageAPIView.as_view()),
    path("special/", views.SpecialListAPIView.as_view()),
    path("post/", views.PostArticleAPIView.as_view()),
    re_path("^retrieve/(?P<pk>\d+)/$", views.ArticleRetrieveAPIView.as_view()),
    path("focus/", views.UserFocusAPIView.as_view()),
]