from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Inmate, Staff, User 
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                "class": "form-control"
            }
        )
    )

class InmateSignUpForm(UserCreationForm):
    first_name = forms.CharField(required = True,max_length=20)
    last_name = forms.CharField(required = True)
    phone_number = forms.CharField(required = True)
    email = forms.EmailField(max_length = 200)
    room_no = forms.CharField(max_length = 20)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit = False)
        user.is_inmate = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.PhNo = self.cleaned_data.get('phone_number')
        user.email = self.cleaned_data.get('email')
        user.save()
        inmate = Inmate.objects.create(user = user)
        inmate.RoomNo = self.cleaned_data.get('room_no')
        inmate.save();
        return user

            

class StaffSignUpForm(UserCreationForm):
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    phone_number = forms.CharField(required = True)
    role = forms.CharField(required = True)
    Address = forms.CharField(required = True)

    class Meta(UserCreationForm.Meta):
        model = User        
    
    @transaction.atomic
    def save(self):
        user = super().save(commit = False)
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.PhNo = self.cleaned_data.get('phone_number')
        user.save()
        staff = Staff.objects.create(user = user)
        #staff.phone_number = self.cleaned_data.get('phone_number')
        staff.Role = self.cleaned_data.get('role')
        staff.Address = self.cleaned_data.get('Address')
        staff.save();
        return user


    
