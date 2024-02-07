from django.urls import path
from .views import *


urlpatterns = [
    path('getcus/<int:id>',get_customer_by_id), 
    path('getairquality/',get_air_quality_view), 
    path('getairqualityusingajax',get_air_quality_using_ajax_view),
    path('savecusbyrestapi',save_customer_view),
    
]
