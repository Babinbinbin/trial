from django.urls import path, include
from . import views
app_name = "first"
urlpatterns=[
    path("homepage",views.homepage,name="homepage"),
    path("",views.index,name="index"),
    path("quiz",views.quiz,name="quiz"),
    path('get_quiz',views.get_quiz,name ='get_quiz'),
    path("op",views.operation,name="op"),
    path("<str:pk>",views.article,name="article"),
]