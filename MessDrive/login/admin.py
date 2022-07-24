from django.contrib import admin
from .models import User, Inmate, Staff

# Register your models here.
admin.site.register(User)
admin.site.register(Inmate)
admin.site.register(Staff)
