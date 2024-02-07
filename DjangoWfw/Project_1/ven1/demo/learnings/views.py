from django.shortcuts import render,redirect
from .models import Employee,Customer
from .forms import Empform
from django.http.response import HttpResponse


# def learning_view(request):
#     if request.method=='GET':
#         empform=Empform()
#         d1={'empform':empform}
#         return render(request,'learnings/empregister.html',context=d1)
    
def learning_view(request):
    d1={}
    # create ka method 1
    if(request.method=='POST'):
        emp=Employee()
        emp.Emp_id=request.POST.get('Emp_id')
        emp.Emp_name=request.POST.get('Emp_name')
        emp.Emp_email=request.POST.get('Emp_email')
        emp.Emp_password=request.POST.get('Emp_password')
        emp.Emp_mobno=request.POST.get('Emp_mobno')
        emp.Emp_age=request.POST.get('Emp_age')
        emp.Emp_depart=request.POST.get('Emp_depart')
        emp.Emp_role=request.POST.get('Emp_role')
        emp.Emp_expinyears=request.POST.get('Emp_expinyears')
        emp.save()
        return HttpResponse('Employee Added Successfully')
    # display read  data
    allemp=Employee.objects.all()
    d1['allemp']=allemp
    return render(request,'learnings/empregister.html',context=d1)

def search_view(request):
    d1={}
    if(request.method=='GET'):
        resp=render(request,'learnings/search.html',context=d1)
        return resp
    elif(request.method=='POST'):
        Empid=request.POST.get('Emp_id')
        emp=Employee.objects.get(Emp_id=Empid)
        detail="Emp_name:{1} Emp_email:{2} Emp_password:{3} Emp_mobno:{4} Emp_depart:{5} Emp_role:{6} Emp_expinyears:{7} Emp_age:{8} )".format(emp.Emp_id,emp.Emp_name,emp.Emp_email,emp.Emp_password,emp.Emp_mobno,emp.Emp_depart,emp.Emp_role,emp.Emp_expinyears,emp.Emp_age)
        d1['details']=detail
        resp=render(request,'learnings/search.html',context=d1)
        return resp
    
# crud operation views all-- step-2
def customer_view(request):
    # dtaa fetch read from database
    d1={}
    allcus=Customer.objects.all()
    d1['allcus']=allcus
    return render(request,'learnings/customer.html',context=d1)

# for create/add method-2
def add_view(request):
    if(request.method=='POST'):
        # field get by maodel
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        cus=Customer(
            name=name,email=email,address=address,phone=phone
        )
        cus.save()
        # same page ke liye
        return redirect('customer/')
    return render(request,'learnings/customer.html')
    
# for edit views methos-2/Update
def edit_view(request):
    allcus=Customer.objects.all()
    context={'cus':allcus,
             }
    return render(request,'learnings/customer.html',context)
def update_view(request,id):
    if(request.method=='POST'):
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        c=Customer(
            # here id use for update not use than save record
            id=id,
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        c.save()
        # render name pe karte hai urls ke or form action me bhi url name se
        return redirect('customer')
    return render(request,'learnings/customer.html')
# For delete
def delete_view(request,id):
    # id se delete nhi krenge to sara delete ho jayega
    cu=Customer.objects.filter(id=id).delete()
    context={
        'cu':cu,
    }
    return redirect('customer',context)
    
   
        
