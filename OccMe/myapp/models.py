from django.db import models
from .validators import validatePhone
from uuid import uuid4

class Occupation (models.Model):
    """ Data class contains Occupation name """
    name = models.CharField(max_length=70)

    def __str__(self) :
        return f"{self.name}"

class Canadian (models.Model):
    """ Data Class contains Canadian information """
    id = models.UUIDField(default=uuid4 , primary_key=True)
    firstname = models.CharField(max_length=70)
    lastname = models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.CharField(max_length=11 , validators=[validatePhone])
    profile = models.ImageField(default="profile.png", null=True, blank=True)
    occupation = models.ForeignKey(Occupation , null=True , related_name="canadians" , on_delete=models.SET_NULL)
    rate = models.IntegerField()
    latitude = models.DecimalField(max_digits=8, decimal_places=6 , null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places= 6 , null=True)


    def __str__(self) :
        return f"{self.firstname} {self.lastname}"