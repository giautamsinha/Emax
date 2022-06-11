from django import views
from . import views
from django.urls import path

urlpatterns = [
    path('course/', views.course, name="course"),
    path('addcourse/', views.addcourse, name="addcourse"),
    
    
]