from django.http import Http404
from ctf.models import Task, UserSolve


def get_task_info(task_name: str) -> dict:
    if task := Task.objects.filter(name=task_name):
        task = task[0]
        users = UserSolve.objects.filter(task=task)
        return {"users": users, "task": task}
    raise Http404
