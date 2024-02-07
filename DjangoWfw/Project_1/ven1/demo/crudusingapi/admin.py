from django.contrib import admin
from .models import Apis

# Register your models here.
@admin.register(Apis)
class Apisadmine(admin.ModelAdmin):
    list_display=['id','name','roll','city']