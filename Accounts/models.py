from email.mime import image
from email.policy import default
from turtle import mode
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    name = models.CharField(_('First Nmae'), max_length=200)
    fatherName    = models.CharField(max_length=200, null=True )
    email      = models.EmailField(_('Email address'), unique=True)
    phone      = models.CharField(_('Contact Number'), unique=True, max_length=12)
    is_admin   = models.BooleanField('Is admin' , default=False)
    is_student = models.BooleanField('Is student' , default=False)
    address    = models.CharField(_('Address'), max_length=200 ,  null=True)
    zipcode    = models.IntegerField(_('ZipCode') , null=True )
    course    = models.CharField(max_length=200, null=True )
    addharNumber    = models.CharField(max_length=200, null=True )
    fees   = models.CharField(max_length=200)
    feesStatus   = models.BooleanField(default=False)
    hide =models.BooleanField(default=False)
    email_token = models.CharField(max_length=200, null=True ,blank=False)
    reset_password_token = models.CharField(max_length=5 , null=True , blank=False)
    is_verified =models.BooleanField(default=False)
    is_staff   = models.BooleanField(default=False)
    is_active  = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone']

    def __str__(self):
        return self.email
