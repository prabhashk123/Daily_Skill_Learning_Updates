from django.http.response import HttpResponse
from django.shortcuts import render
# customer model class ka object banyenge
from .models import Customer
# modelform ka object
from .forms import CustomerForm
from .forms import StudentForm
from .forms import CourseForm

# Create your views here.
# ist method to add customer
def add_view(request):
    d1={}
    if(request.method=='POST'):
        # customer obj
        cus=Customer()
        cus.name=request.POST.get('name')
        # cus.age=request.POST.get('age')
        cus.address=request.POST.get('address')
        cus.phone=request.POST.get('phone')
        cus.save()
        return HttpResponse('Customer Added Successfully')
    # make data print all
    allcus=Customer.objects.all()
    d1['allcus']=allcus
    resp=render(request,'newappdbms/add.html',context=d1)
    return resp

def search_view(request):
    d1={}
    if(request.method=='GET'):
        resp=render(request,'newappdbms/search.html',context=d1)
        return resp
    elif(request.method=='POST'):
        cusid=request.POST.get('cusid')
        cus=Customer.objects.get(id=cusid)
        detail="name:{0} address:{1} phone:{2}".format(cus.name,cus.address,cus.phone)
        d1['details']=detail
        resp=render(request,'newappdbms/search.html',context=d1)
        return resp
    
# form using modelform
def add_using_modelform_view(request):
    # kuchh send karna hai to make dict
    d1={}
    if(request.method=="GET"):
        # object of customer form
        form_cus=CustomerForm()
        # make key of dict
        d1['form']=form_cus
        resp=render(request,'newappdbms/add_cus_using_model.html',context=d1)
        return resp
    elif(request.method=="POST"):
        # make obj and read data r.post
        form_cus=CustomerForm(request.POST) 
        # make key of dict
        d1['form']=form_cus
        if(form_cus.is_valid):
            form_cus.save()
            return HttpResponse("Customer added successfully ")
        else:
            resp=render(request,'newappdbms/add_cus_using_model.html',context=d1)
            return resp
# model form
def sample_view(request):
    d1={} #make dictonay this is used object of modelform transfer data into template html form
    if request.method=="GET":
        stu=StudentForm()  #means unbound form because blank no data
        c=CourseForm()
        d1['s']=stu
        d1['c']=c
        resp=render(request,'newappdbms/sample.html',context=d1)
        return resp
      
    elif request.method=='POST':
        stu=StudentForm(request.POST) #means bound form becasuse it contain data here request.post is also dictonary
        if stu.is_valid(): #it is a valid at 
            stu.save()
            return HttpResponse("Student added successfully")
        else:
            # use this for data is not valid then store data in this dictonary
            d1['s']=stu
            return render(request,'newappdbms/sample.html',context=d1)
           
# for register form by mf
def register_view(request):
    d1={} 
    if request.method=="GET":
        stu=StudentForm() 
        c=CourseForm()
        d1['s']=stu
        d1['c']=c
        resp=render(request,'newappdbms/register_cus.html',context=d1)
        return resp
      
    elif request.method=='POST':
        stu=StudentForm(request.POST)
        if stu.is_valid(): 
            stu.save()
            return HttpResponse("Student register successfully")
        else:
            d1['s']=stu
            return render(request,'newappdbms/register_cus.html',context=d1)
           
# simple html
def test_view(request):
    # print html element
    # d1={}
    # l1={e for e in range(1,100)}
    # d1['nos']=l1
    stu=StudentForm()
    d1={'form':stu}
    resp= render(request,'newappdbms/test.html',context=d1)
    return resp

"""cal using javascripts"""
def cal_view(request):
    resp =render(request,'newappdbms/calculate_javascript.html')
    return resp 