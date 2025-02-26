
from . import views
from django.urls import path, include

urlpatterns = [
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('projects/<int:project_pk>/create_task/', views.create_task, name='create_task'),
    path('tasks/<int:pk>/upload_file/', views.upload_task_file, name='upload_task_file'),

    path('user_info/profile/', views.profile_redirect, name='profile_redirect'),
    path('profile/<int:pk>/', views.user_profile, name='user_profile'),
    # path('', views.project_detail, name='project_detail'),
    
]
