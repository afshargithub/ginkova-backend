from rest_framework import serializers

from common.serializers import (
    LocalizedFieldsMixin,
)

from .models import (
    Disease,
    HealthGoal,
)


class HealthGoalSerializer(
    LocalizedFieldsMixin,
    serializers.ModelSerializer,
):
    name = serializers.SerializerMethodField()

    description = serializers.SerializerMethodField()

    class Meta:
        model = HealthGoal

        fields = (
            "id",
            "name",
            "description",
            "icon",
            "display_order",
        )


class DiseaseSerializer(
    LocalizedFieldsMixin,
    serializers.ModelSerializer,
):
    name = serializers.SerializerMethodField()

    description = serializers.SerializerMethodField()

    class Meta:
        model = Disease

        fields = (
            "id",
            "name",
            "description",
        )