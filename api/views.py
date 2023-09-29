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
        # tasks = Task.objects.all()
        # serializer = TaskSerializer(tasks, many=True)
        # return Response(serializer.data)
    
    if request.method == 'POST':
        return createTask(request)
        # data = request.data
        # action_items_data = data['actionItems']
        # actionItems = action_items_data['actionItems']
        # task = Task.objects.create(
        #     name = data['name'],
        #     priority = data['priority'],
        #     date = data['date'],
        #     Reminder = data['reminder'],    
        # )   
        # for item in actionItems:
        #     TaskActionItem.objects.create(
        #         title = item,
        #         task = task,
        #         complete=False,
        #     )
        # serializer = TaskSerializer(task, many=False)
        # return Response(serializer.data)
    
    if request.method == 'DELETE':
        return delTasks(request)
        # tasks = tasks = Task.objects.all()
        # tasks.delete()
        # return Response('Tasks deleted!')
    

@api_view(['GET', 'DELETE', 'PUT'])
def Taskk(request, TaskId):
    if request.method == 'GET':
        return getTask(request, TaskId)
        # task = Task.objects.get(id=TaskId)
        # serializer = TaskSerializer(task, many=False)
        # return Response(serializer.data)
    
    if request.method == 'DELETE':
        return delTask(request, TaskId)
        # task = Task.objects.get(pk=TaskId)
        # task.delete()
        # return Response('Task was deleted!')

    if request.method == 'PUT':
        return changePriority(request, TaskId)
        # data = request.data
        # task = Task.objects.get(id=TaskId)
        # task.priority = data['priority']
        # task.save()
        # serializer = TaskSerializer(task, many=False)
        # return Response(serializer.data)


@api_view(['PATCH', 'DELETE'])
def ActionItem(request, TaskId, action_item_id):
    if request.method == 'PATCH':
        return chkActionItemUpdProgress(request, TaskId, action_item_id)
        # data = request.data
        # task = Task.objects.get(id=TaskId)
        # actionItem = TaskActionItem.objects.get(pk=action_item_id)
        # actionItem.complete = data['complete']
        # actionItem.save()
        # task.progress = data['progress'] 
        # task.save()  
        # serializer = TaskSerializer(task, many=False)
        # return Response(serializer.data)
    
    if request.method == 'DELETE':
        return delActionItem(request, TaskId, action_item_id)
        # action_item = TaskActionItem.objects.get(pk=action_item_id)
        # action_item.delete()
        # return Response('Note was deleted!')


# @api_view(['PUT'])
# def changePriority(request, TaskId):
#     data = request.data
#     task = Task.objects.get(id=TaskId)
#     task.priority = data['priority']
#     task.save()
#     serializer = TaskSerializer(task, many=False)
#     return Response(serializer.data)

# @api_view(['DELETE'])
# def delActonItem(request, itemId):
#     action_item = TaskActionItem.objects.get(pk=itemId)
#     action_item.delete()
#     return Response('Note was deleted!')

# @api_view(['DELETE'])
# def delTask(request, TaskId):
#     task = Task.objects.get(pk=TaskId)
#     task.delete()
#     return Response('Task was deleted!')

# @api_view(['DELETE'])
# def delAllTasks(request):
#     tasks = tasks = Task.objects.all()
#     tasks.delete()
#     return Response('Tasks deleted!')


# @api_view(['POST'])
# def createTask(request):
#     data = request.data
#     action_items_data = data['actionItems']
#     actionItems = action_items_data['actionItems']
#     task = Task.objects.create(
#         name = data['name'],
#         priority = data['priority'],
#         date = data['date'],
#         Reminder = data['reminder'],    
#     )   
#     for item in actionItems:
#         TaskActionItem.objects.create(
#             title = item,
#             task = task,
#             complete=False,
#         )
#     serializer = TaskSerializer(task, many=False)
#     return Response(serializer.data)