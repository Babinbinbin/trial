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

def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request, username=username,password=password)
        if user is not None:
            log(request,user)
            return HttpResponseRedirect(reverse("first:homepage"))
        else:
            return render(request, "users/signinindex.html", {
                "message": "Invalid credentials"
            })      
    return render(request, "users/signinindex.html")

def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]


        if len(username) >10:
            messages.error(request,"Username must be under 10 chr")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request,"Username should only contain letters and numbers")
            return redirect('home')
        

        user=User.objects.create_user(username,email,password)
        user.user_name=username
        user.save()
        messages.success(request, "Account created successfully")
        return HttpResponseRedirect(reverse("first:homepage"))

    return render(request,"users/register2.html")
         
                
