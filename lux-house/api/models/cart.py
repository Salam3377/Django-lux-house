from django.db import models
from .product import Product
from .menu import Menu
from django.conf import settings
from django.contrib.postgres.fields import ArrayField

class Cart(models.Model):
    product = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='products')



    def __str__(self):
        return f'{self.product}'
    
