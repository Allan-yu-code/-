from django.urls import path,re_path
from . import views
urlpatterns = [
    path("table/", views.TableAPIView.as_view()),
    path("data/", views.DataAPIView.as_view()),
    path("row/", views.RowAPIView.as_view()),
]