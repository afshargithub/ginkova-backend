from decimal import Decimal

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from orders.models import Order
from wallet.models import Wallet

from .services_new1 import (
    process_wallet_payment,
    create_wallet_charge_payment,
    complete_wallet_charge_payment,
)

from .serializers_new1 import (
    PaymentCreateSerializer,
    OnlinePaymentCallbackSerializer,
)
from .models import Payment


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
                    "error": "Invalid order"
                },
                status=400
            )



        # =================================
        # پرداخت کامل از Wallet
        # =================================

        if method == "wallet":


            try:

                payment = process_wallet_payment(
                    order
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
                "Wallet payment successful",

                "payment_id":
                payment.id,

                "order_id":
                order.id,

                "status":
                order.status

            })



        # =================================
        # پرداخت آنلاین برای شارژ Wallet
        # =================================


        try:

            wallet = Wallet.objects.get(
                user=request.user
            )


        except Wallet.DoesNotExist:

            wallet_balance = Decimal("0")

        else:

            wallet_balance = wallet.balance



        required_amount = (
            order.total_price -
            wallet_balance
        )


        if required_amount <= 0:

            return Response(
                {
                    "message":
                    "Wallet balance is enough"
                }
            )



        payment = create_wallet_charge_payment(
            request.user,
            required_amount
        )



        return Response({

            "message":
            "Wallet charge payment created",

            "payment_id":
            payment.id,

            "order_id":
            order.id,

            "amount":
            required_amount,

            "status":
            payment.status

        })
        
        
        
class PaymentCallbackAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def post(self, request):

        serializer = OnlinePaymentCallbackSerializer(
            data=request.data
        )


        serializer.is_valid(
            raise_exception=True
        )


        payment_id = serializer.validated_data[
            'payment_id'
        ]

        transaction_id = serializer.validated_data[
            'transaction_id'
        ]

        gateway_response = serializer.validated_data.get(
            'gateway_response'
        )


        try:

            payment = Payment.objects.get(
                id=payment_id,
                user=request.user,
                status='pending'
            )


        except Payment.DoesNotExist:

            return Response(
                {
                    "error":
                    "Payment not found"
                },
                status=404
            )



        try:

            payment = complete_wallet_charge_payment(
                payment,
                transaction_id,
                gateway_response
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
            "Payment completed successfully",

            "payment_id":
            payment.id,

            "status":
            payment.status

        })