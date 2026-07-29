from decimal import Decimal

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from restaurants.models import RestaurantMeal

from .models import Cart, CartItem

from .serializers import (
    CartItemSerializer,
    AddToCartSerializer,
    UpdateCartSerializer,
    RemoveCartSerializer,
)


class CartAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def get(self, request):

        cart, created = Cart.objects.get_or_create(
            user=request.user
        )


        items = cart.items.select_related(
            'restaurant_meal',
            'restaurant_meal__meal',
            'restaurant_meal__restaurant',
        ).all()


        serializer = CartItemSerializer(
            items,
            many=True
        )


        total = Decimal("0")


        for item in items:

            total += item.subtotal()


        return Response({

            "items": serializer.data,

            "total_price": total

        })



class CartAddAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def post(self, request):

        serializer = AddToCartSerializer(
            data=request.data
        )


        serializer.is_valid(
            raise_exception=True
        )


        restaurant_meal_id = serializer.validated_data[
            "restaurant_meal_id"
        ]


        quantity = serializer.validated_data[
            "quantity"
        ]


        consumed_by = serializer.validated_data.get(
            "consumed_by",
            "self"
        )


        try:

            restaurant_meal = RestaurantMeal.objects.select_related(
                "restaurant",
                "meal"
            ).get(

                id=restaurant_meal_id,

                is_available=True,

                restaurant__is_active=True,

                meal__is_active=True

            )


        except RestaurantMeal.DoesNotExist:

            return Response(

                {
                    "error":
                    "Selected meal is unavailable"
                },

                status=404

            )



        cart, created = Cart.objects.get_or_create(
            user=request.user
        )



        # جلوگیری از سفارش از چند رستوران در یک Cart

        if cart.items.exists():

            current_restaurant = (

                cart.items.first()

                .restaurant_meal

                .restaurant

            )


            if current_restaurant != restaurant_meal.restaurant:

                return Response(

                    {
                        "error":
                        "You cannot add meals from different restaurants to one cart."
                    },

                    status=400

                )



        cart_item, created = CartItem.objects.get_or_create(

            cart=cart,

            restaurant_meal=restaurant_meal,

            consumed_by=consumed_by,


            defaults={

                "quantity": quantity,

                "price": restaurant_meal.price,

            }

        )



        if not created:

            cart_item.quantity += quantity

            cart_item.save()



        return Response({

            "message":
            "Item added to cart",

            "cart_item_id":
            cart_item.id

        })




class CartUpdateAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def put(self, request):

        serializer = UpdateCartSerializer(
            data=request.data
        )


        serializer.is_valid(
            raise_exception=True
        )


        item_id = serializer.validated_data[
            "cart_item_id"
        ]


        quantity = serializer.validated_data[
            "quantity"
        ]



        try:

            item = CartItem.objects.get(

                id=item_id,

                cart__user=request.user

            )


        except CartItem.DoesNotExist:

            return Response(

                {
                    "error":
                    "Item not found"
                },

                status=404

            )



        item.quantity = quantity

        item.save()



        return Response({

            "message":
            "Cart updated",

            "quantity":
            item.quantity,

            "subtotal":
            item.subtotal()

        })




class CartRemoveAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def delete(self, request):

        serializer = RemoveCartSerializer(
            data=request.data
        )


        serializer.is_valid(
            raise_exception=True
        )


        item_id = serializer.validated_data[
            "cart_item_id"
        ]



        try:

            item = CartItem.objects.get(

                id=item_id,

                cart__user=request.user

            )


        except CartItem.DoesNotExist:

            return Response(

                {
                    "error":
                    "Item not found"
                },

                status=404

            )



        item.delete()



        return Response({

            "message":
            "Item removed successfully"

        })