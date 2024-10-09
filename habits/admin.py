from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "action",
    )
