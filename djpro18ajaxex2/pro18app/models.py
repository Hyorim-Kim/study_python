# models.py
from django.db import models

class Product(models.Model):
    category = models.CharField(max_length=50)
    pname = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    description = models.CharField(max_length=50)
