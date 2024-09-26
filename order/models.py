from django.db import models
from datetime import datetime
from products.models import Product
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    totalPrice=models.DecimalField(max_digits=6, decimal_places=2)
    quantity=models.PositiveIntegerField()
    date=models.DateTimeField(default=datetime.now())
    is_delivered=models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username 
    
    class Meta:
        ordering=['user']
    