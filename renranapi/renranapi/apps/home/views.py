from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Banner
from datetime import datetime
from .serializers import BannerModelSerializer
from renranapi.settings import constants
class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(
        is_show=True,
        is_delete=False,
        start_time__lte=datetime.now(),
        end_time__gte=datetime.now()
    ).order_by("orders","-id")[:constants.HOME_BANNER_LENGTH]
    serializer_class = BannerModelSerializer