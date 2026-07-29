from rest_framework import serializers

from .models import Meal, MealCategory
from nutrition.services import calculate_meal_nutrition
from recipes.serializers import RecipeSerializer


class MealSerializer(serializers.ModelSerializer):

    nutrition = serializers.SerializerMethodField()


    class Meta:

        model = Meal

        fields = (
            "id",
            "name",
            "description",
            "meal_type",
            "is_featured",
            "is_active",
            "nutrition",
        )


    def get_nutrition(self, obj):

        return calculate_meal_nutrition(
            obj
        )



class MealDetailSerializer(serializers.ModelSerializer):

    recipes = RecipeSerializer(
        many=True,
        read_only=True
    )


    nutrition = serializers.SerializerMethodField()


    class Meta:

        model = Meal

        fields = (
            "id",
            "name",
            "description",
            "meal_type",
            "is_featured",
            "is_active",
            "recipes",
            "nutrition",
        )


    def get_nutrition(self, obj):

        return calculate_meal_nutrition(
            obj
        )



class MealCategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = MealCategory

        fields = (
            "id",
            "name",
            "description",
        )