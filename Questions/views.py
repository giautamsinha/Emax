from datetime import date ,datetime
from django.shortcuts import render ,redirect
from .models import Questions ,Csv_Files
from django.contrib import messages
import csv , io
from django.utils.encoding import smart_str
from django.http import JsonResponse
import pandas as pd
import random
from django.http import HttpResponse
from .utils import *



# from pyexpat.errors import messages
# Create your views here.
def questions(request):
        if request.user.is_authenticated:
            questionlist=Questions.objects.all()
            return render(request , 'layouts/question_list.html' , {'question_list':questionlist})
        else:
            pass



def addQuestions(request):
    if request.user.is_authenticated:
       if request.method == 'POST':
           question=request.POST['question']
           optionA=request.POST['optionA']
           optionB=request.POST['optionB']
           optionC=request.POST['optionC']
           optionD=request.POST['optionD']
           correctAnswer=request.POST['correctanswer']
           insert_question=Questions(question = question , optionA = optionA , optionB=optionB , optionC=optionC , optionD=optionD ,correctAnswer = correctAnswer )
           insert_question.save()
           messages.success(request,'Question added successfuly')
           return redirect('addQuestions')
       else:
            return render(request , 'layouts/add_questions.html')
    else:
     return redirect('login')


def actionOnQuestion(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        if question_id != ""  and Questions.objects.filter(id = question_id ).exists():
            question=Questions.objects.get(id = question_id)
            question.delete()
            response = HttpResponse({'Success':'Successss'})
            response.status_code = 200
            return response
            pass


def exportsample(request):
   if request.user.is_authenticated: 
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="TestQuestion.csv"'
    writer = csv.writer(response)
    writer.writerow(['Question','Option A','Option B','Option C','Option D','Correct Answer'])
    return response
   else:
       return redirect('login')

def viewQuestion(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        if question_id != "" and Questions.objects.filter(id=question_id).exists():
                questions = Questions.objects.values().filter(id=question_id)
                questions_list=list(questions)
                return JsonResponse({'Success': 'Successss' , 'questions':questions_list})
        else:
                response = HttpResponse({'else': 'else'})
                response.status_code = 200
                return response
    else:
        response = HttpResponse({'else': 'else'})
        response.status_code = 400
        return response





def uploadcsvdata(request):
    if request.user.is_authenticated:
        if request.method == 'POST'  and request.FILES['file']:
            importID=random.randint(1111, 9999)
            insert_file=Csv_Files(csvFilePath = request.FILES['file'] ,importID=importID )
            insert_file.save()
            file_obj=Csv_Files.objects.get(importID=importID)
            csv_data=pd.read_csv(file_obj.csvFilePath.path)
            csv_array=csv_data.to_dict(orient="records")
            for entry in csv_array:
                film=Questions(
                    question=entry['Question'],
                    optionA=entry['Option A'],
                    optionB=entry['Option B'],
                    optionC=entry['Option C'],
                    optionD=entry['Option D'],
                    correctAnswer=entry['Correct Answer']
                )
                film.save()
            messages.success(request,'Csv File Imported Successfuly')
            return redirect('addQuestions')
    else:
        return redirect('login')


# class GeneratePdf(View):
def viewPdf(request):
    if request.user.is_authenticated:
        questionlist=Questions.objects.all()
        data = {
            'today': datetime.date, 
            'question':questionlist
        }
        pdf = render_to_pdf('layouts/pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
    else:
         return redirect('login')