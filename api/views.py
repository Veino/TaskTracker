from django.shortcuts import render
from django.http import JsonResponse
from .models import Task, TaskActionItem
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskSerializer, TaskActionItemSerializer
from .utils import *

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'HTTP Method': 'GET',
            'Endpoint': '/api/tasks',
            'Description': 'Retrieves a list of all tasks.'
        },
        {
            'HTTP Method': 'DELETE',
            'Endpoint': '/api/tasks',
            'Description': 'Deletes all tasks.'

        },
        {
            'HTTP Method': 'POST',
            'Endpoint': '/api/tasks',
            'Description': 'Creates a new task'

        },
        {
            'HTTP Method': 'GET',
            'Endpoint': '/api/tasks/{id}',
            'Description': 'Retrieves a single task by its unique identifier.'

        },
        {
            'HTTP Method': 'DELETE',
            'Endpoint': '/api/tasks/{id}',
            'Description': 'Deletes a task by its unique identifier.'

        },
        {
            'HTTP Method': 'PUT',
            'Endpoint': '/api/tasks/{id}',
            'Description': 'Updates the priority of a task.'
        },
        {
           'HTTP Method': 'PATCH',
            'Endpoint': '/api/tasks/{id}/actionitems/{action_item_id}',
            'Description': 'Updates the progress of an action item within a task.'
        },
        {
            'HTTP Method': 'DELETE',
            'Endpoint': '/api/tasks/{id}/actionitems/{action_item_id}',
            'Description': 'Deletes an action item within a task.'
        },
    ]

    return Response(routes)


@api_view(['GET', 'POST', 'DELETE'])
def Tasks(request):
    if request.method == 'GET':
        return getTasks(request)
    
    if request.method == 'POST':
        return createTask(request)
    
    if request.method == 'DELETE':
        return delTasks(request)
    

@api_view(['GET', 'DELETE', 'PUT'])
def Taskk(request, TaskId):
    if request.method == 'GET':
        return getTask(request, TaskId)
    
    if request.method == 'DELETE':
        return delTask(request, TaskId)

    if request.method == 'PUT':
        return changePriority(request, TaskId)


@api_view(['PATCH', 'DELETE'])
def ActionItem(request, TaskId, action_item_id):
    if request.method == 'PATCH':
        return chkActionItemUpdProgress(request, TaskId, action_item_id)
    
    if request.method == 'DELETE':
        return delActionItem(request, TaskId, action_item_id)
