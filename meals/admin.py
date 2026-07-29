from django.contrib import admin

from .models import Meal, MealCategory


@admin.register(MealCategory)
class MealCategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
    )

    search_fields = (
        'name',
    )


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'meal_type',
        'recipe_count',
        'is_featured',
        'is_active',
    )


    list_filter = (
        'meal_type',
        'is_active',
    )


    search_fields = (
        'name',
    )


    filter_horizontal = (
        'recipes', 
        'categories',
    )


    def recipe_count(self, obj):

        return obj.recipes.count()


    recipe_count.short_description = "Recipes"