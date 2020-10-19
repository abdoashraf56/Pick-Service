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


@login_required(login_url="login")
@Authorize(groups=["user" , "admin"])
@HttpGet
def user_status(request):
    user = OridnaryUser.objects.get(user=request.user)

    requests = Service.objects.filter(user = user , isFinish=False)
    context = {
        "user" : user ,
        "requests" : requests
    }
    return render(request , 'myapp/users/user_status.html',context)

@login_required(login_url="login")
@Authorize(groups=["user",])
@HttpGet
def edit_user_profile(request):
    """
        @desc Get the user profile edit page
        @route /edit_user_profile
    """
    ordinaryUser = OridnaryUser.objects.get(user=request.user)
    user_form = UpdateUserForm(instance=request.user)
    ordinaryUser_form = OrdinaryUserForm(instance=ordinaryUser)
    context = {"ordinaryUser_form" : ordinaryUser_form.as_ul() , "user_form" : user_form.as_ul()}
    return render(request , 'myapp/users/edit_user_profile.html' , context)


@login_required(login_url="login")
@Authorize(groups=["user",])
@HttpPost
def edit_user_profile_post(request):
    """
        @desc POST saved user updated profile 
        @route /edit_user_profile
    """
    ordinaryUser = OridnaryUser.objects.get(user=request.user)
    user_form = UpdateUserForm(request.POST , instance=request.user)
    ordinaryUser_form = OrdinaryUserForm(request.POST , instance=ordinaryUser)
    user_form.save()
    ordinaryUser_form.save()
    return redirect("user_status")