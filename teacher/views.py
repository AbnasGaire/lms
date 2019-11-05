from django.shortcuts import render
from .forms import Addteacher
from lms.forms import Insertdata
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Teacher
# Create your views here.

def addteacher(request):
    if request.method=="GET":
        context={
            'formteacher':Insertdata
        }
        return render(request,'manager_create_teacher.html',context)
    else:
        form=Insertdata(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully created")
            return redirect('managerdashboard')



def teacherlogin(request):
    if request.method=='GET':
        return redirect('signin')


def teacherdata(request):
    if request.method=='GET':

        content={
            'form': Addteacher,


        }
        return render(request,'teachercreate.html',content)
    else:
        form=Addteacher(request.POST)
        data=form.save(commit=False)
        data.user_id=request.user.id
        data.save()
        return redirect('teacherdashboard')

def viewteacher(request):
    if request.method=='GET':
        a=Teacher.objects.all()
        context={
            'teacher':a
        }
        return render(request,'viewteacher.html',context)

def suspendteacher(request,x):
    a=Teacher.objects.get(id=x)
    a.is_suspend=True
    a.save()
    return redirect('viewteacher')

def continueteacher(request,x):
    a=Teacher.objects.get(id=x)
    a.is_suspend=False
    a.save()
    return redirect('viewteacher')




