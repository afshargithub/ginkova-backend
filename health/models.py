from django.conf import settings
from django.db import models


class HealthGoal(models.Model):
    name = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        blank=True,
    )

    # آیکون مورد استفاده در UI
    icon = models.CharField(
        max_length=50,
        blank=True,
        default="",
    )

    # ترتیب نمایش در صفحه اول
    display_order = models.PositiveIntegerField(
        default=0,
    )

    # فعال یا غیرفعال بودن
    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = [
            "display_order",
            "name",
        ]

    def __str__(self):
        return self.name


class HealthGoalTranslation(models.Model):
    health_goal = models.ForeignKey(
        HealthGoal,
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
                    "health_goal",
                    "language",
                ],
                name=(
                    "unique_health_goal_translation_language"
                ),
            ),
        ]

        ordering = [
            "health_goal_id",
            "language",
        ]

    def __str__(self):
        return (
            f"{self.health_goal.name} "
            f"({self.language})"
        )


class Disease(models.Model):
    name = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.name


class DiseaseTranslation(models.Model):
    disease = models.ForeignKey(
        Disease,
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
                    "disease",
                    "language",
                ],
                name=(
                    "unique_disease_translation_language"
                ),
            ),
        ]

        ordering = [
            "disease_id",
            "language",
        ]

    def __str__(self):
        return (
            f"{self.disease.name} "
            f"({self.language})"
        )


class HealthProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    height = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Height in cm",
    )

    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )

    birth_date = models.DateField(
        null=True,
        blank=True,
    )

    diseases = models.ManyToManyField(
        Disease,
        blank=True,
    )

    goals = models.ManyToManyField(
        HealthGoal,
        blank=True,
    )

    notes = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return (
            f"{self.user.username} "
            "Health Profile"
        )