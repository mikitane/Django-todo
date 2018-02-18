from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    LOW_PRIORITY = 3
    NORMAL_PRIORITY = 2
    HIGH_PRIORITY = 1
    PRIORITY_CHOICES = (
        (LOW_PRIORITY,'Low priority'),
        (NORMAL_PRIORITY,'Normal priority'),
        (HIGH_PRIORITY,'High Priority'))


    IDLE = 0
    PROCESS = 1
    DONE = 2
    STATUS_CHOICES = (
        (IDLE,'Idle'),
        (PROCESS,'Process'),
        (DONE,'Done'))
    
    
    user = models.ForeignKey(User)
    text = models.CharField(default='',max_length=50)
    category = models.CharField(default='-',max_length=20)
    priority = models.IntegerField(default=NORMAL_PRIORITY,
                                   choices=PRIORITY_CHOICES)
    status = models.IntegerField(default=IDLE,choices=STATUS_CHOICES)
    created = models.DateField(auto_now_add=True)
    deadline = models.DateField()

