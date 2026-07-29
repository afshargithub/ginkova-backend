from django.contrib import admin

from .models import (
    MealRecommendationRule,
    NutritionRule,
)


@admin.register(MealRecommendationRule)
class MealRecommendationRuleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'meal',
        'goal',
        'disease',
        'score',
        'created_at',
    )


    list_filter = (
        'goal',
        'disease',
        'score',
    )


    search_fields = (
        'meal__name',
        'goal__name',
        'disease__name',
    )


    readonly_fields = (
        'created_at',
        'updated_at',
    )



@admin.register(NutritionRule)
class NutritionRuleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'meal',
        'max_calories',
        'min_protein',
        'max_fat',
        'score',
        'created_at',
    )


    list_filter = (
        'score',
    )


    search_fields = (
        'meal__name',
    )


    readonly_fields = (
        'created_at',
        'updated_at',
    )