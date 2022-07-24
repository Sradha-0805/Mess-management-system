from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from django.forms.models import model_to_dict
from .models import User, Inmate, Staff
from .forms import InmateSignUpForm, StaffSignUpForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from attendance.models import attendance,expense
from login.models import User
from attendance.models import BillDetails,staff_expense

# Create your views here.
no_of_inmates = 10

def index(request):
    return render(request, 'index.html')
def signin(request):
    return render(request, 'signin.html') 
def about(request):
    return render(request, 'about.html') 
def notification(request):
    return render(request, 'notification.html')
def contact(request):
    return render(request, 'contact.html')
def profile(request):
    current_user = request.user.id
    roomno = Inmate.objects.filter(user_id = current_user).values_list('RoomNo', flat = True)
    present = attendance.objects.filter(userid= current_user, date__lte = '2022-08-21', date__gte = '2022-07-1' ).count()
    #tot_present = attendance.objects.filter(date__lte = '2022-08-21', date__gte = '2022-07-1' ).distinct().count()
    #(tot_present)
    print(present)
    r =list(roomno)
    print(r)
    for i in r:
         print(i)
    room = i 

    messbillobj = BillDetails.objects.filter(date = '2022-07-21').values_list('perday', flat = True)
    for k in messbillobj:
      #print(k)
      perday_bill = k
    print(perday_bill) 
    commonbillobj = staff_expense.objects.filter(date = '2022-07-21').values_list('total_salary', flat = True)
    for b in commonbillobj:
        commonbill = b
    print(commonbill)
    total_mess_bill = (present * perday_bill) +  (commonbill/no_of_inmates)  
    return render(request, 'profile.html', {'obj': room, 'present': present, 'messbill': total_mess_bill})
    #return render(request, 'profile.html', {'present': present})


def official(request):
    return render(request, 'starter.html')

def billCalculate(request):
    bill_date = request.POST.getlist('cal_date')
    print(bill_date)
    for i in bill_date:
        print(i)
        date_count = attendance.objects.filter(date = i).count()
        print(date_count)
        expense_amt = expense.objects.filter(date = i).values_list('expense', flat = True)
        print(expense_amt)
        for tot_amt in expense_amt:
            print(tot_amt)
            per_day = tot_amt/date_count
            print(per_day)
            perday_details =  BillDetails()
            perday_details.date = i
            perday_details.perday = per_day
            perday_details.save()

    




    return render(request, 'date.html')


def attendance_one(request):
    # attendance_list = []      
      users = User.objects.filter(is_inmate = True)
      staff = User.objects.filter(is_staff = True).filter(is_superuser = False).filter(is_official = False)
      absentees_name = request.POST.getlist('absenteeslist')
      date_value = request.POST.get('date')
      print(date_value)
      print(absentees_name)
      
     
    #  # code below for excluding absent users and storing present users to database.

      users_present = User.objects.exclude(id__in=absentees_name).values_list('id', flat=True)
      print(users_present )
      for present_user_id in users_present:
             attendance_mark = attendance()
             attendance_mark.date = '2022-07-21'
             user = User.objects.get(id=present_user_id)
             attendance_mark.userid = user 
             attendance_mark.save() 
      return render(request, 'attendance.html', {"User" : users, "Staff" : staff})      
    # #                            # if model field is user, you can add `user_id` here.
    #        #attendance_list.append( attendance_mark )   
    # # #       # instead of creating 100 attendance using 100 queries, you can bulk update together.
    # #        #attendance.objects.bulk_create(attendance_list)   # this line will bulk update every object.

      #date_count = attendance.objects.filter(date = i).count()
    #  print(date_count) 
    #  expense_amt = expense.objects.filter(date = '2022-12-06').values_list('expense', flat = True)
    #  print(expense_amt)
    #  for i in expense_amt:
    #      print(i)
    #  per_day = i/date_count
    #  print(per_day)    
           
     
     
       


# def attendance_one(request):
#     users = User.objects.filter(is_inmate = True)
#     staff = User.objects.filter(is_staff = True).filter(is_superuser = False).filter(is_official = False)
#     get_response = request.POST
#     absentees_name = dict(get_response).get('absenteeslist')
#     print(type(absentees_name))
#     #absentees_list = list(absentees_name)
#     #print(type(absentees_list))
#     # print(absentees_name)
#     for i in absentees_name:
#         #absentees = User.objects.all()
#         absentees = User.objects.exclude(id = i).values('id')
#         print(absentees)
#         #a = list(absentees)
#        # print(a)
#         #for i in a:
#             #print(i)
#         b = [d['id'] for d in absentees]
#         print(b)
       
            
#         attendance_mark = attendance()
#         for j in b:
#                 attendance_mark.date = '2022-06-06'
#                 attendance.userid = j
#                 attendance_mark.save()

       

        #a = attendance()
        #a.userid = absentees[0][1]
        #print(a)

        #ids    = author.values_list('pk', flat=True)
        #p = User.objects.get(username= id).pk
    
          
       # print(list(absentees))

   #a = list(absentees_name )
   # print(absentees_name)
    
   # print(a)
    #func_print(request,absentees_name)
    
    #print(absentees)
    #return render(request, 'attendance.html', {"User" : users, "Staff" : staff})  
    


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if(request.method == 'POST'):
        if(form.is_valid()):
            username = form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None and user.is_inmate:
                login(request, user)
                return redirect('profile')
            if user.is_staff and user.is_official:
                login(request, user)
                return redirect('official')    
            elif user is not None and user.is_staff:
                login(request, user)
                return redirect('profile')   
            else:
                msg = "invalid credentials"  
        else:
            msg = "error on validating form"
    return render(request, 'signin.html', {'form': form, 'msg' : msg})                      
        
# def func_print(request,data):
#     database = User.objects.all()
#     absentees = User.objects.exclude(id in absentees_name)
#     topics = User.objects.values_list()
#     print(database)
#     # print("database: ",len(database),"topics: ",len(topics))
#     # # print(topics)
#     # for list in topics:
#     #     print(list)
#     #     break
class inmate_register(CreateView):
    model = User
    form_class = InmateSignUpForm
    template_name = 'inmate.html'
    success_url = 'login_view' 


class staff_register(CreateView):
    model = User
    form_class = StaffSignUpForm
    template_name = 'staff.html'
    success_url = 'login_view' 

