from rest_framework import serializers
from decimal import Decimal

from common.choices import CONSUMED_BY_CHOICES

from .models import (
    Cart,
    CartItem,
)



class CartItemSerializer(serializers.ModelSerializer):


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


    estimated_preparation_time = serializers.IntegerField(
        source="restaurant_meal.estimated_preparation_time",
        read_only=True
    )


    is_available = serializers.BooleanField(
        source="restaurant_meal.is_available",
        read_only=True
    )


    subtotal = serializers.SerializerMethodField()



    class Meta:

        model = CartItem


        fields = [

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

            "estimated_preparation_time",

            "is_available",

            "subtotal",

        ]



    def get_subtotal(self, obj):

        return obj.subtotal()





class CartSerializer(serializers.ModelSerializer):


    items = CartItemSerializer(
        many=True,
        read_only=True
    )


    total_price = serializers.SerializerMethodField()



    class Meta:

        model = Cart


        fields = [

            "id",

            "items",

            "total_price",

        ]



    def get_total_price(self, obj):

        total = Decimal("0")


        for item in obj.items.all():

            total += item.subtotal()


        return total





class AddToCartSerializer(serializers.Serializer):


    restaurant_meal_id = serializers.IntegerField()


    quantity = serializers.IntegerField(
        min_value=1
    )


    consumed_by = serializers.ChoiceField(
        choices=CONSUMED_BY_CHOICES,
        default="self"
    )





class UpdateCartSerializer(serializers.Serializer):


    cart_item_id = serializers.IntegerField()


    quantity = serializers.IntegerField(
        min_value=1
    )





class RemoveCartSerializer(serializers.Serializer):


    cart_item_id = serializers.IntegerField()