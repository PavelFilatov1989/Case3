from django.urls import path
from .views import *

urlpatterns = [
    path('', shop_index, name='index'),
    path('products/', products_list, name='products'),
    path('orders/', orders_list, name='orders'),
]