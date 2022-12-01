from django.db import models
from .product import Product
from .menu import Menu
from django.conf import settings
from django.contrib.postgres.fields import ArrayField

class Cart(models.Model):
    product = models.ManyToManyField(Menu, related_name='products')# multiple products many to many
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner')
    # owner user


    def __str__(self):
        return f'{self.product}'
    
