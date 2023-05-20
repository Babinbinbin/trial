from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,"first/homepage.html")
def index(request):
    return render(request,"first/index.html")