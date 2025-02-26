from django import forms
from .models import Task, TaskFile, TaskPhoto, Stage, Subtask


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'name', 'task_type', 'address', 'executor', 'deadline']


class TaskFileForm(forms.ModelForm):
    class Meta:
        model = TaskFile
        fields = ['file', 'description']


class TaskPhotoForm(forms.ModelForm):
    class Meta:
        model = TaskPhoto
        fields = ['image', 'description']


class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ['name', 'description', 'deadline']


class SubtaskForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = ['name', 'description', 'executor', 'deadline']
