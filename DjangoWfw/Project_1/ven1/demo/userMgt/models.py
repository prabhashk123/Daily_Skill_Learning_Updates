from django.db import models
from django.contrib.auth.models import User
# signals model
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    address=models.TextField(max_length=500)
    photo=models.ImageField(null=True, blank=False,upload_to='cus_pic')
    date_of_birth=models.DateField(null=True, blank=False)
    created_date=models.DateTimeField(auto_now_add=True) 
    updated_date=models.DateTimeField(auto_now=True)
# one to relationship Cutomer and user
    user=models.OneToOneField(User,on_delete=models.CASCADE)

# signals in django like post_save
@receiver(sender=User,signal=post_save)
def receiver_user_post_save(sender,instance,created,*args,**kwargs):
    # sender class name from where we are getting signal here class name is User like model class is sender
    #instance: object of new save record mens here user class ka hi object aayega
    # created: boolean value True meanse inserted and False means updated
        pass