from django.contrib import admin

from .models import (
    Recipe,
    RecipeIngredient,
    RecipeTranslation,
)


class RecipeTranslationInline(
    admin.TabularInline
):
    model = RecipeTranslation

    extra = 0

    fields = (
        "language",
        "name",
        "description",
    )

    ordering = (
        "language",
    )


class RecipeIngredientInline(
    admin.TabularInline
):
    model = RecipeIngredient

    extra = 0

    fields = (
        "ingredient",
        "quantity",
        "unit",
    )

    autocomplete_fields = (
        "ingredient",
    )


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "preparation_time",
        "cooking_time",
        "ingredient_count",
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
        RecipeTranslationInline,
        RecipeIngredientInline,
    )

    def ingredient_count(self, obj):
        return obj.ingredients.count()

    ingredient_count.short_description = (
        "Ingredients"
    )