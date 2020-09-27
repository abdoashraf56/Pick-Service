from django.http import HttpResponse , HttpResponseNotFound

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

