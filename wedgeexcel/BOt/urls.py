from django.contrib import admin
from django.urls import path
from BOt import views

urlpatterns = [
    path('', views.BOT1,name="bot1")
    
]