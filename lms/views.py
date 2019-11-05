from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from teacher.models import Teacher
from .forms import Insertdata
from student.models import Student



def home(request):
    if request.method=='GET':
        context={
            'form':Insertdata()
        }
        return render(request,'home.html',context)
    else:
        form=Insertdata(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')

def signin(request):
    if request.method=="GET":
        return render(request,'signin.html')
    else:
        u=request.POST.get('uname')
        p=request.POST.get('password')

        user=authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            id=request.user.id
            a=checkuser(id)
            if a==1:
                b=Teacher.objects.get(user_id=request.user.id)
                if b.is_suspend == True:
                    return redirect('suspend')
                else:
                    return redirect('teacherdashboard')
            elif a==2:

                return redirect('studentdashboard')
            else:
                return redirect('who')

        else:
            messages.error(request,'Username or Password incorrect')
            return redirect('signin')
def managerdash(request):
    if request.method=='GET':
        return render(request,'managerdash.html')

def teacherdasboard(request):
    if request.method=='GET':
        a= Teacher.objects.get(user_id=request.user.id)

        context={
            'teacher':a
            }
        return render(request,'teacherdashboard.html',context)

def who(request):
    return render(request,'who.html')


def checkuser(id):
    try:
        if Teacher.objects.get(user_id=id):
            return 1
    except:
        try:
            if Student.objects.get(user_id=id):
                return 2
        except:
            return 3


def suspend(request):
    if request.method=='GET':
        return render(request,'suspend.html')



