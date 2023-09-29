from django.urls import path

from . import views

urlpatterns = [
    path('', views.getRoutes, name="index"),
    path('tasks/', views.Tasks, name="tasks"),
    # path('tasks/create/', views.createTask, name="createTask"),
    # path('task/delete-action-item/<str:itemId>', views.delActonItem, name='delete_action_item'),
    # path('tasks/delete-all/', views.delAllTasks, name="delete-all-tasks"),
    # path('tasks/<str:TaskId>/delete/', views.delTask, name="delete-task"),
    path('tasks/<str:TaskId>/actionitems/<str:action_item_id>', views.ActionItem, name="action-item-update-del"),
    # path('task/<str:TaskId>/change-priority', views.changePriority, name='change-priority'),
    path('tasks/<str:TaskId>/', views.Taskk, name="task"),
]