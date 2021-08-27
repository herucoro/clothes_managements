from rest_framework import viewsets
from .models import Order, History
from .serializers import OrderSerializer, HistorySerializer

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

