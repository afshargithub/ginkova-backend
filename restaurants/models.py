from django.conf import settings
from django.db import models

from meals.models import Meal


class Restaurant(models.Model):
    name = models.CharField(
        max_length=150,
    )

    manager_name = models.CharField(
        max_length=100,
        blank=True,
    )

    phone = models.CharField(
        max_length=20,
    )

    address = models.TextField()

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )

    opening_time = models.TimeField(
        null=True,
        blank=True,
    )

    closing_time = models.TimeField(
        null=True,
        blank=True,
    )

    delivery_radius = models.PositiveIntegerField(
        default=5,
        help_text="Kilometers",
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


class RestaurantTranslation(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
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

    address = models.TextField(
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
                    "restaurant",
                    "language",
                ],
                name=(
                    "unique_restaurant_translation_language"
                ),
            ),
        ]

        ordering = [
            "restaurant_id",
            "language",
        ]

    def __str__(self):
        return (
            f"{self.restaurant.name} "
            f"({self.language})"
        )


class RestaurantMeal(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.PROTECT,
        related_name="restaurant_meals",
    )

    meal = models.ForeignKey(
        Meal,
        on_delete=models.PROTECT,
        related_name="restaurant_options",
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    image = models.ImageField(
        upload_to="restaurant_meals/",
        blank=True,
        null=True,
    )

    estimated_preparation_time = (
        models.PositiveIntegerField(
            default=0,
            help_text="Minutes",
        )
    )

    is_available = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return (
            f"{self.restaurant} - "
            f"{self.meal}"
        )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "restaurant",
                    "meal",
                ],
                name=(
                    "unique_restaurant_meal"
                ),
            ),
        ]