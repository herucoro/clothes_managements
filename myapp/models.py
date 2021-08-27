from django.db import models

# Create your models here.


class Order(models.Model):
    order_number = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    delivery_date = models.DateField(null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return '注文番号:' + str(self.order_number) + ' / 社員番号:' + str(self.user_id)

class History(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    seazon = models.CharField(max_length=1)
    size = models.CharField(max_length=2)
    kinds_of_clothes = models.CharField(max_length=1)
    quantity = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)    