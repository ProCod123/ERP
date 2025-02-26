from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Task, TaskFile, TaskPhoto, Stage, Subtask, CustomUser
from .forms import TaskForm, TaskFileForm, TaskPhotoForm, StageForm, SubtaskForm # (forms.py - создайте его отдельно)
from django.http import HttpResponseForbidden

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = project.tasks.all()
    context = {'project': 'project', 'tasks': tasks}
    return render(request, 'project_detail.html', context)


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    stages = task.stages.all()
    files = task.files.all()
    photos = task.photos.all()
    context = {'task': task, 'stages': stages, 'files': files, 'photos': photos}
    return render(request, 'task_detail.html', context)


@login_required
def create_task(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.manager = request.user # Предполагается, что создатель - менеджер
            task.save()
            return redirect('project_detail', pk=project_pk)
    else:
        form = TaskForm()
    context = {'form': form, 'project': project}
    return render(request, 'create_task.html', context)


@login_required
def upload_task_file(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.task = task
            file.save()
            return redirect('task_detail', pk=pk)
    else:
        form = TaskFileForm()
    context = {'form': form, 'task': task}
    return render(request, 'upload_file.html', context)


@login_required
def user_profile(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.user != user:
        return HttpResponseForbidden("Вы не можете просматривать профили других пользователей.")
    context = {'user': user}
    return render(request, 'profile.html', context)

@login_required
def profile_redirect(request):
    user_id = request.user.id
    # Перенаправляем на URL с ID пользователя
    return redirect('user_profile', pk=user_id)