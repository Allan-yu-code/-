from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path,re_path
from . import views
urlpatterns = [
    path("login/", obtain_jwt_token ),
    path("captcha/", views.CaptchaAPIView.as_view()),
    re_path("^sms/(?P<mobile>1[3-9]\d{9})/$", views.SMSCodeAPIView.as_view()),
]

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("",views.UserAPIView)
urlpatterns+=router.urls