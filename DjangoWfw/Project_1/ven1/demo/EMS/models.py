from django.db import models

# Create your models here.
class Employees(models.Model):
    Emp_id=models.AutoField(primary_key=True)
    Emp_email=models.CharField(max_length=200,blank=False,null=False)
    Emp_password=models.CharField(max_length=40,blank=False,null=False)
    Emp_name=models.CharField(max_length=200,blank=False,null=False)
    Emp_mobno=models.CharField(max_length=10)
    Emp_age=models.IntegerField(max_length=2)
    Emp_depart=models.CharField(max_length=200)
    Emp_role=models.CharField(max_length=200)
    Emp_expinyears=models.IntegerField(max_length=2)


