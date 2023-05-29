from django.urls import path, include
from . import views
urlpatterns=[
    path("home",views.home,name="home"),
    path("",views.index,name="index"),
    path("quiz",views.quiz,name="quiz")
    
]