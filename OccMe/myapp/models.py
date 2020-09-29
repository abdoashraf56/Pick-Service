from django.db import models
from .validators import validatePhone
from uuid import uuid4
from django.contrib.auth.models import User

class Occupation (models.Model):
    """ Data class contains Occupation name """
    name = models.CharField(max_length=70)

    def __str__(self) :
        return f"{self.name}"

class Canadian (models.Model):
    """ Data Class contains Canadian information """
    id = models.UUIDField(default=uuid4 , primary_key=True)
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, related_name="canadian")
    firstname = models.CharField(max_length=70)
    lastname = models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.CharField(max_length=11 , validators=[validatePhone])
    profile = models.ImageField(default="profile.png", null=True, blank=True)
    occupation = models.ForeignKey(Occupation , null=True , related_name="canadians" , on_delete=models.SET_NULL)
    rate = models.IntegerField(default=3)
    latitude = models.DecimalField(max_digits=8, decimal_places=6 , null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places= 6 , null=True)


    def __str__(self) :
        return f"{self.firstname} {self.lastname}"

class OridnaryUser(models.Model):
    """ Data Class contains user information """
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, related_name="oridnaryUser")
    phone = models.CharField(max_length=11 , validators=[validatePhone])
    latitude = models.DecimalField(max_digits=8, decimal_places=6 , null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places= 6 , null=True)
    profile = models.ImageField(default="profile.png", null=True, blank=True)

    def __str__(self) :
        return f"{self.phone}"