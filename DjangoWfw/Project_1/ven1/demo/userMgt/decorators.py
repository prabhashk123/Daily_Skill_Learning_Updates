from django.shortcuts import render

# make decorator in python method1
# def login_not_required(func):
#     # inner me jo view hai wahi pas hoga
#     def inner(request):
#         if request.user.is_authenticated==False:
#             return func(request)
#         else:
#             return render(request,'userMgt/home.html')
#     return inner

# make decorator in python method-2
# def login_not_required(func):
#     # inner me jo view hai wahi pas hoga
#     def inner(*args,**kwargs):
#         if args[0].user.is_authenticated==False:
#             return func(args[0])
#         else:
#             return render(args[0],'userMgt/home.html')
#     return inner

# make decorator in python method-2
def login_not_required(func):
    # inner me jo view hai wahi pas hoga ye tuple ke andar first argument chalega
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated==False:
            return func(request)
        else:
            return render(request,'userMgt/home.html')
    return inner