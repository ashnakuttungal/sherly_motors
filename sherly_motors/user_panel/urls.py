from django.contrib import admin
from django.urls import path,include 
from. import views

urlpatterns = [
path('user_registeration',views.user_registeration),
path('user_login',views.user_login),
path('search_car',views.search_car),

]