from rest_framework import serializers

from common.serializers import (
    LocalizedFieldsMixin,
)

from .models import Ingredient


class IngredientSerializer(
    LocalizedFieldsMixin,
    serializers.ModelSerializer,
):
    name = serializers.SerializerMethodField()

    description = serializers.SerializerMethodField()

    class Meta:
        model = Ingredient

        fields = (
            "id",
            "name",
            "description",
            "calories",
            "protein",
            "carbohydrate",
            "fat",
            "fiber",
            "sugar",
            "sodium",
        )