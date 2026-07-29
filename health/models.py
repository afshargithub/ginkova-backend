from django.db import models
from django.conf import settings


class HealthGoal(models.Model):

    name = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    # آیکون مورد استفاده در UI
    icon = models.CharField(
        max_length=50,
        blank=True,
        default=""
    )

    # ترتیب نمایش در صفحه اول
    display_order = models.PositiveIntegerField(
        default=0
    )

    # فعال یا غیرفعال بودن
    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["display_order", "name"]
        

class Disease(models.Model):

    name = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name


class HealthProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    height = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Height in cm"
    )

    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    birth_date = models.DateField(
        null=True,
        blank=True
    )

    diseases = models.ManyToManyField(
        Disease,
        blank=True
    )

    goals = models.ManyToManyField(
        HealthGoal,
        blank=True
    )

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return f"{self.user.username} Health Profile"