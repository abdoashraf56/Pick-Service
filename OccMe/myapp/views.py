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
    canadians = Canadian.objects.all().order_by("-rate")

    # if filter is provide in request filter the canadians by it
    filterByOccupation = request.GET.get("occupation")
    if filterByOccupation :
        canadians = canadians.filter(occupation=filterByOccupation)

    context = {"canadians" : canadians , "range" : range(5)}
    return render(request , 'myapp/home.html' , context)

