from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .decorators import *
from .forms import *
import django.utils.timezone as tz
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
    return render(request , 'myapp/users/home.html' , context)

@login_required(login_url="login")
@Authorize(groups=["user" , "admin"])
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
        return render(request , 'myapp/users/canadian-profile.html' , context)
    else : 
        return HttpResponseNotFound("Can'y find your canadian")

@login_required(login_url="login")
@Authorize(groups=["user" , "admin"])  
@HttpGet
def pickService(request , pk):
    """
        @desc Get the pick service page to pick it
        @route pick-service/:pk
    """
    canadain = Canadian.objects.get(id=pk)
    form = ServiceForm()
    context = {"canadain" : canadain , "form" : form} 
    return render(request , 'myapp/users/pick-service.html' , context)

@login_required(login_url="login")
@Authorize(groups=["user" , "admin"])
@HttpPost
def postService(request , pk):
    """
        @desc Post new service to database
        @route post-service/:pk
    """
    canadian = Canadian.objects.get(id=pk)
    user = OridnaryUser.objects.get(user = request.user)
    print(request.POST.get("photo"))
    service = Service.objects.create(
        user= user ,
        canadian = canadian ,
        startAt= request.POST.get("startAt"),
        description=request.POST.get('description' , ''),
        photo = request.FILES.get("photo")
    )
    service.save()
    return render(request , 'myapp/users/thankspage.html')