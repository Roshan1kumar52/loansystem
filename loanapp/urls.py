
from django.urls import path
from django.contrib import admin
from . import views

app_name='loanapp'
urlpatterns = [
    
    
     path('pre',views.pre,name="pre"),
     path('forget',views.forg,name="forget"),
     path('forgt',views.fort,name="for"),
     path('user',views.Uuser, name= "user"),
     path('sign',views.sig,name="sign"),
]


