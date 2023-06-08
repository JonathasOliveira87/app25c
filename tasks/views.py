from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Task
from datetime import datetime
from .forms import TaskForm

@login_required
def taskList(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')

    if search:
        tasks_search = Task.objects.filter(title__icontains=search)
        return render(request, 'search.html', {'tasks_search': tasks_search, 'search_query': search})
    elif filter == 'all':
        tasks_search = Task.objects.all()
    elif filter:
        tasks_search = Task.objects.filter(Escala=filter)
        return render(request, 'list.html', {'tasks_search': tasks_search, 'search_query': filter})
    
    
    now = datetime.now()

    open_tasks_list = Task.objects.filter(EndTime__gte=now, done='doing').order_by('-created_task')
    closed_tasks_list = Task.objects.filter(done='done').order_by('-created_task')
    fail_tasks_list = Task.objects.filter(EndTime__lt=now, done='fail').order_by('-created_task')

    open_paginator = Paginator(open_tasks_list, 4)
    closed_paginator = Paginator(closed_tasks_list, 4)
    fail_paginator = Paginator(fail_tasks_list, 4)

    open_page = request.GET.get('open_page')
    closed_page = request.GET.get('closed_page')
    fail_page = request.GET.get('fail_page')

    open_tasks = open_paginator.get_page(open_page)
    closed_tasks = closed_paginator.get_page(closed_page)
    fail_tasks = fail_paginator.get_page(fail_page)

    return render(request, 'list.html', {'open_tasks': open_tasks, 'closed_tasks': closed_tasks, 'fail_tasks': fail_tasks})


@login_required
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'task.html', {'task': task})


@login_required
def updateTask(request, id):
    task = get_object_or_404(Task, pk=id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm(instance=task)

    return render(request, 'task.html', {'form': form, 'task': task})