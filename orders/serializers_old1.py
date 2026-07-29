from rest_framework import serializers

from .models import (
    Order,
    OrderItem,
)


class CheckoutSerializer(serializers.Serializer):

    address_id = serializers.IntegerField()



class OrderItemSerializer(serializers.ModelSerializer):

    meal_name = serializers.CharField(
        source="meal.name",
        read_only=True
    )

    class Meta:

        model = OrderItem

        fields = (
            "id",
            "meal",
            "meal_name",
            "quantity",
            "price",
            "consumed_by",
        )



class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(
        many=True,
        read_only=True
    )


    status_display = serializers.CharField(
        source="get_status_display",
        read_only=True
    )


    class Meta:

        model = Order

        fields = (
            "id",
            "status",
            "status_display",
            "total_price",
            "created_at",
            "delivery_address",
            "items",
        )