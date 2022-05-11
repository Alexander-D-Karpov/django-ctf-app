from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

from .services.get_task_info import get_task_info
from .services.get_tasks import get_tasks
from .services.get_user_solves import get_user_solves
from .services.submit_task import submit_task


def task_list(request):
    massage = None

    if request.method == "POST":
        massage = submit_task(request.POST["name"], request.user, request.POST["flag"])

    return render(
        request,
        "ctf/index.html",
        context={
            "tasks": get_tasks(),
            "solved": get_user_solves(request.user),
            "massage": massage,
        },
    )


def task_info(request, name):
    return render(request, "ctf/task-info.html", get_task_info(name))
