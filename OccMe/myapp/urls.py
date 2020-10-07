from django.urls import path
from . import canadianviews , userviews
from . import auth

urlpatterns = [
    #url for users
    path('', userviews.home , name = "home"),
    path('canadian_profile/<uuid:pk>', userviews.canadian_profile , name = "canadian_profile"),
    path('pick-service/<uuid:pk>', userviews.pickService , name = "pick-service"),
    path('post-service/<uuid:pk>', userviews.postService , name = "post-service"),
    
    
    #url for canadians
    path('canadian', canadianviews.canadian , name = "canadian"),
    path('canadian_requests', canadianviews.canadian_requests , name = "canadian_requests"),
    path('canadian_requests_accepted', canadianviews.canadian_requests_accepted , name = "canadian_requests_accepted"),
    path('edit_candian_profile', canadianviews.edit_canadian_profile , name = "edit_candian_profile"),
    path('edit_candian_profile_post', canadianviews.edit_canadian_profile_post , name = "edit_candian_profile_post"),
    path('accept/<uuid:pk>', canadianviews.accept , name = "accept"),
    path('refuse/<uuid:pk>', canadianviews.refuse , name = "refuse"),

    
    # authoriztion and authincation urls
    path('register' , auth.registerPage , name="register"),
    path('login' , auth.loginPage , name="login"),
    path('logout' , auth.logoutPage , name="logout"),
]
