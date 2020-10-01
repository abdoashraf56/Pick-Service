from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .decorators import *
from .forms import *
from django.contrib.auth import authenticate , login , logout
# Create your views here.

@login_required(login_url="login")
@Authorize(groups=["user" , "admin"])
@HttpGet
def home(request):
    """
        @desc Get The Home page with canadians avaliable
        @route home/?occupation=
    """
    canadians = Canadian.objects.all().order_by("-rate", "occupation" , "user__first_name")
    occupations = Occupation.objects.all()
    # if filter is provide in request filter the canadians by it
    filterByOccupation = request.GET.get("occupation")
    if filterByOccupation :
        canadians = canadians.filter(occupation=filterByOccupation)
    
    context = {"canadians" : canadians , "range" : range(5) , "occupations" : occupations}
    return render(request , 'myapp/home.html' , context)

@HttpGet
def canadian_profile(request , pk):
    """
        @desc Get the canadian profile and his reviews
        @route canadina_profile/:pk
    """
    canadian = Canadian.objects.get(id = pk)
    if canadian :
        context = {
            "title" : "Canadian Profile" ,
            "range" : range(5) ,
            "canadian" : canadian
            }
        return render(request , 'myapp/canadian-profile.html' , context)
    else : 
        return HttpResponseNotFound("Can'y find your canadian")
    

