from django.urls import path
from .import views
#from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    path('expense', views.expense, name = "expense"),
    path('success', views.success, name = "success"),
    path('successExpense', views.successOne, name = "successExpense"),
    


]