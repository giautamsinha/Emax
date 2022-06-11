from django import views
from . import views
from unicodedata import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('questions/', views.questions, name="questions"),
    path('addQuestions/', views.addQuestions, name="addQuestions"),
    path('actionOnQuestion/', views.actionOnQuestion, name="actionOnQuestion"),
    path('exportsample/', views.exportsample, name="exportsample"),
    # path('importsample/', views.importsample, name="importsample"),   
    path('viewQuestion/', views.viewQuestion, name="viewQuestion"),
    path('uploadcsvdata/', views.uploadcsvdata, name="uploadcsvdata"),
    path('viewPdf/', views.viewPdf, name="viewPdf"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)