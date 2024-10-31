from django import forms
from .models import TeachersData

class TeachersDataForm(forms.ModelForm):
    class Meta:
        model = TeachersData
        fields = ['firstName', 'lastName', 'username', 'city', 'state', 'zipcode', 'experience', 'subjects', 'previousexperience', 'email' , 'contact'  ,'class_range','photo' ]
