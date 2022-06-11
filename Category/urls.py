from django import views
from . import views
from django.urls import path

urlpatterns = [
    path('cate/', views.cat, name="cat"),
    path('get/', views.get, name="get"),

    path('category/', views.category, name="category"),
 




]