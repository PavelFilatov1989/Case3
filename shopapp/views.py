from django.shortcuts import render
from .models import *

def shop_index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'shopapp/index.html', data)


def products_list(request):
    products = Product.objects.all()
    data = {
        'title': 'Товары',
        'products': products,
    }

    return render(request, 'shopapp/products.html', context=data)


def orders_list(request):
    orders = Order.objects.all().prefetch_related('products').select_related('user_id')
    data = {
        'title': 'Заказы',
        'orders': orders,
    }
    return render(request, 'shopapp/orders.html', context=data)
