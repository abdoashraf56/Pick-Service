from django.db import models
from .utilites import validatePhone


class Canadian (models.Model):
    """ Data Class contains Canadian information """
    occupations = ["Electrics" , "Plumper" , "Mechanic" , "Carpenter" , "Other"]
    
    firstname = models.CharField(max_length=70)
    lastname = models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.CharField(max_length=11 , validators=[validatePhone])
    image = models.ImageField(default="profile.png", null=True, blank=True)
    occupation = models.CharField(max_length=70 , choices=occupations)
    rate = models.IntegerField()
    latitude = models.DecimalField(8,6)
    longitude = models.DecimalField(9,6)