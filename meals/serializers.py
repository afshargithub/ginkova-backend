from rest_framework import serializers

from common.serializers import (
    LocalizedFieldsMixin,
)
from nutrition.services import (
    calculate_meal_nutrition,
)
from recipes.serializers import RecipeSerializer

from .models import Meal, MealCategory


class MealSerializer(
    LocalizedFieldsMixin,
    serializers.ModelSerializer,
):
    name = serializers.SerializerMethodField()

    description = serializers.SerializerMethodField()

    nutrition = serializers.SerializerMethodField()

    class Meta:
        model = Meal

        fields = (
            "id",
            "name",
            "description",
            "image",
            "meal_type",
            "is_featured",
            "is_active",
            "nutrition",
        )

    def get_nutrition(self, obj):
        return calculate_meal_nutrition(obj)


class MealDetailSerializer(
    LocalizedFieldsMixin,
    serializers.ModelSerializer,
):
    name = serializers.SerializerMethodField()

    description = serializers.SerializerMethodField()

    recipes = RecipeSerializer(
        many=True,
        read_only=True,
    )

    nutrition = serializers.SerializerMethodField()

    class Meta:
        model = Meal

        fields = (
            "id",
            "name",
            "description",
            "image",
            "meal_type",
            "is_featured",
            "is_active",
            "recipes",
            "nutrition",
        )

    def get_nutrition(self, obj):
        return calculate_meal_nutrition(obj)


class MealCategorySerializer(
    LocalizedFieldsMixin,
    serializers.ModelSerializer,
):
    name = serializers.SerializerMethodField()

    description = serializers.SerializerMethodField()

    image = serializers.ImageField(
        read_only=True,
    )

    class Meta:
        model = MealCategory

        fields = (
            "id",
            "name",
            "description",
            "image",
        )