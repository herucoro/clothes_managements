from django.conf.urls import url, include
from rest_framework import fields, serializers
from .models import *

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('order_number', 'user_id', 'delivery_date')


class HistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = History
        fields = ('order', 'seazon', 'size', 'kinds_of_clothes', 'quantity')
