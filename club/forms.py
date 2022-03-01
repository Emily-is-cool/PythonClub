from importlib.resources import Resource
from django import forms
from .models import resource, meeting 

class resourceForm(forms.ModelForm):
    class Meta: 
        model=resource
        fields='__all__'

class meetingForm(forms.ModelForm):
    class Meta:
        model=meeting
        fields='__all__'