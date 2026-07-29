from django.contrib import admin

from .models import HealthProfile, Disease, HealthGoal


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    search_fields = (
        'name',
    )


@admin.register(HealthGoal)
class HealthGoalAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    search_fields = (
        'name',
    )


@admin.register(HealthProfile)
class HealthProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'weight',
        'height',
        'created_at',
    )

    search_fields = (
        'user__username',
        'user__email',
    )

    filter_horizontal = (
        'diseases',
        'goals',
    )