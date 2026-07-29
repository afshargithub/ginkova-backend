from rest_framework import serializers

from .models import RestaurantMeal


class RestaurantMealSerializer(serializers.ModelSerializer):

    restaurant_name = serializers.CharField(
        source="restaurant.name",
        read_only=True
    )

    meal_name = serializers.CharField(
        source="meal.name",
        read_only=True
    )


    class Meta:

        model = RestaurantMeal

        fields = (
            "id",
            "restaurant_name",
            "meal_name",
            "price",
            "image",
            "estimated_preparation_time",
            "is_available",
        )