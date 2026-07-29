from rest_framework import serializers

from .models import Restaurant, RestaurantMeal


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:

        model = Restaurant

        fields = (
            "id",
            "name",
            "manager_name",
            "phone",
            "address",
            "latitude",
            "longitude",
            "opening_time",
            "closing_time",
            "delivery_radius",
            "is_active",
        )


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