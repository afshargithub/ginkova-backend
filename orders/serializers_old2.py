from rest_framework import serializers
from .models import (Order, OrderItem,)


class CheckoutSerializer(serializers.Serializer):

    address_id = serializers.IntegerField()


class OrderItemSerializer(serializers.ModelSerializer):

    meal_id = serializers.IntegerField(
        source="restaurant_meal.meal.id",
        read_only=True
    )

    meal_name = serializers.CharField(
        source="restaurant_meal.meal.name",
        read_only=True
    )

    restaurant_id = serializers.IntegerField(
        source="restaurant_meal.restaurant.id",
        read_only=True
    )

    restaurant_name = serializers.CharField(
        source="restaurant_meal.restaurant.name",
        read_only=True
    )

    image = serializers.ImageField(
        source="restaurant_meal.image",
        read_only=True
    )

    time_to_ready = serializers.IntegerField(
        source="restaurant_meal.time_to_ready",
        read_only=True
    )

    is_available = serializers.BooleanField(
        source="restaurant_meal.is_available",
        read_only=True
    )

    subtotal = serializers.SerializerMethodField()

    class Meta:

        model = OrderItem

        fields = (
            "id",
            "restaurant_meal",
            "meal_id",
            "meal_name",
            "restaurant_id",
            "restaurant_name",
            "image",
            "quantity",
            "price",
            "consumed_by",
            "time_to_ready",
            "is_available",
            "subtotal",
        )

    def get_subtotal(self, obj):

        return obj.quantity * obj.price


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(
        many=True,
        read_only=True
    )

    status_display = serializers.CharField(
        source="get_status_display",
        read_only=True
    )

    restaurant_id = serializers.IntegerField(
        source="restaurant.id",
        read_only=True
    )

    restaurant_name = serializers.CharField(
        source="restaurant.name",
        read_only=True
    )

    class Meta:

        model = Order

        fields = (
            "id",
            "restaurant",
            "restaurant_id",
            "restaurant_name",
            "status",
            "status_display",
            "total_price",
            "created_at",
            "delivery_address",
            "items",
        )