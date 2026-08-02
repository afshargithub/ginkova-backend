from django.contrib import admin

from .models import (
    Unit,
    UnitTranslation,
)


class UnitTranslationInline(
    admin.TabularInline
):
    model = UnitTranslation

    extra = 0

    fields = (
        "language",
        "name",
    )

    ordering = (
        "language",
    )


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "symbol",
        "unit_type",
        "unit_factor",
        "display_order",
        "is_active",
    )

    list_filter = (
        "unit_type",
        "is_active",
    )

    search_fields = (
        "name",
        "symbol",
        "translations__name",
    )

    ordering = (
        "display_order",
        "name",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    inlines = (
        UnitTranslationInline,
    )