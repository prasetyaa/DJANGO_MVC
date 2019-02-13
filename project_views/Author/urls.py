from django.urls import path
from . import views

urlpatterns = [
    path('', views.lima, name ='lima')
]