from django.shortcuts import render
from .models import Question
from .models import Answer

# Create your views here.

def homepage(request):
    return render(request,"first/homepage.html")
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
def get_quiz(request):
    try:
        question_obj = list(Question.object.all())
        data =[]
    
        for question in question_obj:
            data.append( {
                'category' : question.category.category_name,
                'question' :  question.question,
                'matks'   : question.marks
            })
        payload = {"status":True ,'data' :data }

        return HttpResponse(payload, mimetype='application/json')
    except :
        pass
