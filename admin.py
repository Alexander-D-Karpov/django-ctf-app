from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(TaskFile)


@admin.register(Task)
class RateAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "solves", "made_by")
    list_filter = ("solves", "made_by")
    search_fields = ("name", "flag")


@admin.register(UserSolve)
class RateAdmin(admin.ModelAdmin):
    list_display = ("user", "task", "time")
    list_filter = ("user", "task")
