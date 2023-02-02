from django import forms 
from .models import student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'

class userform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class userplainform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
