
from django.contrib import admin
from django.urls import path
from . import views
app_name='Travello'

urlpatterns = [
    path('',views.homepage),
    path('dest/<int:dest_id>',views.dest_details,name='details'),
    path('destination/<int:dest_id>',views.dest_details,name='details'),
    path('add',views.dest_add),
    path('api/dests/',views.get_all_destinations)
]
