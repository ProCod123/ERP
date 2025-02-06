from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True)
    position = models.ForeignKey('UserPosition', on_delete=models.SET_NULL, related_name='users', null=True, blank=True)
    organization = models.ForeignKey('Organization', on_delete=models.SET_NULL, related_name='users', null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, related_name='users', null=True, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Organization(models.Model):
    organization = models.CharField(max_length=100)

    def __str__(self):
        return self.organization
    
    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class UserPosition(models.Model):
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.position
    
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Department(models.Model):
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.department
    
    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    manager = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_projects')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=255)
    task_type = models.ForeignKey('TaskType', on_delete=models.CASCADE, related_name='tasks')
    address = models.CharField(max_length=255, blank=True)
    executor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='executed_tasks')
    manager = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_tasks')
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class TaskType(models.Model):
    task_type = models.CharField(max_length=50)

    def __str__(self):
        return self.task_type
    
    class Meta:
        verbose_name = 'Тип задачи'
        verbose_name_plural = 'Типы задач'


class TaskFile(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='task_files/')
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File for task {self.task.name}"
    
    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class TaskPhoto(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='task_photos/')
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo for task {self.task.name}"
    
    class Meta:
        verbose_name = 'Фотографии'
        verbose_name_plural = 'Фотографии'


class Stage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='stages')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Этап'
        verbose_name_plural = 'Этапы'


class Subtask(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, related_name='subtasks')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    executor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='subtasks')
    deadline = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Подзадача'
        verbose_name_plural = 'Подзадачи'