from django import  forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin import widgets

class ServiceForm(forms.ModelForm):
    class Meta : 
        model = Service
        fields = ["photo" ,]

class OccupationForm(forms.ModelForm):
    class Meta :
        model = Occupation
        fields = "__all__"

class RegisterForm(UserCreationForm):
    class Meta :
        model = User 
        fields = ['first_name' , 'last_name' , 'username' , 'email' ,'password1' , 'password2']