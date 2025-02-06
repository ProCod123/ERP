
from django.contrib import admin
from .models import CustomUser, Organization, UserPosition, Department, Project, Task, TaskType, Stage, Subtask, TaskFile, TaskPhoto

admin.site.register(CustomUser)
admin.site.register(Organization)
admin.site.register(UserPosition)
admin.site.register(Department)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(TaskType)
admin.site.register(Stage)
admin.site.register(Subtask)
admin.site.register(TaskFile)
admin.site.register(TaskPhoto)
