from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.

class userProfile(models.Model):
    userInfo= models.OneToOneField(User,on_delete=models.CASCADE)
    favoriteProducts=models.ManyToManyField(Product)
    # carts=models.ManyToManyField(Product)
    address= models.CharField(max_length=100)
    address2= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    state= models.CharField(max_length=100)
    zipCode=models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.userInfo.username