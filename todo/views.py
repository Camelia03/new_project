from django.shortcuts import render, redirect
from .models import Task

# Create your views here.


def get_todo_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'todo/todo_list.html', context)


def add_task(request):
    if request.method == 'POST':
        name = request.POST.get('task_name')
        done = 'done' in request.POST
        Task.objects.create(name=name, done=done)

        return redirect('get_todo_list')
    return render(request, 'todo/add_task.html')
