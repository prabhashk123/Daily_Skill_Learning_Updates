from django.urls import path
from .import views

urlpatterns = [
    path('log/',views.log,name='log'),
    path('cusform/',views.cus_views,name='cusform'),
]
