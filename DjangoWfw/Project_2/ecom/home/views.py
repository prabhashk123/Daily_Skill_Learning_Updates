from django.shortcuts import render
# for render product details
from products.models import Product



def index(request):

    context = {'products' : Product.objects.all()}
    return render(request , 'home/index.html' , context)