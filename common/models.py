from django.db import models


class Unit(models.Model):

    UNIT_TYPE_CHOICES = (
        ("weight", "Weight"),
        ("volume", "Volume"),
        ("count", "Count"),
    )

    name = models.CharField(
        max_length=50,
        unique=True
    )

    symbol = models.CharField(
        max_length=10,
        unique=True
    )

    unit_type = models.CharField(
        max_length=20,
        choices=UNIT_TYPE_CHOICES
    )

    unit_factor = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        default=1
    )

    display_order = models.PositiveIntegerField(
        default=0
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
        return f"{self.name} ({self.symbol})"