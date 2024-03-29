from django.shortcuts import render
from .models import Quiz
from questions.models import (Question,Answer)
from results.models import Result
from django.views.generic import ListView
from django.http import JsonResponse
from django.shortcuts import HttpResponse



def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def ajax_test(request):
    if is_ajax(request=request):
        message = "This is ajax"
    else:
        message = "Not ajax"
    return HttpResponse(message)
# Create your views here.


 

class QuizListView(ListView):
    model = Quiz
    template_name = 'quizes/main.html'

def quiz_view(request,pk):
    quiz = Quiz.objects.get(pk = f"{pk}")
    return render(request ,"quizes/quiz.html",{'obj' : quiz})

def quiz_data_view(request, pk):
    quiz=Quiz.objects.get(pk=int(pk))
    questions=[]
    for q in quiz.get_questions():
        answers=[]
        for a in q.answer_set.all():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })

def save_quiz_view(request,pk):  
    if request.is_ajax():
            questions =[]
            data = request.POST
            data_ = dict(data.lists())
            data_.pop('csrfmiddlewaretoken')
            for  k in data_.keys():
                question = Question.objects.get(text=k)
                questions.append(question)
            user =request.user
            quiz =Quiz.objects.get(pk=pk)
            score =0
            multiplier =(100/quiz.number_of_questions)
            results =[] 
            correct_answer = None

            for q in questions:
                a_selected = request.POST.get(q.text)

                if a_selected !="":
                    question_answers =Answer.objects.filter(question = q)
                    for a in question_answers:
                        if a_selected == a.text :
                            if a.correct:
                                score+=1
                                correct_answer =a.text
                        else:
                            if a.correct:
                                correct_answer =a.text
                    results.append({str(q): {'correct_answer' : correct_answer,"answered":a_selected}})
                else:
                    question_answers =Answer.objects.filter(question =q)
                    for a in question_answers:
                            if a.correct:
                                correct_answer =a.text
                    results.append({str(q) : {'correct_answer' : correct_answer,"answered":"None"}})
            score_ = score*multiplier
            Result.objects.create(quiz=quiz,user=user,score=score_)      

            if score_ >= quiz.required_score_to_pass:
                return JsonResponse({'passed':True,'score':score_ ,'results' :results})
            else:
                return JsonResponse({'passed' : False,'score' :score_,"results" :results}) 
        
        
        
    

