from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Tasks
from .forms import CreateTask,EditForm
from django.contrib import messages
# Create your views here.
def homepage(request):
    all_tasks = Tasks.objects.all()
    if request.method == "POST":
        fm = CreateTask(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Item Added")
            fm = CreateTask()
    else:
        fm = CreateTask()
    return render(request,'tasks/home.html',{'tasks':all_tasks,'form':fm})

def delete(request,myid):
    task_to_delete = Tasks.objects.get(id=myid)
    task_to_delete.delete()
    messages.warning(request,"Item Deleted")
    return HttpResponseRedirect('/')

def edit(request,myid):
    user = Tasks.objects.get(id=myid)
    if request.method == "POST":
        fm = EditForm(request.POST,instance=user)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Item Updated")
    else:
        fm = EditForm(instance=user)

    return render(request,'tasks/edit.html',{'form':fm})

def clear_all(request):
    all_tasks = Tasks.objects.all()
    for task in all_tasks:
        task.delete()
    return HttpResponseRedirect('/')
