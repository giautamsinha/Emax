from django import views
from . import views
from unicodedata import name
from django.urls import path
urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout_request, name="logout"),

    path('register/', views.register, name="register"),
    path('resetpassword/', views.resetpassword, name="resetpassword"),
    path('verify/<token>/', views.verify, name="verify"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('studentList', views.studentList, name="studentList"),
    path('changeStatus', views.changeStatus, name="changeStatus"),
    path('viewStudentDetails', views.viewStudentDetails, name="viewStudentDetails"),
    path('updateStudentDetails ', views.updateStudentDetails , name="updateStudentDetails"),
    path('deleteStudent', views.deleteStudent , name="deleteStudent"),
    path('hideStudent', views.hideStudent , name="hideStudent"),
    path('exportStudentList', views.exportStudentList , name="exportStudentList"),
    path('payment', views.payment , name="payment"),
    path('testing', views.testing , name="testing"),








]
