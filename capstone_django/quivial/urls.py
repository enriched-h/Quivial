from django.contrib import admin
from django.urls import path
from . import views

"""
URL patterns for the Quivial app.

This module defines the URL patterns for the Quivial app, including views and URL names.

Attributes:
    app_name (str): The name of the app.

"""

app_name = 'quivial'

urlpatterns = [

    path('', views.index, name='index'),
    path('user_home/', views.user_home, name='user_home'),
    path('play/', views.play, name='play'),
    path('user_login/', views.user_login, name='user_login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('user_register/', views.user_register, name='user_register'),
    path('authenticate_registered_user/', views.authenticate_registered_user, name='authenticate_registered_user'),
    path('user_logout/', views.user_logout, name='user_logout')
    

]