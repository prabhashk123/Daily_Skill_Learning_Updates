# Create your model forms
from django import forms
from .models import Customer
from .models import Course
from .models import Student

class CustomerForm(forms.ModelForm):
    # make inner class name meta
    class Meta:
        # use model like mere pas customer model hai
        model=Customer
        # for all field like name,address,phone of customer models
        fields='__all__'
        # for not all field only selected than use list of fields
        # fields=['name','address']
class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'


