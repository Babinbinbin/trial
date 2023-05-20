from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserRegistrationForm

# Create your views here.

def register2(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request,'users/register2.html',{'form':form})

