from rest_framework import serializers

from common.serializers import (
    LocalizedFieldsMixin,
    UnitSerializer,
)
from ingradients.serializers import (
    IngredientSerializer,
)

from .models import Recipe, RecipeIngredient


class RecipeIngredientSerializer(
    serializers.ModelSerializer
):
    ingredient = IngredientSerializer(
        read_only=True,
    )

    unit = UnitSerializer(
        read_only=True,
    )

    class Meta:
        model = RecipeIngredient

        fields = (
            "ingredient",
            "quantity",
            "unit",
        )


class RecipeSerializer(
    LocalizedFieldsMixin,
    serializers.ModelSerializer,
):
    name = serializers.SerializerMethodField()

    description = serializers.SerializerMethodField()

    ingredients = RecipeIngredientSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Recipe

        fields = (
            "id",
            "name",
            "description",
            "preparation_time",
            "cooking_time",
            "ingredients",
        )