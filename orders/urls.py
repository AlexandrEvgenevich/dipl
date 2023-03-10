"""orders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main_app.views import RegisterUserView, ShowProductsView, CreateOrderView,\
    ShowOrdersView, UpdateOrderView, ChangePasswordView

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register_user/', RegisterUserView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    path('user_login/', obtain_auth_token),
    path('show_products/', ShowProductsView.as_view()),
    path('create_order/', CreateOrderView.as_view()),
    path('show_orders/', ShowOrdersView.as_view()),
    path('update_order/', UpdateOrderView.as_view())
]
