from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all() 
    return render(request, "task_list.html", {"tasks": tasks})

def add_task(request):
    if request.method == "POST":
        description = request.POST["description"]
        Task.objects.create(description=description)  
        return redirect("task_list")  
    return render(request, "add_task.html")  

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  
    task.completed = not task.completed  
    task.save() 
    return redirect("task_list")  

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  
    task.delete()  
    return redirect("task_list")  