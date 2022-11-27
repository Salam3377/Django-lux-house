from django.db import models



class Product(models.Model):

    name = models.CharField(max_length=150, db_index=True)
    #slug = models.CharField(max_length=150, db_index=True, unique=True)
    #image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1000, blank=True)
    #available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    uploaded = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.name
    
    def as_dict(self):
        """Returns dictionary version of Menu models"""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
        }
