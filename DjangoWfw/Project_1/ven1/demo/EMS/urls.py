from django.urls import path
from .import views

urlpatterns = [
    path('employee/',views.employeeform),
    path('emsform/',views.emsform),
]
