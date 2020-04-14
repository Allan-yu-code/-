from django.urls import path
from . import views
urlpatterns = [
    path("qq/url/", views.OAuthQQUserAPIView.as_view({"get":"get_url"})),
    path("qq/info/", views.OAuthQQUserAPIView.as_view({
        "get":"get_info",
        "put":"qq_login",
        "post":"qq_register",
    })),
]