from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OccupationForm():
    class Meta :
        model = Occupation
        fields = "__all__"

class RegisterForm(UserCreationForm):
    class Meta :
        model = User 
        fields = ['first_name' , 'last_name' , 'username' , 'email' ,'password1' , 'password2']