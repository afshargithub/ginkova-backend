from django.contrib import admin

from .models import (
    Disease,
    DiseaseTranslation,
    HealthGoal,
    HealthGoalTranslation,
    HealthProfile,
)


class HealthGoalTranslationInline(
    admin.TabularInline
):
    model = HealthGoalTranslation

    extra = 0

    fields = (
        "language",
        "name",
        "description",
    )

    ordering = (
        "language",
    )


class DiseaseTranslationInline(
    admin.TabularInline
):
    model = DiseaseTranslation

    extra = 0

    fields = (
        "language",
        "name",
        "description",
    )

    ordering = (
        "language",
    )


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )

    search_fields = (
        "name",
        "description",
        "translations__name",
        "translations__description",
    )

    ordering = (
        "name",
    )

    inlines = (
        DiseaseTranslationInline,
    )


@admin.register(HealthGoal)
class HealthGoalAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "display_order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "description",
        "translations__name",
        "translations__description",
    )

    ordering = (
        "display_order",
        "name",
    )

    inlines = (
        HealthGoalTranslationInline,
    )


@admin.register(HealthProfile)
class HealthProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "weight",
        "height",
        "created_at",
    )

    search_fields = (
        "user__username",
        "user__email",
    )

    filter_horizontal = (
        "diseases",
        "goals",
    )