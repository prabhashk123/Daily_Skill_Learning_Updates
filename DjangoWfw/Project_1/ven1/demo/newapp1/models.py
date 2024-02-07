import re
from django.db import models
from django.core.exceptions import ValidationError
#validation
def my_mobile_validetor(value):
# for tow digit find use slice method [0:2]
    if value[0:2]!="99":
        raise ValidationError("only number should start at 99")
def my_mobile_validetor2(value):
    if value[len(value)-2:len(value)]!="99":
        raise ValidationError("only number should endwith 99")
# def mobile(value):
#     p=re.compile(r'\d(10,11)')
#     m=p.match(value)
#     if m==p:
#         raise ValidationError("please enter only 11 digit")

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    mobile_no=models.CharField(max_length=15,validators=[my_mobile_validetor,my_mobile_validetor2])
    email_id=models.CharField(max_length=100)

