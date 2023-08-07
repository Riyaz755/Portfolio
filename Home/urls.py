from django.contrib import admin
from django.urls import path,include
from Home import views

urlpatterns = [
   
    path('',views.Home,name='Home'),
    path('contact',views.contact,name='contact'),
    path('About',views.About,name='About'),
    path('Portfolio',views.portfolio,name='Portfolio')
]