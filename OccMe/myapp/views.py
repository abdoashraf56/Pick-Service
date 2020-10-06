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
    return render(request , 'myapp/home.html' , context)

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
        return render(request , 'myapp/canadian-profile.html' , context)
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
    return render(request , 'myapp/pick-service.html' , context)

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
    return render(request , 'myapp/thankspage.html')

@login_required(login_url="login")
@Authorize(groups=["canadian"])
@HttpGet
def canadian(request):
    canadian = Canadian.objects.get(user=request.user)
    requests_num = Service.objects.filter(canadian = canadian).count()
    context = { 
            "range" : range(5) ,
            "canadian" : canadian ,
            "requests": requests_num
        }
    return render(request , 'myapp/canadian.html' , context)

@login_required(login_url="login")
@Authorize(groups=["canadian",])
@HttpGet
def canadian_requests(request):
    canadian = Canadian.objects.get(user=request.user)
    requests = Service.objects.filter(canadian = canadian).order_by("-createdAt")
    context = { 
            "range" : range(5) ,
            "canadian" : canadian ,
            "requests": requests
        }
    return render(request , 'myapp/canadian-requests.html' , context)

@login_required(login_url="login")
@Authorize(groups=["canadian",])
@HttpGet
def edit_canadian_profile(request):
    canadian = Canadian.objects.get(user=request.user)
    user_form = UpdateUserForm(instance=request.user)
    canadian_form = CanadianForm(instance=canadian)
    context = {"canadian_form" : canadian_form.as_ul() , "user_form" : user_form.as_ul()}
    return render(request , 'myapp/edit_candian_profile.html' , context)


@login_required(login_url="login")
@Authorize(groups=["canadian",])
@HttpPost
def edit_canadian_profile_post(request):
    canadian = Canadian.objects.get(user=request.user)
    user_form = UpdateUserForm(request.POST , instance=request.user)
    canadian_form = CanadianForm(request.POST , instance=canadian)
    user_form.save()
    canadian_form.save()
    return HttpResponse(200)
