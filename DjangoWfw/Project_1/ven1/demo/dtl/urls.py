from django.urls import path
from .views import *
# base url="http://127.0.0.1:8000/dtl/"

urlpatterns = [
    path('',view_home,name='home'),
    path('variable/',view_variable,name='variable'),
    path('base/',view_base,name='base'),
    path('homes/',view_homes,name='homes'),
    path('ifexample/',view_ifexample,name='ifexample'),
    path('fatch_all_stu/',view_fatch_all_stu,name='fatch_all_stu'),
    path('writesession/',view_writesession,name='writesession'),
    path('readsession/',view_readsession,name='readsession'),

]
