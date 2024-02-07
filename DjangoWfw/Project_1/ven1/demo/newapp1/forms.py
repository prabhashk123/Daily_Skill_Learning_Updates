from django.forms import fields
from .models import Customer
from django import forms
from django.core.exceptions import ValidationError

class CustomerForm(forms.ModelForm): 
# add one field which is not store in data if add data in database then make field in models    
    gender=forms.ChoiceField(choices=[('Male','MALE'),('Female','FEMALE')])
    class Meta:
        model =Customer 
        fields = ['name','date_of_birth','mobile_no','email_id']
# modified attribut at run type then make constructor
    def __init__(self,*args,**kwargs):
        """for parent feature call in this child for super method"""
        super().__init__(*args,**kwargs)

        """for one field attrs change for css and update"""
        # self.fields['date_of_birth'].widget.attrs['class']='bgcolor'
        self.fields['date_of_birth'].widget=forms.TextInput(attrs={'type':'date'})

        """for all field attrs change fields give dictonary then key and values"""
        for e in self.fields.values():
            e.widget.attrs['class']='bgcolor'      
        
# validations for multiple field overwrite the cleaned method make class inside modelform like inheritance
    def clean(self,*arg,**kwargs):
        # overite inheritence use super method
        super().clean(*arg,**kwargs)
        name1=self.cleaned_data['name']
        email1=self.cleaned_data['email_id']
        if name1 not in email1:
            raise ValidationError("name not found in email")
        
        # clean method used for field seperate validetors
    # def clean_name(self):
    #     data=self.cleaned_data['name']
    #     if (ord(data[0])>=65 and ord(data[0])<=90):
    #         pass
    #     else:
    #         raise ValidationError("first letter of name is capital")
    #     return data
# field modified  same name previous field
    email_id=forms.ChoiceField(choices=[('prabhash@gmail.com','prabhash@gmail.com'),('subhash@gmail.com','subhash@gmail.com'),('akash@gmail.com','akash@gmail.com')])
    # date_of_birth=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    
