from django import forms
from django.forms import ModelForm
from .models import expense
import django.forms.widgets

class ExpenseForm(ModelForm):
    class Meta:
        model = expense
        fields = ('date', 'expense', 'cleaningStaff_per_day', 'cookingStaff_per_day')
        
        widgets = {
            'date' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'expense': forms.TextInput(attrs = {'class' : 'form-control'}),
            'cleaningStaff_per_day': forms.TextInput(attrs = {'class' : 'form-control'}),
            'cookingStaff_per_day': forms.TextInput(attrs = {'class' : 'form-control'}),

           }
        