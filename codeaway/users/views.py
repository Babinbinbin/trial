from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserRegistrationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as log
from django.contrib.auth.models import User

# Create your views here.

def registerhomepage(request):
    pass
    
    

def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request, username=username,password=password)
        if user is not None:
            log(request,user)
            return HttpResponseRedirect(reverse("homepage"))
        else:
            return render(request, "users/login.html", {
                "message": "invalid credentials"
            })      
    return render(request, "users/signinindex.html")

def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        user=User.objects.create_user(username,email,password)
        user.user_name=username
        user.save()
        messages.success(request, "Account created successfully")
        return HttpResponseRedirect(reverse("homepage"))

    return render(request,"users/register2.html")
         
                
