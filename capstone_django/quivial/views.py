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


def index(request):
    """
       Render the index.html template, the first page that the user sees when entering the website.  
    """
    return render(request, 'quivial/index.html')

                
def user_home(request):
    """
       Render the user_home.html template for registered and logged in users, which displays the site rules and a button to navigate to the play view.
    """
    return render(request, 'quivial/user_home.html')


@login_required()
def play(request):
    """
       Render the play.html template, which displays the dad jokes. 
    """
    return render(request, "quivial/play.html")


def user_login(request):
    """ 
        Render the login.html template found in the authentication directory of the Quivial folder for user authentication.
    """
    return render(request, 'quivial/authentication/login.html')


def authenticate_user(request):
    """
       Authenticate the user by checking the username and password submitted in a POST request. If the credentials are correct, log in the user and
       redirect to the user_home view with a success message. If the credentials are incorrect, redirect to the login view with an error message.
    """
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
    """
        Render the register.html template found in the authentication directory of the Quivial folder for user registration.
    """

    return render(request, 'quivial/authentication/register.html')


def authenticate_registered_user(request):
    """
       Authenticate a new user by creating a new User object with the submitted username and password. If the username already exists, 
       redirect to the registration view with an error message. If the username is unique, save the new user's credentials, log in the user, 
       and redirect to the user_home view with a success message.
    """
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
    """
        Log out the user and redirect to the user_home view where they can choose to log in or register. This function does not return anything.
    """
    return HttpResponseRedirect(
        reverse ('quivial:user_home')
    )