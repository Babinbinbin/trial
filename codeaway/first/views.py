from django.shortcuts import render
from .models import Question
from .models import Answer
# Create your views here.

def home(request):
    return render(request,"first/home.html")
def index(request):
    return render(request,"first/index.html")
def quiz(request):
    store = [i for i in Question.objects.all()]
    value = [i for i in Answer.objects.all()]
    return render(request,"first/test.html",{
        "questions" : store,
        'answers' : value,
        "iscorrect": Answer.is_correct
    })
