from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    content = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.SmallIntegerField()
    created = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)


class Order(models.Model):
    comments = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=100,)
    create = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,)
    products = models.ManyToManyField(Product)