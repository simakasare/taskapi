from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    assign= models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    task_description = models.TextField(max_length=200)
    status = models.BooleanField(default=False)
    started = models.DateField(blank=True, null=True)
    completed = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.task_name