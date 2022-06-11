from django.http import HttpResponse
from django.shortcuts import render ,redirect
from .models import Exam
from Course.models import Course
from django.http import JsonResponse
from django.contrib import messages




def exam(request):
 if request.user.is_authenticated:
    if request.method == 'POST':
        id = request.POST.get('id')
        if id != "" and Course.objects.filter(id=id).exists():
            course = Course.objects.values().filter(id=id)
            examcourse = list(course)
            return JsonResponse({'Success': 'Success' ,'examcourse':examcourse})
            # response.status_code = 200
            # return response
        else:
            pass
    else:
        course=Course.objects.all()
        return render(request, 'layouts/addexam.html' , { 'course':course})
 else:
    return redirect('login')



def addexam(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            courseid=request.POST['courseid']
            coursename=request.POST['coursename']
            test=request.POST['test']
            subject=request.POST['subject']
            datetime=request.POST['datetime']
            marks=request.POST['marks']
            negative=request.POST['negativemarking']

            exam=Exam(courseId = courseid , courseName = coursename , testName = test , subjectName = subject , marks = marks , negativeMarking =negative ,examDate = datetime , status=True)
            exam.save()
            messages.success(request, 'Exam Addded Successfully !')
            return redirect('exam')
        else:
             messages.error(request, 'Something went wrong !')
             return redirect('exam')

    else:
        return redirect('login')


def examlist(request):
    if request.user.is_authenticated:
        examList = Exam.objects.filter()
        return render(request, 'layouts/exam_list.html', {'exam_list': examList})
    else:
        return redirect('login')
