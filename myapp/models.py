from django.db import models

# Create your models here.


class Order(models.Model):
    order_number = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)


class History(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    seazon = models.CharField(max_length=1)
    size = models.IntegerField()
    quantity = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
