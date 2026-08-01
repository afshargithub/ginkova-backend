from django.conf import settings
from django.db import models

from common.models import Unit
from ingradients.models import Ingredient


class Recipe(models.Model):
    name = models.CharField(
        max_length=150,
    )

    description = models.TextField(
        blank=True,
    )

    preparation_time = models.PositiveIntegerField(
        default=0,
        help_text="Minutes",
    )

    cooking_time = models.PositiveIntegerField(
        default=0,
        help_text="Minutes",
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


class RecipeTranslation(models.Model):
    recipe = models.ForeignKey(
        Recipe,
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
                    "recipe",
                    "language",
                ],
                name=(
                    "unique_recipe_translation_language"
                ),
            ),
        ]

        ordering = [
            "recipe_id",
            "language",
        ]

    def __str__(self):
        return (
            f"{self.recipe.name} "
            f"({self.language})"
        )


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients",
    )

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
    )

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    unit = models.ForeignKey(
        Unit,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return (
            f"{self.recipe} - "
            f"{self.ingredient}"
        )