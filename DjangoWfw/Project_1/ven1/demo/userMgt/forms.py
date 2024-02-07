from .models import *
from django import forms

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        # fields='__all__'
        # remove one fieled below cmd
        exclude=['user']
    date_of_birth=forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))