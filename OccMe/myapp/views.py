from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .decorators import *
# Create your views here.

@HttpGet
def home(request):
    """
        @desc Get The Home page with canadians avaliable
        @route home/?occupation=
    """
    canadians = Canadian.objects.all().order_by("-rate", "occupation" , "firstname")

    # if filter is provide in request filter the canadians by it
    filterByOccupation = request.GET.get("occupation")
    if filterByOccupation :
        canadians = canadians.filter(occupation=filterByOccupation)

    context = {"canadians" : canadians , "range" : range(5)}
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
    

