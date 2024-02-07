from pydoc import render_doc
from tkinter import E
from django.shortcuts import render
from products.models import Product,SizeVariant
# for cart
# from accounts.models import Cart,CartItems
# for redirect same page in django
# from django.http import HttpResponseRedirect

def get_product(request , slug):
    # print(request.user.profile.get_cart_count)
    try:
        product = Product.objects.get(slug =slug)
        # send price use context
        context={'product':product}
        #for backend size by price
        if request.GET.get('size'):
            size=request.GET.get('size')
            price=product.get_product_price_by_size(size)
            context['selected_size']=size
            context['updated_price']=price
            print(price)
        return render(request  , 'product/product.html' , context = context)
    except Exception as e:
        print(e)


# # Cart functionality slug product ko layega
# def add_to_cart(request,uid):
#     # pass variant string kry
#     variant=request.GET.get('variant')
#     product = Product.objects.get(uid=uid)
#     user=request.user
#     # send query grt_or_create
#     cart , _ =Cart.objects.get_or_create(user=user,is_paid=False)
#     cart_item=CartItems.objects.create(cart=cart,product=product,)
#     if variant:
#         variant=request.GET.get('variant')
#         size_variant=SizeVariant.objects.get(size_name=variant)
#         cart_item.size_variant=size_variant
#         cart_item.save()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))