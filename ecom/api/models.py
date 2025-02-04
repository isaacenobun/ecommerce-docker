from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class AdminUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email

class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=300, default='None')
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name