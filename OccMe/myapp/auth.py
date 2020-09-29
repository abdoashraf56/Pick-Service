from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .decorators import *
from .forms import *
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User , Group

@NotAllowed_on_login
def registerPage(request):
    form = RegisterForm()
    occupations = Occupation.objects.all()
    errors = None
    if request.method == "POST" :
        form = RegisterForm(request.POST)
        if form.is_valid() :
            user = form.save()
            #check if the user register as canadina and create new canadian
            if request.POST.get("canadian") == "on" :
                occupation = request.POST.get("occupation")
                Canadian.objects.create(
                    user = user,
                    firstname = request.POST.get("first_name"),
                    lastname = request.POST.get("last_name") ,
                    email = request.POST.get("email") ,
                    phone = request.POST.get("phone"),
                    occupation= Occupation.objects.get(id = int(request.POST.get("occupation")))
                )
                group = Group.objects.get(name='canadian')
                user.groups.add(group)
            else :
                OridnaryUser.objects.create(
                    user = user ,
                    phone = request.POST.get("phone")
                )
                group = Group.objects.get(name='user')
                user.groups.add(group)
            return redirect("/")
        else :
            errors = form.errors.values()
    context = {"form" : form , "occupations" : occupations , "errors" : errors}
    return render(request , 'myapp/register.html' , context)

@NotAllowed_on_login
def loginPage(request):
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username , password=password)

        if user is not None:
            login(request , user)
            return redirect("/")
    return render(request , 'myapp/login.html')

@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect("/")