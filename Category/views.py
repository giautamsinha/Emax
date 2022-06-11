from django.http import HttpResponse
from django.shortcuts import render
from .models import CoursesCategorys
# Create your views here.
def cat(request):
    val1="ADCA"
    val2=["Test 1" , "Test 2" , "Test 3","Semester 1" ,"Semester 2" , "Semester 3" ,"Main Test 1", "Main Test 2", "Main Test 3", "Final Exam" ]
    val3=["subject 1" , "subject 2" ]
    insert_question=CoursesCategorys(courseName = val1 , courseSubCategory = val2 , subjectName=val3)
    insert_question.save()
#  Test 1, Test 2, Test 3, Semester 1, Semester 2, Semester 3, Main Test 1, Main Test 2, Main Test 3, Final Exam
    return HttpResponse("hello")
    
    # "Test 1" , "Test 2" , "Test 3","Semester 1" ,"Semester 2" , "Semester 3" ,"Main Test 1", "Main Test 2", "Main Test 3", "Final Exam" 

def get(request):
    questionlist=CoursesCategorys.objects.all()
    for i in questionlist:
       a=i
    
    return HttpResponse(i)




def category(request):
    questionlist=CoursesCategorys.objects.all()
    for i in questionlist:
       a=i
    
    return HttpResponse(i)

