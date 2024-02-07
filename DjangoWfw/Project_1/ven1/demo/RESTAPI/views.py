from django.shortcuts import render
# make rest_api module import
from django.http.response import HttpResponse
from newappdbms.models import Customer
from .serializer import CustomerSerializer
import requests
"""Method-2"""
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

"""form creat data save using restapi in tables dtabase means consume api """
# list of string pas in method because multiple call so use 
@api_view(http_method_names=['POST'])
def save_customer_view(request):
    # native dta format in this case Deserailize me data equal to pass karna hai
    cus_searlize=CustomerSerializer(data=request.data)
    if cus_searlize.is_valid():
        cus=cus_searlize.save()
        return Response(data="Customer with id "+str(cus.id) + " is save in table",status=status.HTTP_200_OK)
    else:
         return Response(data="There is Error while saving customer ",status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def get_customer_by_id(request,id):
    try:
        cus=Customer.objects.get(id=id)
        cus_native=CustomerSerializer(cus)
        resp=Response(data=cus_native.data,status=status.HTTP_200_OK)
        return resp
    except Exception as ex:
        resp=Response(data=str(ex),status=status.HTTP_404_NOT_FOUND)
        return resp
    
"""example consume api on browser api call"""
def get_air_quality_view(request):
    if request.method=='GET':
        return render(request,'RESTAPI/get_air_quality.html')
    elif request.method=='POST':
        lat=request.POST.get('textlat')
        lon=request.POST.get('textlong')
        hour=request.POST.get('texthour')
        url = "https://air-quality.p.rapidapi.com/forecast/airquality"
        params={"lon":lon,"lat":lat,'hour':hour}
        headers = {"X-RapidAPI-Key": "d476fe8a30msh5f4ac71f8ab9e20p136d04jsnd518c42968ed","X-RapidAPI-Host": "air-quality.p.rapidapi.com"}
        resp_api=requests.get(url=url,params=params,headers=headers)
        # read api using di
        print(resp_api)
        d1={'data':resp_api.text}
        return render(request,'RESTAPI/get_air_quality.html',context=d1)
    
"""Example api consume using Ajax javascripts"""
def get_air_quality_using_ajax_view(request):
    return render(request,'RESTAPI/get_air_quality_using_ajax.html')

# Create your views here.
"""Method-1 creat Rest api make method1 complex data convert to use serailzer class"""
# def get_customer_by_id(request,id):
#     # this is call api data bye single
#     # cus=Customer.objects.get(id=id)
#     # for call multiple data used below  pass many=true in seralizer class
#     cus=Customer.objects.all() #dtatypes of cus is QuerySet
#     cus_native=CustomerSerializer(cus,many=True) #This process is Serialization
#     cus_json=json.dumps(cus_native.data)
#     resp=HttpResponse(cus_json,content_type='application/json')
#     return resp

""" creat Rest api make method1 complex data convert to use serailzer class"""

