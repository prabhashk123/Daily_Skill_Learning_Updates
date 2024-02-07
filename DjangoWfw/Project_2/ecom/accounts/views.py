from cmath import log
from tkinter import E
from django.shortcuts import redirect, render
# django message se alert
from django.contrib import messages
# for user check
from django.contrib.auth.models import User
#for login aunthicate
from django.contrib.auth import authenticate , login , logout
# Redirct for same page and return response by http..
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from .models import Profile
# for cart
from accounts.models import Cart,CartItems,Coupon
from products.models import Product,SizeVariant
# for payment
import razorpay
from django.conf import settings

def login_page(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)
         
# verified by profile model
        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Your account is not verified.')
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username = email , password= password)
        if user_obj:
            login(request , user_obj)
            #redirect main page
            return redirect('/')
        
        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)

    return render(request ,'accounts/login.html')

def register_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)
        print(email)

# for check user exists
        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            # Redirct for same page
            return HttpResponseRedirect(request.path_info)
               
# for create user if not exists
        user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()
        
        messages.success(request, 'An email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)

    return render(request ,'accounts/register.html')

def activate_email(request , email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email token')
    
# Cart functionality slug product ko layega
def add_to_cart(request,uid):
    # pass variant string kry
    variant=request.GET.get('variant')
    product = Product.objects.get(uid=uid)
    user=request.user
    # send query grt_or_create
    cart , _ =Cart.objects.get_or_create(user=user,is_paid=False)
    cart_item=CartItems.objects.create(cart=cart,product=product,)
    if variant:
        variant=request.GET.get('variant')
        size_variant=SizeVariant.objects.get(size_name=variant)
        cart_item.size_variant=size_variant
        cart_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# for remove cart
def remove_cart(request,cart_item_uid):
    try:
        cart_item=CartItems.objects.get(uid=cart_item_uid)
        cart_item.delete()
    except Exception as e :
        print(e)
        print("Removed Successfully")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def cart(request):
# cart matching means empty cart
    try:
        cart_obj=Cart.objects.get(is_paid=False,user=request.user)
    except Cart.DoesNotExist:
        cart_obj=None
        # print(e) 
    if request.method=='POST':
        coupon=request.POST.get('coupon')
        coupon_obj=Coupon.objects.filter(coupon_code__icontains=coupon)
        if not coupon_obj.exists():
            messages.warning(request, 'invalid coupon')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        if cart_obj.coupon:
            messages.warning(request, 'coupon allready exists')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        if cart_obj.get_cart_total() < coupon_obj[0].minimum_amount:
            messages.warning(request, f'Amount should be greater than {coupon_obj[0].minimum_amount}')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        if coupon_obj[0].is_expired:
            messages.warning(request,'Coupon expired')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        cart_obj.coupon=coupon_obj[0]
        cart_obj.save()
        messages.success(request, 'coupon applied')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
  # client for payment
    if cart_obj:
        client=razorpay.Client(auth=(settings.KEY,settings.SECRET))
        payment=client.order.create({'amount':cart_obj.get_cart_total() * 100,'currency':'INR','payment_capture':1})
        cart_obj.razor_pay_payment_id=payment['id']
        cart_obj.save()
        print(payment)
    # payment=None

    context={'cart':cart_obj,'payment':payment}
    return render(request,'accounts/cart.html',context)

def remove_coupon(request,cart_id):
    cart=Cart.objects.get(uid=cart_id)
    cart.coupon=None
    cart.save()
    messages.success(request, 'Coupon Removed')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# for payment
def success(request):
    try:
        order_id=request.GET.get('order_id')
        cart=Cart.objects.get(razor_pay_order_id=order_id)
        cart.is_paid=True
        cart.save()
    except Exception as e:
        print(e)
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return HttpResponse(request, 'Payment Success')

def invoice_show(request):
    cart=Cart.objects.all()
    product=Product.objects.all()
    context={
        'cart':cart,
        'product':product
    }
    return render(request,'accounts/pdfs/invoices.html',context=context)

    

