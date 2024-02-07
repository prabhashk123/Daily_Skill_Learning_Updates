# from rest_framework.serializers import Serializer
from rest_framework import serializers
from newappdbms.models import Customer

# this is model class example
# class Customer(models.Model):
#     name=models.CharField(max_length=20,null=False,blank=False)
#     age=models.IntegerField(null=True,blank=True)
#     address=models.TextField(max_length=30,null=True,blank=True)
"""Method-2 for using modelseralizer"""
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'


"""Method-1 make serialzer use serialzer class for complex data in json string formate first dict than json str same field name of model class"""
# class CustomerSerializer(serializers.Serializer):
#     name=serializers.CharField()
#     age=serializers.IntegerField()
#     address=serializers.CharField()
#     phone=serializers.CharField()

