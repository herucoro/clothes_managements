from myapp.serializers import HistorySerializer
from django.conf.urls import url, include
from rest_framework import routers, urlpatterns
from .views import OrderViewSet, HistoryViewSet

router = routers.DefaultRouter()
router.register(r'order', OrderViewSet)
router.register(r'history', HistoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),    
]