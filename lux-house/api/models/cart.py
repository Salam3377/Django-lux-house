from django.db import models
from .menu import Menu

class Cart(models.Model):
    item = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='item_to_cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.item} , added'
