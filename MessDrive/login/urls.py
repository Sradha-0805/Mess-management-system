from django.urls import path
from .import views
#from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    path('', views.index, name = "index"),
    path('signin/', views.login_view, name = "signin"),
    path('inmate_register/', views.inmate_register.as_view(), name = "inmate_register"),
    path('staff_register/', views.staff_register.as_view(), name = "staff_register"),
    path('about/', views.about, name = "about"),
    path('notification/', views.notification, name = "notification"),
    path('contact/', views.contact, name = "contact"),
    path('login/', views.login_view, name = "login_view"),
    path('staff_register/login_view/', views.login_view, name = "login_view"),  
    path('inmate_register/login_view/', views.login_view, name = "login_view"), 
    path('profile/', views.profile, name = "profile"),
    path('inmate_register/signin.html', views.login_view, name = 'inmate_login' ), 
    path('official/', views.official, name = 'official'),
    path('attendance/', views.attendance_one, name = 'attendanceOne'),
    path('calculate', views.billCalculate, name = "calculation"),

]
