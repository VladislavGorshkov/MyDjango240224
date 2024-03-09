from django.db import models

# Create your models here.

class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   count = models.PositiveIntegerField() 
   info = models.TextField(max_length=200, default="Нет описания")

def __rep__(self) -> str:
   return f'Item({self.name}, {self.brand}, {self.count} )'