from django.db import models

# Create your models here.
from django.db import models
from recipes.models import Recipe


class MealCategory(models.Model):

    name = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )


    def __str__(self):
        return self.name



class Meal(models.Model):

    MEAL_TYPE_CHOICES = (
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    )


    name = models.CharField(
        max_length=150
    )


    description = models.TextField(
        blank=True
    )


    meal_type = models.CharField(
        max_length=20,
        choices=MEAL_TYPE_CHOICES
    )

    recipes = models.ManyToManyField(
        Recipe
    )

    categories = models.ManyToManyField(
        MealCategory,
        blank=True
    )

    is_featured = models.BooleanField(
        default=False
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