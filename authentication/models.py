from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    fonctions = (
        ("candidate","candidate"),
        ("employer", "employer"),
        ) 
    function = models.CharField(max_length=30,choices=fonctions, verbose_name='functions')
    profile_photo = models.ImageField(verbose_name='profile_photo', null=True, blank=True)
    
    