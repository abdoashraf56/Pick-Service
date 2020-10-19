from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .decorators import *
from .forms import *
from random import choice
import django.utils.timezone as tz
from django.contrib.auth import authenticate , login , logout
# Create your views here.


@login_required(login_url="login")
@Authorize(groups=["canadian"])
@HttpGet
def canadian(request):
    """
        @desc Get the canadian profile page
        @route /canadian
    """
    canadian = Canadian.objects.get(user=request.user)
    requests_num = Service.objects.filter(canadian = canadian,isFinish=False,isAccepted=False).count()
    context = { 
            "range" : range(5) ,
            "canadian" : canadian ,
            "requests": requests_num
        }
    return render(request , 'myapp/canadian/canadian.html' , context)

@login_required(login_url="login")
@Authorize(groups=["canadian",])
@HttpGet
def canadian_requests(request):
    """
        @desc Get the canadian requests page
        @route /canadian_requests
    """
    canadian = Canadian.objects.get(user=request.user)
    requests = Service.objects.filter(canadian = canadian,isFinish=False,isAccepted=False).order_by("-createdAt")
    context = { 
            "range" : range(5) ,
            "canadian" : canadian ,
            "requests": requests
        }
    return render(request , 'myapp/canadian/canadian-requests.html' , context)

@login_required(login_url="login")
@Authorize(groups=["canadian",])
@HttpGet
def canadian_requests_accepted(request):
    """
        @desc Get the canadian requests page
        @route /canadian_requests
    """
    canadian = Canadian.objects.get(user=request.user)
    requests = Service.objects.filter(canadian = canadian,isFinish=False,isAccepted=True).order_by("-createdAt")
    context = { 
            "range" : range(5) ,
            "canadian" : canadian ,
            "requests": requests
        }
    return render(request , 'myapp/canadian/canadian_requests_accepted.html' , context)

@login_required(login_url="login")
@Authorize(groups=["canadian",])
@HttpGet
def edit_canadian_profile(request):
    """
        @desc Get the canadian profile edit page
        @route /edit_candian_profile
    """
    canadian = Canadian.objects.get(user=request.user)
    user_form = UpdateUserForm(instance=request.user)
    canadian_form = CanadianForm(instance=canadian)
    context = {"canadian_form" : canadian_form.as_ul() , "user_form" : user_form.as_ul()}
    return render(request , 'myapp/canadian/edit_candian_profile.html' , context)


@login_required(login_url="login")
@Authorize(groups=["canadian",])
@HttpPost
def edit_canadian_profile_post(request):
    """
        @desc POST saved canadian updated profile 
        @route /edit_candian_profile
    """
    canadian = Canadian.objects.get(user=request.user)
    user_form = UpdateUserForm(request.POST , instance=request.user)
    canadian_form = CanadianForm(request.POST , instance=canadian)
    user_form.save()
    canadian_form.save()
    return redirect("canadian")

@login_required(login_url="login")
@Authorize(groups=["canadian",])
@HttpGet
def accept(request , pk):
    """
        @desc canadian accept the request service
        @route /accept/:pk
    """
    service = Service.objects.get(id = pk)
    service.isAccepted = True
    #Notify the user the canadian accept the request
    service.note = f"{service.canadian.user.get_full_name()} accept your request"
    service.save()
    return redirect("canadian_requests")

@login_required(login_url="login")
@Authorize(groups=["canadian",])
@HttpGet
def refuse(request , pk):
    """
        @desc canadian refuse the request service and go to other
        @route /accept/:pk
    """
    service = Service.objects.get(id = pk)
    canadians = Canadian.objects.filter(occupation=service.canadian.occupation)
    canadians = [c for c in canadians if c.id != service.canadian.id]
    random_canadian = choice(canadians)
    service.canadian = random_canadian
    #Notify the user the canadian refused and turn to other random one
    service.note = f"your request has shift to {random_canadian.user.get_full_name()}"
    service.save()
    return redirect("canadian_requests")