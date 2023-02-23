from django.shortcuts import render
from .models import Product, Order, OrderItems
from .serializers import ProductSerializer, OrderItems, GetOrdersSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User

class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        users = User.objects.all()
        if str(request.data['username']) in str(users):
            return Response({request.data['username']: 'user with same name already registered'})
        if str(request.data['password1']) != str(request.data['password2']):
            return Response('passwords do not match')

        user = User.objects.create_user(
            username=request.data['username'],
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            email=request.data['email'],
            is_active=True
        )
        user.set_password(request.data['password1'])
        user.save()
        return Response({request.data['username']: 'created'})

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request):
        if str(request.data['new_password1']) != str(request.data['new_password2']):
            return Response('passwords do not match')

        user = User.objects.get(username=self.request.user)
        user.set_password(request.data['new_password1'])
        user.save()

        return Response('password_changed')

class ShowProductsView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, read_only=True)
        return Response(serializer.data)

class CreateOrderView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = User.objects.get(username=self.request.user)
        order = Order.objects.create(user_id=user.id)
        for key, val in list(request.data.items()):
            OrderItems.objects.create(order=order, item_name=key, item_quantity=val)

        return Response('order_created')

class ShowOrdersView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = User.objects.get(username=self.request.user)
        orders = Order.objects.filter(user_id=user.id)
        serializer = GetOrdersSerializer(orders, many=True, read_only=True)
        return Response(serializer.data)


class UpdateOrderView(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request):
        pass

