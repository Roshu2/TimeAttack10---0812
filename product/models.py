from django.db import models
from user.models import User
# Create your models here.


class Product(models.Model):
    name = models.CharField(verbose_name="상품명", max_length=70)
    description = models.TextField(verbose_name="상품 설명", max_length=500)
    price = models.IntegerField(verbose_name="가격")
    start_date = models.DateTimeField(verbose_name="도입일")
    is_active = models.BooleanField(verbose_name="활성화 여부", default=True)
    
    class Meta:
        db_table = "products"

class Subscribe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    purchase_date = models.DateTimeField(verbose_name="구매일", auto_now_add=True)
    subscribe_start = models.DateTimeField(verbose_name="구독 시작일", auto_now_add=True)
    subscribe_end = models.DateTimeField(verbose_name="구독 종료일")
    
    class Meta:
        db_table = "subscribes"