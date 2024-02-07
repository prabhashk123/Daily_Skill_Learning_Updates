from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.sessions.models import Session
from .models import contact
from django.http.response import HttpResponse


# Create your views here.
def register(request):
    if request.method=='POST':
        email=request.POST['n1']
        password=request.POST['n2']
        username=request.POST['n3']
        obj=User.objects.create_user(email=email, password=password, username=username)
        obj.save()
        return render(request,'homes1.html')
    else:
        return render(request,'register.html')
def homes1(request):
    if request.method=='POST':
        email=request.POST['n1']
        password=request.POST['n2']
        username=request.POST['n3']
        obj=User.objects.create_user(email=email, password=password, username=username)
        obj.save()
        return render(request,'homes1.html')
    else:
        # if request.session.has_key('is_log'):
        return render(request,'homes1.html')
def about(request):
    return render(request,'about.html')
def Contact(request):
    d1={}
    if request.method=='POST':
        con=contact()
        con.name=request.POST.get('name')
        con.email=request.POST.get('email')
        con.phone=request.POST.get('phone')
        # con.select=request.POST.get('select')
        con.query=request.POST.get('query')
        con.save()
        # return HttpResponse('Contact added')
        return redirect('contact')
    return render(request,'contact.html',context=d1)
def logins(request):
    if request.method=='POST':
        username=request.POST['usname']
        password=request.POST['pass']
        # check valid username and password
        obj=auth.authenticate(username=username,password=password)
        # request.session['is_log']=True
        if obj is not None:
            return render(request,'homes1.html')
    else:
        return render(request,'logins.html',{'error':'Enter valid username or password'})
def logout(request):
    auth.logout(request)
    return render(request,'register.html')
# For sessison
def cart(request):
    return render(request,'cart.html')
def addcourse(request):
    if request.method=="POST":
        n1=request.POST['coursename']
        n2=request.POST['durationmonth']
        request.session[n1]=n2
        return render(request,'cart.html')
    else:
        return render(request,'cart.html')


    