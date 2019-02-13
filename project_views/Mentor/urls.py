from django.urls import path
from . import views

urlpatterns = [
    path('', views.tiga, name ='tiga')
]