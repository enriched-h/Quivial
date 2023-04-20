from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse

# Landing page for all users
def index(request):
    return render(request, 'quivial/index.html')

                 
# Registered users are taken to this past after succesfully logging in
def user_home(request):
    return render(request, 'quivial/user_home.html')


@login_required()
def play(request, num_questions=10):
    return render(request, "quivial/play.html")


# Allows registered users to login
def user_login(request):
    return render(request, 'quivial/authentication/login.html')


def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('quivial:user_login'),
            messages.error(request,'Username or password incorrect, Please try again')

        )
    else:
         login(request, user)
         
         return HttpResponseRedirect(
             reverse('quivial:user_home'),
             messages.success(request,'Logged in succesfully')
        )


# Registers users 
def user_register(request):
    return render(request, 'quivial/authentication/register.html')


def authenticate_registered_user(request):
    username = request.POST['username']
    password = request.POST['password']
    new_user =  User.objects.create_user(username=username, password=password)
    if new_user is None:
        return HttpResponseRedirect(
            reverse('quivial:user_register'),
            messages.error(request,'Username already exists')

        )
    else:
         new_user.save()
         
         return HttpResponseRedirect(
             reverse('quivial:user_home'),
             messages.success(request,'Registered in succesfully')
        )


# Allows users to logout
def user_logout(request):
    return HttpResponseRedirect(
        reverse ('quivial:user_home')
    )