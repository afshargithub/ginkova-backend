from django.contrib import admin

from .models import Recipe, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'preparation_time',
        'cooking_time',
        'is_active',
    )

    search_fields = (
        'name',
    )

    list_filter = (
        'is_active',
    )

    inlines = [
        RecipeIngredientInline,
    ]


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "recipe",
        "ingredient",
        "quantity",
        "unit",
    )

    list_filter = (
        "unit",
    )

    search_fields = (
        "recipe__name",
        "ingredient__name",
    )