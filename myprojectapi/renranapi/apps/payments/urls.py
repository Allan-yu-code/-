from django.urls import path
from . import views
urlpatterns = [
    path("alipay/", views.AliPayAPIView.as_view()),
    path("alipay/result/", views.AliPayResultAPIView.as_view()),
]