from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Teacher(models.Model):
    fullname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    contact=models.IntegerField()
    is_firstlogin=models.BooleanField(default=True ,null=True,blank=True)
    is_suspend=models.BooleanField(default=False,null=True,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return  self.user.username
