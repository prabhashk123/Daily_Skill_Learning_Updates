from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Customer)
class customerAdmin(admin.ModelAdmin):
    list_display=['name','date_of_birth','mobile_no','email_id']
    list_filter=['name']
    search_fields=['name']

