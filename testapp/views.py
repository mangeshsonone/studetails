from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import studentform,userform,userplainform
from django.contrib.auth.models import User
from .models import student

def studentdetails(request):
    if request.method=='POST':
        fm=studentform(request.POST)
        if fm.is_valid():
            # fm.save()
            print('hi')
            name=fm.cleaned_data['name']
            address=fm.cleaned_data['address']
            student.objects.create(name=name,address=address)
            
    fm=studentform()
    return render(request,'detail.html',{'form':fm})


def userdetails(request):
    fm=userform()
    return render(request,'user.html',{'form':fm})

def userplaindetails(request):
    if request.method=='POST':
        fm=userplainform(request.POST)
        if fm.is_valid():
            fm.save()
    fm=userplainform()
    return render(request,'userplain.html',{'form':fm})

def userbasicdetails(request):
    if request.method=='POST':
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['username']
            passw=fm.cleaned_data['password1']
            print(passw)
            User.objects.create(username=name,password=passw)
    fm=UserCreationForm()
    return render(request,'userbasic.html',{'form':fm})
