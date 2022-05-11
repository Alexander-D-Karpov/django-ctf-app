from ctf.models import Task


def get_tasks() -> list[Task]:
    tasks = sorted(Task.objects.all(), key=lambda x: x.id, reverse=True)
    return tasks
