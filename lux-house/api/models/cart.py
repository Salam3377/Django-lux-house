from django.db import models

from .menu import Product
from django.conf import settings
from django.contrib.postgres.fields import ArrayField

class Cart(models.Model):
    product = models.ManyToManyField(Product, related_name='products')# multiple products many to many
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner')
    # owner user


    def __str__(self):
        return f'{self.product}'
    
