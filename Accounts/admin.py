from django.contrib import admin
from .models import  User
# Register your models here.
admin.site.register(User)
# admin.site.register(Role)



# from email.mime import image
# from email.policy import default
# from turtle import mode
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.utils.translation import gettext_lazy as _
# from .managers import UserManager
# Create your models here.


# class Role(models.Model):
#     '''
#     The Role entries are managed by the system,
#     automatically created via a Django data migration.
#     '''
#     STUDENT = 1
#     TEACHER = 2
#     ADMIN = 3
#     ROLE_CHOICES = (
#         (STUDENT, 'student'),
#         (TEACHER, 'teacher'),
#         (ADMIN, 'admin'),
#     )

#     id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

#     def __str__(self):
#       return self.get_id_display()

# class User(AbstractBaseUser, PermissionsMixin):
#     username = None
#     name = models.CharField(_('First Nmae'), max_length=200)
#     fatherName    = models.CharField(max_length=200, null=True )
#     # last_name  = models.CharField(_('Last Name'), max_length=200)
#     email      = models.EmailField(_('Email address'), unique=True)
#     phone      = models.CharField(_('Contact Number'), unique=True, max_length=12)
#     address    = models.CharField(_('Address'), max_length=200 ,  null=True)
#     zipcode    = models.IntegerField(_('ZipCode') , null=True )
#     course    = models.CharField(max_length=200, null=True )
#     email_token = models.CharField(max_length=200, null=True ,blank=False)
#     reset_password_token = models.CharField(max_length=5 , null=True , blank=False)
#     is_verified =models.BooleanField(default=False)
#     is_active  = models.BooleanField(default=False)
#     is_staff   = models.BooleanField(default=False)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     objects=UserManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name','phone']

#     def __str__(self):
#         return self.email
