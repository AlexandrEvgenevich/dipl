from django.db import models
from django.contrib.auth.models import User

class Shop(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(blank=True, null=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)

class Product(models.Model):
    name = models.CharField(max_length=100)

class ProductInfo(models.Model):
    product = models.ForeignKey(Product, related_name='product_info', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    shop = models.ForeignKey(Shop, related_name='products', on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE)

class OrderItems(models.Model):
    order = models.ForeignKey(Order, related_name='item', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    item_quantity = models.PositiveIntegerField(blank=False, null=False)