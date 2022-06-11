# from ast import Not
# from cgitb import reset
# from email import message
# import json
import random
from pyexpat.errors import messages
# import re
# from unicodedata import name
# from urllib import request
# from django import http
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import User
import uuid
from .utils import *
from django.contrib.auth import authenticate,  login as dj_login, logout
from django.core import serializers
from django.http import JsonResponse
import csv
# Create your views here.


def register(request):
    try:
        if request.method == "POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            contact_number = request.POST['contact_number']
            email = request.POST['email']
            password = request.POST['password']
            c_password = request.POST['c_password']
            email_token = str(uuid.uuid4())
            if password == c_password:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already Exist')
                    return redirect('register')
                else:
                    if User.objects.filter(phone=contact_number).exists():
                        messages.error(request, 'Contact number already Exist')
                        return redirect('register')
                    else:
                        name = first_name + " " + last_name
                        sendEmail = send_email_token(email, email_token, name)
                        if sendEmail:
                            User.objects.create_user(name=name ,
                                                     phone=contact_number, email=email, password=password, email_token=email_token)
                            messages.success(
                                request, 'You are register successfuly')
                            return redirect('register')
                        else:
                            messages.error(request, 'Somthin went wrong')
                            return redirect('register')
            else:
                messages.error(request, 'Password do not match')
                return redirect('register')
        else:
            return render(request, 'accounts/register.html')
    except Exception as e:
        messages.error(request, 'Password do not match')
        return redirect('register')

@csrf_protect
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            if User.objects.filter(email=email, is_verified=True).exists():
                if User.objects.filter(email=email, is_verified=True, is_active=True):
                    if User.objects.filter(email=email, is_verified=True, is_active=True, is_admin=True):
                        user = authenticate(email=email, password=password)
                        if user is not None:
                            dj_login(request, user)
                            return redirect("dashboard")
                        else:
                            return HttpResponse("somthing worng")
                    else:
                        return HttpResponse("hdfgfd")
                else:
                    messages.error(
                        request, "Your account was de-activated by admin !")
                    return redirect('login')
            else:
                messages.error(request, "Please verfiy your email !")
                return redirect('login')
        else:
            messages.error(request, "Email Not Found")
            return redirect('login')
    else:
       return render(request, 'accounts/login.html')


def verify(request, token):
    try:
        user = User.objects.get(email_token=token)
        user.is_verified = True
        user.is_active = True
        user.save()
        messages.success(request, 'Your account is verified')
        return redirect('register')
    except Exception as e:
        messages.error(request, 'Somthin went wrong')
        return redirect('register')


def resetpassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            resetPasswordToken = random.randint(1111, 9999)
            users = User.objects.get(email=email)
            name = users.name
            sendEmail = send_password_token(email, resetPasswordToken, name)
            if sendEmail:
                users.reset_password_token = resetPasswordToken
                users.save()
                messages.success(request, 'OTP send to ypur register email id')
                return redirect('resetpassword')
            else:
                return HttpResponse("dbhjfh")

        else:
            messages.error(request, 'Email is invalid')
            return redirect('resetpassword')
    else:
        return render(request, 'accounts/reset_password.html')


def logout_request(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Logout successfully ! ')
        return redirect('login')

    # logout(request)
    # messages.success(request,'OTP send to ypur register email id')
    # return redirect('logout')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'layouts/admin_dashboard.html')
    else:
         return redirect('login')

   
def studentList(request):
    if request.user.is_authenticated:
         if request.method == 'POST':
            course = request.POST['myselect']
            if course == "All":
                studentList = User.objects.filter(is_student=True , hide=False)
                return render(request, 'layouts/student_list.html', {'student_list': studentList})
            else:
                studentList = User.objects.filter(is_student=True , hide=False , course = course)
                return render(request, 'layouts/student_list.html', {'student_list': studentList})
         else:
            studentList = User.objects.filter(is_student=True , hide=False)
            return render(request, 'layouts/student_list.html', {'student_list': studentList})
            # return HttpResponse("2")

    else:
        return HttpResponse("k")


def changeStatus(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        changestatus = request.POST.get('status')
        if student_id != "" and changestatus == "activate" and User.objects.filter(id=student_id).exists():
            user = User.objects.get(id=student_id)
            user.is_active = True
            user.save()
            response = HttpResponse({'Success': 'Successss'})
            response.status_code = 200
            return response
        if student_id != "" and changestatus == "deactivate" and User.objects.filter(id=student_id).exists():
            user = User.objects.get(id=student_id)
            user.is_active = False
            user.save()
            response = HttpResponse({'Success': 'Successsss'})
            response.status_code = 200
            return response
        else:
            pass

    #   response = HttpResponse({'else':'else'})
    #   response.status_code = 200
    #   return response


def viewStudentDetails(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        if student_id != "" and User.objects.filter(id=student_id).exists():
                user = User.objects.values().filter(id=student_id)
                student=list(user)
                return JsonResponse({'Success': 'Successss' , 'user':student})
        else:
                response = HttpResponse({'else': 'else'})
                response.status_code = 200
                return response
    else:
        response = HttpResponse({'else': 'else'})
        response.status_code = 400
        return response


def updateStudentDetails(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        # zipcode = request.POST.get('zipcode')
        if student_id != "" and User.objects.filter(id=student_id).exists():
            user = User.objects.get(id=student_id)
            user.name=name
            user.email=email
            user.address=address
            user.phone=number
            # user.zipcode=zipcode
            user.save()
            response = HttpResponse({'Success': 'Success'})
            response.status_code = 200
            return response
        else:
            pass
    else:
        pass

def deleteStudent(request):
     if request.method == 'POST':
        student_id = request.POST.get('student_id')
        if student_id != "" and User.objects.filter(id=student_id).exists():
             user = User.objects.get(id=student_id)
             user.delete()
             response = HttpResponse({'Success': 'Success'})
             response.status_code = 200
             return response



def hideStudent(request):
     if request.method == 'POST':
        student_id = request.POST.get('student_id')
        if student_id != "" and User.objects.filter(id=student_id).exists():
             user = User.objects.get(id=student_id)
             user.hide=True
             user.save()
             response = HttpResponse({'Success': 'Success'})
             response.status_code = 200
             return response



def exportStudentList(request):
    if request.user.is_authenticated:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Student.csv"'
        writer = csv.writer(response)
        writer.writerow(['Student Name','Father Name', 'Phone', 'Email', 'Address', 'Zipcode', 'Course', 'Addhar NUmber', 'Fees'])
        student = User.objects.all().values_list('name','fatherName', 'phone', 'email', 'address', 'zipcode', 'course', 'addharNumber', 'fees')
        for user in student:
            writer.writerow(user)
        return response
    else:
        return redirect('login')
        


def payment(request):
    if request.user.is_authenticated:
        studentList = User.objects.filter(is_student=True)
        return render(request, 'layouts/payment.html',  {'student_list': studentList})
    else:
        return redirect('login')




def testing(request):
    return HttpResponse(request)