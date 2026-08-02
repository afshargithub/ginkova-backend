from django.conf import settings
from django.db import models

from recipes.models import Recipe


class MealCategory(models.Model):
    name = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        blank=True,
    )

    image = models.ImageField(
        upload_to="meal_categories/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
    
    
class MealCategoryTranslation(models.Model):
    meal_category = models.ForeignKey(
        MealCategory,
        on_delete=models.CASCADE,
        related_name="translations",
    )

    language = models.CharField(
        max_length=10,
        choices=settings.LANGUAGES,
    )

    name = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "meal_category",
                    "language",
                ],
                name=(
                    "unique_meal_category_translation_language"
                ),
            ),
        ]

        ordering = [
            "meal_category_id",
            "language",
        ]

    def __str__(self):
        return (
            f"{self.meal_category.name} "
            f"({self.language})"
        )


class Meal(models.Model):
    MEAL_TYPE_CHOICES = (
        ("breakfast", "Breakfast"),
        ("lunch", "Lunch"),
        ("dinner", "Dinner"),
    )

    name = models.CharField(
        max_length=150,
    )

    description = models.TextField(
        blank=True,
    )

    image = models.ImageField(
        upload_to="meals/",
        blank=True,
        null=True,
    )

    meal_type = models.CharField(
        max_length=20,
        choices=MEAL_TYPE_CHOICES,
    )

    recipes = models.ManyToManyField(
        Recipe,
    )

    categories = models.ManyToManyField(
        MealCategory,
        blank=True,
    )

    is_featured = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class MealTranslation(models.Model):
    meal = models.ForeignKey(
        Meal,
        on_delete=models.CASCADE,
        related_name="translations",
    )

    language = models.CharField(
        max_length=10,
        choices=settings.LANGUAGES,
    )

    name = models.CharField(
        max_length=150,
    )

    description = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "meal",
                    "language",
                ],
                name=(
                    "unique_meal_translation_language"
                ),
            ),
        ]

        ordering = [
            "meal_id",
            "language",
        ]

    def __str__(self):
        return (
            f"{self.meal.name} "
            f"({self.language})"
        )