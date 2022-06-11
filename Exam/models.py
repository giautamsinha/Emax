from django.db import models

# Create your models here.
class Exam(models.Model):
    courseId=models.IntegerField()
    courseName=models.CharField(max_length=300 , null=True)
    testName=models.CharField(max_length=300 , null=True)
    subjectName=models.CharField(max_length=300 , null=True)
    marks=models.CharField(max_length=100 , null=True)
    negativeMarking=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    examDate=models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.courseName
