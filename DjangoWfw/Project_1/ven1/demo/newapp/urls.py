# create your urls
from django.urls import path
from .import views
from django.http.response import HttpResponse
from django.shortcuts import render
# For http response make cal culator
def cal(request):
    # resp=HttpResponse("This is our calculator")
    # no read karna hai to get data read user ka server
    if request.method=="GET":
        no1=request.GET.get('no1',"")
        no2=request.GET.get('no2',"")
        res=''
        if (no1!=""):
            if 'sum' in request.GET:
                res=int(no1)+int(no2)
            if 'sub' in request.GET:
                res=int(no1)-int(no2)
        # make dictonary to call data
        d1={'no1':no1,'no2':no2,'res':res}
        return render(request,'cal.html',context=d1)
    
# data send through url writing
    
def sum(request,no1,no2):
    res=no1+no2
    resp=HttpResponse("Here we are passed data on url <br> sum two number "+ str(res))
    return resp
def sub(request,no1,no2):
    res=no1-no2
    resp=HttpResponse("pass data on url<br>subtract of two number "+str(res))
    return resp

urlpatterns = [
    path('',views.register,name='register'),
    path('homes1/',views.homes1,name='homes1'),
    path('about/',views.about,name='about'),
    path('contact/',views.Contact, name='contact'),
    path('logout/',views.logout,name='logout'),
    path('logins/',views.logins,name='logins'),
    path('addcourse/',views.addcourse,name='addcourse'),
    path('register/',views.register,name='register'),
    # view create in also urls files data send on urls
    path('cal/',cal),
    path('cal/sum/<int:no1>/<int:no2>/',sum),
    path('cal/sub/<int:no1>/<int:no2>/',sub),

  
]
