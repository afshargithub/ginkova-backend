from rest_framework import serializers

from common.serializers import (
    LocalizedFieldsMixin,
)

from .models import (
    Restaurant,
    RestaurantMeal,
)


class RestaurantSerializer(
    LocalizedFieldsMixin,
    serializers.ModelSerializer,
):
    name = serializers.SerializerMethodField()

    address = serializers.SerializerMethodField()

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

    def get_address(self, obj):
        translation = self.get_translation(obj)

        if (
            translation is not None
            and translation.address
        ):
            return translation.address

        return obj.address


class RestaurantMealSerializer(
    LocalizedFieldsMixin,
    serializers.ModelSerializer,
):
    restaurant_name = (
        serializers.SerializerMethodField()
    )

    meal_name = (
        serializers.SerializerMethodField()
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

    def get_restaurant_name(self, obj):
        return self.get_name(
            obj.restaurant
        )

    def get_meal_name(self, obj):
        return self.get_name(
            obj.meal
        )