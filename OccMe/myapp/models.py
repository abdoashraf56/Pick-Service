from django.db import models
from .utilites import validatePhone
from uuid import uuid4


class Canadian (models.Model):
    """ Data Class contains Canadian information """

    id = models.UUIDField(default=uuid4() , primary_key=True)
    firstname = models.CharField(max_length=70)
    lastname = models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.CharField(max_length=11 , validators=[validatePhone])
    profile = models.ImageField(default="profile.png", null=True, blank=True)
    occupation = models.CharField(max_length=70)
    rate = models.IntegerField()
    latitude = models.DecimalField(max_digits=8, decimal_places=6 , null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places= 6 , null=True)