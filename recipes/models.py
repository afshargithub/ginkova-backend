from django.db import models
from ingradients.models import Ingredient
from common.models import Unit


class Recipe(models.Model):

    name = models.CharField(
        max_length=150
    )

    description = models.TextField(
        blank=True
    )

    preparation_time = models.PositiveIntegerField(
        default=0,
        help_text="Minutes"
    )

    cooking_time = models.PositiveIntegerField(
        default=0,
        help_text="Minutes"
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return self.name



from common.models import Unit


class RecipeIngredient(models.Model):

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients"
    )

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE
    )

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    unit = models.ForeignKey(
        Unit,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return (
            f"{self.recipe} - "
            f"{self.ingredient}"
        )