from django.urls import path
from . import views
from . import auth

urlpatterns = [
    path('', views.home , name = "home"),
    path('canadian_profile/<uuid:pk>', views.canadian_profile , name = "canadian_profile"),
    path('pick-service/<uuid:pk>', views.pickService , name = "pick-service"),
    path('post-service/<uuid:pk>', views.postService , name = "post-service"),
    
    
    
    path('canadian', views.canadian , name = "canadian"),
    path('edit_candian_profile', views.edit_canadian_profile , name = "edit_candian_profile"),
    path('edit_candian_profile_post', views.edit_canadian_profile_post , name = "edit_candian_profile_post"),

    
    # authoriztion and authincation urls
    path('register' , auth.registerPage , name="register"),
    path('login' , auth.loginPage , name="login"),
    path('logout' , auth.logoutPage , name="logout"),
]
