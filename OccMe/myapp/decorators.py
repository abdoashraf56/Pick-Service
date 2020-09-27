from django.http import HttpResponse

def HttpGet(view_func):
    """
     Validate the request is GET request
    """
    def wrap(request , *args , **keyargs):
        if request.method == "GET":
            return view_func(request , *args , **keyargs)
        else :
            return HttpResponse(404)
    return wrap

def HttpPost(view_func):
    """
     Validate the request is POST request
    """
    def wrap(request , *args , **keyargs):
        if request.method == "POST":
            return view_func(request , *args , **keyargs)
        else :
            return HttpResponse(404)
    return wrap

