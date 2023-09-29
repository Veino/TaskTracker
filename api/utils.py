from django.shortcuts import render
from django.http import JsonResponse
from .models import Task, TaskActionItem
from rest_framework.response import Response
from .serializers import TaskSerializer, TaskActionItemSerializer

def getTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
    
def createTask(request):   
    data = request.data
    action_items_data = data['actionItems']
    actionItems = action_items_data['actionItems']
    task = Task.objects.create(
        name = data['name'],
        priority = data['priority'],
        date = data['date'],
        Reminder = data['reminder'],    
    )   
    for item in actionItems:
        TaskActionItem.objects.create(
            title = item,
            task = task,
            complete=False,
        )
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

def delTasks(request):   
    tasks = tasks = Task.objects.all()
    tasks.delete()
    return Response('Tasks deleted!')
    

def getTask(request, TaskId):
    task = Task.objects.get(id=TaskId)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

def delTask(request, TaskId):
    task = Task.objects.get(pk=TaskId)
    task.delete()
    return Response('Task was deleted!')

def changePriority(request, TaskId):
    data = request.data
    task = Task.objects.get(id=TaskId)
    task.priority = data['priority']
    task.save()
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


def chkActionItemUpdProgress(request, TaskId, action_item_id):
    data = request.data
    task = Task.objects.get(id=TaskId)
    actionItem = TaskActionItem.objects.get(pk=action_item_id)
    actionItem.complete = data['complete']
    actionItem.save()
    task.progress = data['progress'] 
    task.save()  
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

def delActionItem(request, TaskId, action_item_id):
    action_item = TaskActionItem.objects.get(pk=action_item_id)
    action_item.delete()
    return Response('Note was deleted!')