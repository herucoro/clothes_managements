from myapp.serializers import HistorySerializer
# from django.conf.urls import url, include
from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import *

router = routers.DefaultRouter()
router.register(r'order', OrderViewSet)
router.register(r'history', HistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),    
]