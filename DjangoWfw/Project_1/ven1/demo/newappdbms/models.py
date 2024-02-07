from django.db import models
# Create your models here.
# means create class for tables 
# Our cms inherit by model class
class Customer(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)
    age=models.IntegerField(null=True,blank=True)
    address=models.TextField(max_length=30,null=True,blank=True)
    phone=models.CharField(max_length=15)
    # str method return print time
    # def __str__(self):
    #     return self.name+':'+str(self.id)+')'
    # cus=Customer.objects.get(id=3)
    # cus
"""One to one relationship"""
class Student(models.Model):
    name=models.CharField(max_length=50)
    user_id=models.CharField(max_length=15,unique=True)
    mobileno=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class PersonDetail(models.Model):
    adddress=models.TextField(max_length=50,null=True,blank=True)
    father_name=models.CharField(max_length=50)
    # if delete student then automatic delete persondatails usin on_delete
    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    def __str__(self):
        return self.father_name
    

"""one to many rs"""
class PaymentDetail(models.Model):
    amount=models.ImageField()
    ref_no=models.CharField(max_length=50)
    # foreignkey use for multiple student ko lega
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.amount)
    
"""many to many rs"""
class Course(models.Model):
    course_name=models.CharField(max_length=100,unique=True)
    students=models.ManyToManyField(Student,null=True,blank=True)
    