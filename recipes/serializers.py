from rest_framework import serializers

from .models import Recipe, RecipeIngredient
from ingradients.serializers import IngredientSerializer



class RecipeIngredientSerializer(serializers.ModelSerializer):

    ingredient = IngredientSerializer(read_only=True)
    unit = serializers.StringRelatedField()

    class Meta:

        model = RecipeIngredient

        fields = (
            "ingredient",
            "quantity",
            "unit",
        )



class RecipeSerializer(serializers.ModelSerializer):

    ingredients = RecipeIngredientSerializer(
        many=True,
        read_only=True
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