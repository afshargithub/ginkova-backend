from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from wallet.models import Wallet
from .services_new1 import (process_wallet_payment, create_wallet_charge_payment, complete_wallet_charge_payment)

from orders.models import Order
from .serializers_new1 import PaymentCreateSerializer


class PaymentCreateAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def post(self, request):

        serializer = PaymentCreateSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )


        order_id = serializer.validated_data[
            'order_id'
        ]

        method = serializer.validated_data[
            'method'
        ]


        try:

            order = Order.objects.get(
                id=order_id,
                user=request.user,
                status='pending_payment'
            )


        except Order.DoesNotExist:

            return Response(
                {
                    "error":
                    "Invalid order"
                },
                status=400
            )
        
        # -----------------------------
        # Wallet Payment
        # -----------------------------
        if method == "wallet":

            try:

                wallet = Wallet.objects.get(
                    user=request.user
                )

            except Wallet.DoesNotExist:

                return Response(
                    {
                        "error": "Wallet not found"
                    },
                    status=400
                )


            try:

                payment = process_wallet_payment(
                    order,
                    wallet
                )

            except ValueError as e:

                return Response(
                    {
                        "error": str(e)
                    },
                    status=400
                )


            return Response({

                "message": "Wallet payment successful",

                "payment_id": payment.id,

                "order_id": order.id,

                "status": order.status

            })

        # -----------------------------
        # Online Payment
        # -----------------------------
        payment = create_wallet_charge_payment(order)

        return Response({

            "message": "Online payment created",

            "payment_id": payment.id,

            "order_id": order.id,

            "status": payment.status

        })