from django.contrib import admin

from .models import (
    Meal,
    MealCategory,
    MealCategoryTranslation,
    MealTranslation,
)


class MealCategoryTranslationInline(
    admin.TabularInline
):
    model = MealCategoryTranslation

    extra = 0

    fields = (
        "language",
        "name",
        "description",
    )

    ordering = (
        "language",
    )


class MealTranslationInline(
    admin.TabularInline
):
    model = MealTranslation

    extra = 0

    fields = (
        "language",
        "name",
        "description",
    )

    ordering = (
        "language",
    )


@admin.register(MealCategory)
class MealCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "name",
    )

    inlines = (
        MealCategoryTranslationInline,
    )


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "meal_type",
        "recipe_count",
        "is_featured",
        "is_active",
    )

    list_filter = (
        "meal_type",
        "is_featured",
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "name",
    )

    filter_horizontal = (
        "recipes",
        "categories",
    )

    inlines = (
        MealTranslationInline,
    )

    def recipe_count(self, obj):
        return obj.recipes.count()

    recipe_count.short_description = "Recipes"