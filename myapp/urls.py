from myapp.serializers import HistorySerializer
# from django.conf.urls import url, include
from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import *

router = routers.DefaultRouter()
router.register('order', OrderViewSet)
router.register('history', HistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),    
]