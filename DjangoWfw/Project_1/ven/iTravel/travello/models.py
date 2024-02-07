from django.db import models

# Create your models here.
# (1)creat class name destination with five attributes
# class Destination:
#     id:int
#     name:str
#     image:str
#     desc:str
#     price:int

# # Model is class name and models is module class Destination for database
class Destination(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

