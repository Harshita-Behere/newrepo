from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    path('', views.login_page ,name='login'),
    path('school/', views.school ,name='school'),
     path('logout/', views.logout_view, name='logout'),

    
]
