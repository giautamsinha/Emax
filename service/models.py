from enum import unique
from pyexpat import model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Customer(models.Model):
    duration_service=(
        ('Month' , "30 Days"),
        ('Half Month',"15 Days"),
    )
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    address=models.CharField(max_length=255)
    phone=PhoneNumberField(null=False, unique=True)
    duration=models.CharField(choices=duration_service , max_length=100 , null=True)
    tiffin_start_date=models.DateField(null=True)
    created_on=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name