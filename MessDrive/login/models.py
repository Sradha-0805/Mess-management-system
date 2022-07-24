from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
class User(AbstractUser):
    is_inmate = models.BooleanField(default = False)
    is_official = models.BooleanField(default = False)
    PhNo = models.CharField(max_length = 12, null = True)

class Inmate(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    RoomNo = models.IntegerField(null = True) 
    


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    Role = models.CharField(max_length = 25)
    Address = models.CharField(max_length = 30)    

