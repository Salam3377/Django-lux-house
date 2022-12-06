from django.db import models
from django.conf import settings


class Product(models.Model):
    name= models.CharField(max_length= 30)
    price= models.CharField(max_length = 15)
    description = models.CharField(max_length=255)
    menu_type = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.price} {self.description} {self.menu_type}"
    
    def as_dict(self):
        """Returns dictionary version of Menu models"""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'menu_type': self.menu_type,
            'image' : self.image,
        }

