from django.http import HttpResponse , HttpResponseNotFound , HttpResponseNotAllowed
from django.shortcuts import render , redirect
def HttpGet(view_func):
    """
     Validate the request is GET request
    """
    def wrap(request , *args , **keyargs):
        if request.method == "GET":
            return view_func(request , *args , **keyargs)
        else :
            return HttpResponseNotFound('<h1>Page not found</h1>')
    return wrap

def HttpPost(view_func):
    """
     Validate the request is POST request
    """
    def wrap(request , *args , **keyargs):
        if request.method == "POST":
            return view_func(request , *args , **keyargs)
        else :
            return HttpResponseNotFound('<h1>Page not found</h1>')
    return wrap


def NotAllowed_on_login(view_func):
    """
        Validate the user isn't log in before enter page
    """
    def wrapper(request , *args , **keyargs):
        if request.user.is_authenticated == False : 
            return view_func(request , *args , **keyargs)
        else:
            return redirect('')
    return wrapper

def Authorize(groups):
    """
        Authorize controls by list of groups
    """
    def warp1(view_func):
        def wrap2(request , *args , **keyargs):
            if request.user.groups.filter(name__in=groups).count() > 0 :
                return view_func(request , *args , **keyargs)
            else :
                return HttpResponseNotAllowed("<h1>You not allowed here</h1>")
        return wrap2
    return warp1



