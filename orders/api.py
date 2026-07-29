from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.models import UserAddress

from .serializers import (CheckoutSerializer, OrderSerializer,)
from .services import (create_order_from_cart, update_order_status,)
from .models import Order



class CheckoutAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def post(self, request):

        serializer = CheckoutSerializer(
            data=request.data
        )


        serializer.is_valid(
            raise_exception=True
        )


        address_id = serializer.validated_data[
            'address_id'
        ]


        try:

            address = UserAddress.objects.get(
                id=address_id,
                user=request.user,
                is_active=True
            )


        except UserAddress.DoesNotExist:

            return Response(
                {
                    "error":
                    "Invalid address"
                },
                status=400
            )


        try:

            order = create_order_from_cart(
                request.user,
                address
            )


        except ValueError as e:

            return Response(
                {
                    "error": str(e)
                },
                status=400
            )


        return Response({

            "message":
            "Order created successfully",

            "order_id":
            order.id,

            "amount":
            order.total_price,

            "status":
            order.status

        })
        
        
        
class OrderStatusAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def patch(self, request):

        order_id = request.data.get(
            "order_id"
        )

        new_status = request.data.get(
            "status"
        )


        if not order_id or not new_status:

            return Response(
                {
                    "error":
                    "order_id and status are required"
                },
                status=400
            )


        try:

            order = Order.objects.get(
                id=order_id,
                user=request.user
            )


        except Order.DoesNotExist:

            return Response(
                {
                    "error":
                    "Order not found"
                },
                status=404
            )


        try:

            update_order_status(
                order,
                new_status
            )


        except ValueError as e:

            return Response(
                {
                    "error": str(e)
                },
                status=400
            )


        return Response({

            "message":
            "Order status updated successfully",

            "order_id":
            order.id,

            "status":
            order.status,

            "status_display":
            order.get_status_display()

        })        
        

class OrderListAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        orders = Order.objects.filter(
            user=request.user
        ).select_related(
            "restaurant",
            "delivery_address"
        ).prefetch_related(
            "items__restaurant_meal__meal",
            "items__restaurant_meal__restaurant",
        ).order_by("-created_at")

        serializer = OrderSerializer(
            orders,
            many=True
        )

        return Response(serializer.data)



class OrderDetailAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def get(self, request, order_id):

        try:

            order = Order.objects.select_related(
                "restaurant",
                "delivery_address"
            ).prefetch_related(
                "items__restaurant_meal__meal",
                "items__restaurant_meal__restaurant",
            ).get(
                id=order_id,
                user=request.user
            )


        except Order.DoesNotExist:

            return Response(
                {
                    "error": "Order not found"
                },
                status=404
            )


        serializer = OrderSerializer(
            order
        )


        return Response(
            serializer.data
        )
