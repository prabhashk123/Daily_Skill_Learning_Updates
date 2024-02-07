"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('newapp/',include('newapp.urls'),name='newapp'),
    path('newapp1/',include('newapp1.urls'),name='newapp1'),
    path('newappdbms/',include('newappdbms.urls'),name='newappdbms'),
    path('dtl/',include('dtl.urls'),name='dtl'),
    path('userMgt/',include('userMgt.urls'),name='userMgt'),
    path('restapi/',include('RESTAPI.urls'),name='restapi'),
    path('EMS/',include('EMS.urls'),name='EMS'),
    path('learnings/',include('learnings.urls'),name='learnings'),
    path('crudusingapi/',include('crudusingapi.urls'),name='crudusingapi')
]
