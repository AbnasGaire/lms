from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    fullname=models.CharField(max_length=100)
    enrolled_course=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    contact=models.IntegerField()
    is_firstlogin=models.BooleanField(default=True)
    is_suspend=models.BooleanField(default=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        self.user.username
