from django import views
from . import views
from django.urls import path

urlpatterns = [
    path('exam/', views.exam, name="exam"),
    path('addexam/', views.addexam, name="addexam"),
    path('examlist/', views.examlist, name="examlist"),



]