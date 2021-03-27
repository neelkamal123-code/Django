from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Tasks
from .forms import CreateTask
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def homepage(request):
    ## tasks of particular user
    all_tasks_of_user = Tasks.objects.filter(user=request.user)# name of user
    if request.method == "POST":
        fm = CreateTask(request.POST)
        if fm.is_valid():
            obj = fm.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request,"Item Added")
            fm = CreateTask()
    else:
        fm = CreateTask()
    return render(request,'tasks/home.html',{'tasks':all_tasks_of_user,'form':fm,'user':request.user})
## delete request / Done button
@login_required(login_url='/login/')
def delete(request,myid):
    task_to_delete = Tasks.objects.get(id=myid)
    task_to_delete.delete()
    messages.warning(request,"Item Deleted")
    return HttpResponseRedirect('/homepage/')

## edit button
@login_required(login_url='/login/')
def edit(request,myid):
    user = Tasks.objects.get(id=myid)
    if request.method == "POST":
        fm = CreateTask(request.POST,instance=user)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Item Updated")
    else:
        fm = CreateTask(instance=user)

    return render(request,'tasks/edit.html',{'form':fm})

## clear all button
@login_required(login_url='/login/')
def clear_all(request):
    all_tasks = Tasks.objects.all()
    for task in all_tasks:
        task.delete()
    messages.success(request,'All Cleared :)')
    return HttpResponseRedirect('/homepage/')

## Signup form
def signup_form(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'User Registered Successfully')
            fm = UserCreationForm()
    else:
        fm  = UserCreationForm()
    return render(request,'tasks/signup.html',{'form':fm})

## Login Form
def login_form(request):
    if request.method=="POST":
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/homepage/')

    else:
        fm = AuthenticationForm(request=request)
    return render(request,'tasks/login.html',{'form':fm,'user':request.user})

## logout functionality
@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')

## change password functionality
@login_required(login_url='/login/')
def password_change_form(request):
    if request.method == "POST":
        fm = PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Password Changed :)')
            return HttpResponseRedirect('/login/')
    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request,'tasks/passchange.html',{'form':fm})