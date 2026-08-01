from django.contrib import admin

from .models import (
    Ingredient,
    IngredientTranslation,
)


class IngredientTranslationInline(
    admin.TabularInline
):
    model = IngredientTranslation

    extra = 0

    fields = (
        "language",
        "name",
        "description",
    )

    ordering = (
        "language",
    )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "calories",
        "protein",
        "carbohydrate",
        "fat",
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
        "name",
    )

    inlines = (
        IngredientTranslationInline,
    )