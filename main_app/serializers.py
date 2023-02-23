from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Product, ProductInfo, Order, OrderItems

class ProductInfoSerializer(ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = ['quantity', 'price', 'shop']

class ProductSerializer(ModelSerializer):
    product_info = ProductInfoSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['name', 'product_info']

class OrderItemsSerializer(ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ['item_name', 'item_quantity']

class CreateOrderSerializer(ModelSerializer):
    order_items = OrderItemsSerializer(many=True)
    class Meta:
        model = Order
        fields = ['user', 'order_items']

class GetOrdersSerializer(ModelSerializer):
    items = OrderItemsSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'items']

