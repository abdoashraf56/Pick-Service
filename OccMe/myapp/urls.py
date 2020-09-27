from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home , name = "home"),
    path('canadian_profile/<uuid:pk>', views.canadian_profile , name = "canadian_profile"),
]

