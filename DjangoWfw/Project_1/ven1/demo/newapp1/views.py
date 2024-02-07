from django.shortcuts import render
from .forms import *
from django.http import HttpResponse

# Create your views here.
def log(request):
    # data send on server
    if(request.method=='POST'):
        email=request.POST.get('email')
        password=request.POST.get('password')
        print("email",email)
        print('password',password)
    resp=render(request,'newapp1\log.html')
    return resp
def cus_views(request):
    if request.method=='GET':
      cusform=CustomerForm()
      d1={'form':cusform}
      return render(request,'newapp1/customer.html',context=d1)
    elif request.method=="POST":
        cusform=CustomerForm(request.POST)
        if cusform.is_valid():
            cusform.save()
            return HttpResponse("Customer added successfully")
        else:
            d1={'form':cusform}
            return render(request,'newapp1/customer.html',context=d1)

