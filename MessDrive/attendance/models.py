from django.db import models
from django.conf import settings

# Create your models here.
class attendance(models.Model):
    date = models.DateField()
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True)

class expense(models.Model):
    date = models.DateField()
    expense = models.IntegerField()
    cleaningStaff_per_day = models.IntegerField()
    cookingStaff_per_day = models.IntegerField()
    
class staff_expense(models.Model):
    date = models.DateField()
    total_salary = models.IntegerField()

class BillDetails(models.Model):
    date = models.DateField()
    perday = models.IntegerField()

    #user.objects.exclude id 

    