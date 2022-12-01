from django.db import models
from django.conf import settings


class Product(models.Model):

    name = models.CharField(max_length=150, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    uploaded = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.name
    
    # def as_dict(self):
    #     """Returns dictionary version of Menu models"""
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'price': self.price,
    #         'description': self.description,
    #     }
