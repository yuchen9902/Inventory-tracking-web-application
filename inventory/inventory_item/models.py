from itertools import product
from pyexpat import model
from unicodedata import category
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)



