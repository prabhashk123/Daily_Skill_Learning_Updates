from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=100)
    select=models.CharField(max_length=50)
    query=models.CharField(max_length=200)
