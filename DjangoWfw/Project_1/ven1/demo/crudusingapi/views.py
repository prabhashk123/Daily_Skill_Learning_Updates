from django.shortcuts import render
from .models import Apis
from rest_framework.parsers import JSONParser
import io
from .serializer import Apiserializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# csrf for class based
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.
# Function based api crud operations
# @csrf_exempt
# def apis(request):
#     if request.method=='GET':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get('id',None)
#         if id is not None:
#             ap=Apis.objects.get(id=id)
#             serializer=Apiserializers(ap)
#             json_data=JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type='application/json')
#         ap=Apis.objects.all()
#         serializer=Apiserializers(ap,many=True)
#         json_data=JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type='application/json',)
# # for create
#     if request.method=='POST':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         # convert python dta to complex
#         serializer=Apiserializers(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             response={'msg':'data created'}
#             json_data=JSONRenderer().render(response)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')
# # for Update
#     if request.method=='PUT':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get('id')
#         ap=Apis.objects.get(id=id)
#         # Partial Update
#         serializer=Apiserializers(ap,data=pythondata,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Updated'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')
# # for delete
#     if request.method=='DELETE':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get('id')
#         ap=Apis.objects.get(id=id)
#         ap.delete()
#         res={'msg':'Data Deleted'}
#         # json_data=JSONRenderer().render(res)
#         # return HttpResponse(json_data,content_type='application/json')
#         # 2 line ke badle
#         return JsonResponse(res,safe=False)

"""Class based api crud operaations"""
@method_decorator(csrf_exempt,name='dispatch')
class Apis(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            ap=Apis.objects.get(id=id)
            serializer=Apiserializers(ap)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        ap=Apis.objects.all()
        serializer=Apiserializers(ap,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    
    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        # convert python dta to complex
        serializer=Apiserializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            response={'msg':'data created'}
            json_data=JSONRenderer().render(response)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        ap=Apis.objects.get(id=id)
        # Partial Update
        serializer=Apiserializers(ap,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        ap=Apis.objects.get(id=id)
        ap.delete()
        res={'msg':'Data Deleted'}
        # json_data=JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type='application/json')
        # 2 line ke badle
        return JsonResponse(res,safe=False)


        

        




        



