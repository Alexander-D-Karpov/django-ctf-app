from django.db.models import F

from ctf.models import Task, UserSolve
from user.models import Person
from secrets import compare_digest


def submit_task(task_name: str, user: Person, flag: str) -> str:
    """validates flag and task and creates userSolve"""
    if task := Task.objects.filter(name=task_name):
        task = task[0]
    else:
        return "Task doesn't exist or was deleted"

    if UserSolve.objects.filter(user=user, task=task).exists():
        return "task is already solved"

    if len(flag) > 200:
        return "flag is too long"

    if "{" in flag:
        flag = flag.split("{")[1][:-1]

    if compare_digest(flag, task.flag):
        UserSolve.objects.create(user=user, task=task)
        task.solves = F("solves") + 1
        user.solves = F("solves") + 1
        task.save(update_fields=["solves"])
        user.save(update_fields=["solves"])
        return "you are right!"

    return "flag is not correct"
