from rest_framework.serializers import ModelSerializer
from .models import Task, TaskActionItem

class TaskActionItemSerializer(ModelSerializer):
    class Meta:
        model = TaskActionItem
        fields = ['title', 'complete', 'id']

class TaskSerializer(ModelSerializer):
    actionItems = TaskActionItemSerializer(many=True)
    class Meta:
        model = Task
        fields ='__all__'
    