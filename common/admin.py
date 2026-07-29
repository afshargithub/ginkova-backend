from django.contrib import admin

from .models import Unit


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
    )

    ordering = (
        "display_order",
        "name",
    )