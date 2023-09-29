from django.db import models

Priorities= [
    ('low', 'Low Priority'),
    ('medium', 'Medium Priority'),
    ('high', 'High Priority'),
    
]


class Task(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    progress = models.IntegerField(default=0)
    priority = models.CharField(max_length=20, choices=Priorities, default='Low Priority')
    Reminder = models.BooleanField(default=False)

    @property
    def get_actionItems(self):
        ActonItems = self.taskactionitem_set.all()
        return ActonItems

    def __str__(self):
        return self.name

class TaskActionItem(models.Model):
    title = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)
    task = models.ForeignKey(Task, related_name="actionItems", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
