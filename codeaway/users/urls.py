from django.urls import path
from . import views
urlpatterns=[
    path('register2',views.register2,name ="register")
]