from django.db import models

from user.models import Person as User
from file.models import File


# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=100, unique=True)
    link = models.URLField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    flag = models.CharField(max_length=200)
    solves = models.IntegerField(default=0)
    made_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_files(self):
        return [x.file for x in TaskFile.objects.filter(task__name=self.name)]

    def __str__(self):
        return self.name


class TaskFile(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)

    def __str__(self):
        return self.task.name + " - " + self.file.name


class UserSolve(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + " " + self.task.name
