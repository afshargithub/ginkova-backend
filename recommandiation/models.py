from django.db import models

from meals.models import Meal
from health.models import (
    HealthGoal,
    Disease,
)


class MealRecommendationRule(models.Model):

    meal = models.ForeignKey(
        Meal,
        on_delete=models.CASCADE,
        related_name='recommendation_rules'
    )


    goal = models.ForeignKey(
        HealthGoal,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )


    disease = models.ForeignKey(
        Disease,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )


    score = models.PositiveIntegerField(
        default=0
    )


    description = models.TextField(
        blank=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):

        return (
            f"{self.meal.name} - "
            f"{self.score}"
        )
        


class NutritionRule(models.Model):

    meal = models.ForeignKey(
        Meal,
        on_delete=models.CASCADE,
        related_name='nutrition_rules'
    )


    max_calories = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )


    min_protein = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )


    max_fat = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )


    score = models.PositiveIntegerField(
        default=0
    )


    description = models.TextField(
        blank=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):

        return (
            f"{self.meal.name} Nutrition Rule"
        )
        
