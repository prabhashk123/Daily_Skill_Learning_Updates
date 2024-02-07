from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .import models
from .models import Destination
from .forms import DestinationForm

def homepage(request):
    # return render(request,'index.html',{'price':700})
    # return render(request,'index.html')
     dests=Destination.objects.all()
     return render(request,'index.html',{'dests':dests})
"""
(2)Create an object of the Destination class in homepage 
function of views.py and initialize with required data.
Pass the object in response to the home page request.
"""
# def homepage(request):
#     dest=models.Destination()
#     dest.id=1
#     dest.name="Patna"
#     dest.desc="The Smart city"
#     dest.image="destination_1.jpg"
#     dest.price=500
#     return render(request,'index.html',{'dest1':dest})
def dest_details(request,dest_id):
    dest=list(Destination.objects.filter(id=dest_id))[0]
    if dest:
        # use for session in django
        d=request.session.setdefault('recent_destinations',{})
        d[dest.id]=dest.name
        request.session['recent_destination']=d
        # return render(request,'destination.html',{'dest':dest[0]})
        return render(request,'destination.html',{'dest':dest})
    
def dest_add(request):
    if request.method=='POST':
        form = DestinationForm(request.POST,request.FILES)
        print(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.info(request,'Error while creating Destination')
    return render(request,'destinationForm.html',{'form':DestinationForm()})
# Step-2 create for rest api created views-------
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DestinationSerializer
@api_view(['GET'])
def get_all_destinations(request):
    dests=Destination.objects.all()
    serializer=DestinationSerializer(dests,many=True)
    return Response(serializer.data)





