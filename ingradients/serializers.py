from rest_framework import serializers

from .models import Ingredient



class IngredientSerializer(serializers.ModelSerializer):

    class Meta:

        model = Ingredient

        fields = (
            "id",
            "name",
            "calories",
            "protein",
            "carbohydrate",
            "fat",
            "fiber",
            "sugar",
            "sodium",
        )