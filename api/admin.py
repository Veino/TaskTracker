from django.contrib import admin
from .models import Task, TaskActionItem

# Register your models here.

admin.site.register(Task)
admin.site.register(TaskActionItem)
