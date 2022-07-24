from django.shortcuts import render
from .forms import ExpenseForm
from .models import attendance
from django.contrib import messages

# Create your views here.
def expense(request):
    form = ExpenseForm
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'expense.html', {'form' : form})

def success(request):
    return render(request, 'success.html')

def successOne(request):
    return render(request, 'successExpense.html')    
    
#def saveitem(request):
    #if request.method == 'POST':
       # if request.POST.get('ddl-select1'):
            #savevalue = attendance()
            #savevalue.userid = request.POST.get('ddl-select1')
            #savevalue.save() 
            #messages.success(request, 'The absentees are '+savevalue.userid' is saved successfully') 

