from django.urls import path
from . import views
from . import auth

urlpatterns = [
    path('', views.home , name = "home"),
    path('canadian_profile/<uuid:pk>', views.canadian_profile , name = "canadian_profile"),
    path('pick-service/<uuid:pk>', views.pickService , name = "pick-service"),
    path('post-service/<uuid:pk>', views.postService , name = "post-service"),

    
    # authoriztion and authincation urls
    path('register' , auth.registerPage , name="register"),
    path('login' , auth.loginPage , name="login"),
    path('logout' , auth.logoutPage , name="logout"),
]
