from django.contrib import admin

from .models import Ingredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'calories',
        'protein',
        'carbohydrate',
        'fat',
        'is_active',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'name',
    )