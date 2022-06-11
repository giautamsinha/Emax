from django import http
from django.shortcuts import render
from django.http import HttpResponse
from numpy import insert
from .models import Course

# Create your views here.


def course(request):
    if request.user.is_authenticated:
        course=Course.objects.all()
        return render(request , 'layouts/course.html',{'course':course})




def addcourse(request):
    if request.method == 'POST':
      coursename = request.POST.get('coursename') 
      examname1 = request.POST.get('examname1')
      examname2 = request.POST.get('examname2')
      examname3 = request.POST.get('examname3')
      examname4 = request.POST.get('examname4')
      examname5 = request.POST.get('examname5')
      examname6 = request.POST.get('examname6')
      examname7 = request.POST.get('examname7') 
      examname8 = request.POST.get('examname8')
      examname9 = request.POST.get('examname9')
      examname10 = request.POST.get('examname10')
      subjectname1  = request.POST.get('subjectname1')
      subjectname2 = request.POST.get('subjectname2')
      subjectname3 = request.POST.get('subjectname3')
      subjectname4 = request.POST.get('subjectname4')
      subjectname5 = request.POST.get('subjectname5')
      subjectname6 = request.POST.get('subjectname6')

      insert_course=Course(courseName = coursename , examName1 = examname1 , examName2=examname2 , examName3=examname3 , examName4=examname4 ,examName5 = examname5 , examName6=examname6 , examName7=examname7 , examName8= examname8 , examName9 =examname9 , examName10=examname10 , subjectName1=subjectname1 , subjectName2=subjectname2 ,subjectName3 =subjectname3 ,subjectName4 = subjectname4 ,subjectName5=subjectname5 , subjectName6=subjectname6 )
      insert_course.save()
      response = HttpResponse({'Success':'Successss'})
      response.status_code = 200
      return response
