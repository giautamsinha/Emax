from django.utils import timezone
from django.db import models

# Create your models here.
class Questions(models.Model):
    question=models.CharField(max_length=500,null=True)
    optionA=models.CharField(max_length=200 ,null=True)
    optionB=models.CharField(max_length=200 ,null=True)
    optionC=models.CharField(max_length=200 ,null=True)
    optionD=models.CharField(max_length=200 ,null=True)
    correctAnswer=models.CharField(max_length=200 ,null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.question


class Csv_Files(models.Model):
    csvFilePath=models.FileField(upload_to='documents/')
    importID=models.CharField(max_length=200,null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.csvFilePath