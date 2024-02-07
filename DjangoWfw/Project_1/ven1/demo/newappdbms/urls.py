from django.urls import path
from .views import *

urlpatterns = [
    path('add/',add_view),
    path('search/',search_view),
    path('add_using_models',add_using_modelform_view),
    path('sampleform',sample_view),
    path('registerform',register_view),
    path('test',test_view),
    path('cal',cal_view),

]
