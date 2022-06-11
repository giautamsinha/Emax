from . import views
from unicodedata import name
from django.urls import path
urlpatterns = [
    path('qwe/', views.test, name="test"),

]
