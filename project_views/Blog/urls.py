from django.urls import path
from . import views

urlpatterns = [
    path('', views.dua_blog, name ='dua')
]