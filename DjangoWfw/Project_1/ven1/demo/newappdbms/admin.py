from django.contrib import admin
from .models import Student

# admin.site.register(Student)

# Register your models here. and also custom admin
@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display=['name','user_id','mobileno']
    # search by name or user_id
    list_filter=['user_id']
    search_fields=['name']
