from django.conf import settings
from django.db import models


class Ingredient(models.Model):
    name = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        blank=True,
    )

    calories = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    protein = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    carbohydrate = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    fat = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    fiber = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    sugar = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    sodium = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
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


class IngredientTranslation(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
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
                    "ingredient",
                    "language",
                ],
                name=(
                    "unique_ingredient_translation_language"
                ),
            ),
        ]

        ordering = [
            "ingredient_id",
            "language",
        ]

    def __str__(self):
        return (
            f"{self.ingredient.name} "
            f"({self.language})"
        )