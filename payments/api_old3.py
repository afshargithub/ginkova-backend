from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.utils import timezone
from orders.models import Order
from .gateways.factory import PaymentGatewayFactory

from .services_new1 import (
    process_wallet_payment,
    create_online_payment,
    create_wallet_charge_payment,
    complete_wallet_charge_payment,
    complete_online_payment,
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
        gateway_code = serializer.validated_data.get(
            'gateway'
        )

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


        # =================================
        # پرداخت کامل Wallet
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
        # پرداخت آنلاین سفارش
        # =================================

        payment, gateway_response = create_online_payment(
            order,
            gateway_code
        )


        return Response({

            "message":
            "Online payment created",

            "payment_id":
            payment.id,

            "gateway":
            gateway_response,

            "status":
            payment.status

        })





# =====================================================
# Callback پرداخت آنلاین
# =====================================================

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
                # status='pending'
            )
            # ابتدا خط بالا را کامنت کرده سپس کد زیر را قرار دادیمstatus='pending'
            if payment.status == "success":

                return Response(
                    {
                        "message":
                        "Payment already completed",

                        "payment_id":
                        payment.id,

                        "status":
                        payment.status
                    },
                    status=400
                )            




        except Payment.DoesNotExist:

            return Response(
                {
                    "error":
                    "Payment not found"
                },
                status=404
            )


        # ---------------------------------
        # اگر Payment مربوط به Wallet باشد
        # ---------------------------------

        if payment.order is None:

            payment = complete_wallet_charge_payment(
                payment,
                transaction_id,
                gateway_response
            )


            return Response({

                "message":
                "Wallet charged successfully",

                "payment_id":
                payment.id,

                "status":
                payment.status

            })



        # ---------------------------------
        # اگر Payment مربوط به Order باشد
        # ---------------------------------
        # payment.status = 'success'
        # payment.transaction_id = transaction_id
        # payment.gateway_response = gateway_response
        # payment.gateway_name = "fake"
        # payment.gateway_reference = transaction_id
        # payment.paid_at = timezone.now()
        # payment.save()

        # order = payment.order
        # order.status = 'paid'
        # order.save()
        try:
            payment = complete_online_payment(
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
        order = payment.order

        return Response({
            "message":
            "Order payment completed successfully",

            "payment_id":
            payment.id,

            "order_id":
            order.id,

            "status":
            payment.status

        })
        
        
class PaymentGatewayListAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def get(self, request):

        gateways = PaymentGatewayFactory.get_available_gateways()


        return Response(
            gateways
        )