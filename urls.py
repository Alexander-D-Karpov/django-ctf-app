from django.urls import path

from .views import *

urlpatterns = [
    path("", task_list, name="index.ctf"),
    path("<str:name>", task_info, name="task"),
]
