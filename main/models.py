from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.

class Items(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('accessories', 'Accessories'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    @property
    def is_in_stock(self):
        return self.stock > 0
    
    def reduce_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            self.save()
        else:
            raise ValueError("Not enough stock available")
        
    def get_thumbnail(self):
        if self.thumbnail == None or self.thumbnail == '':
            if self.category == 'jersey':
                return '/static/images/jersey.png'
            elif self.category == 'shoes':
                return '/static/images/shoes.png'
            elif self.category == 'accessories':
                return '/static/images/accessories.png'
        else:
            return self.thumbnail

    

