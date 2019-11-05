from django.shortcuts import render
from lms.forms import Insertdata
from django.shortcuts import render,redirect
from .forms import Managerdetail
from django.contrib import messages
# Create your views here.
def addmanager(request):
    if request.method=='GET':
        context={
            'form':Insertdata()
        }
        return render(request,'home.html',context)
    else:
        form=Insertdata(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'managerdetail.html',{'form':Managerdetail})
        else:
            messages.error(request,'Data not valid')
            return redirect('error')

def managerdetail(request):
    if request.method=='GET':
        context={'form':Managerdetail}
        return render(request,'managerdetail.html',context)
    else:
        form=Managerdetail(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.user_id=form.id
def error(request):
    if request.method=='GET':
        return render(request,'error.html')