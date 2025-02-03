from django.db import models

# Create your models here.

class item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=300, default='None')
    stock = models.IntegerField(default=0)