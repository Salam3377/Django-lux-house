from django.db import models

class Menu(models.Model):
    name= models.CharField(max_length= 100)
    price= models.CharField(max_length = 100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.price} {self.description}"
    
    def as_dict(self):
        """Returns dictionary version of Menu models"""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description
        }

