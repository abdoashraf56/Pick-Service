from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .decorators import *
from .forms import *
from django.contrib.auth import authenticate , login , logout


@NotAllowed_on_login
def registerPage(request):
    form = RegisterForm()
    errors = None
    if request.method == "POST" :
        form = RegisterForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect("/")
        else :
            errors = form.errors.values()
    context = {"form" : form , "errors" : errors}
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