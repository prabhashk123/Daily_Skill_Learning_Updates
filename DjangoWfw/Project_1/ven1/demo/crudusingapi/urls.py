from django.urls import path
from . import views

urlpatterns = [
    # path('api/',views.apis,name='api'),
    path('api/',views.Apis.as_view(),name='api')

]
