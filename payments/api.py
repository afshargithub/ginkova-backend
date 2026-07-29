from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from orders.models import Order

from .models import Payment

from .serializers_new1 import (
    PaymentCreateSerializer,
    OnlinePaymentCallbackSerializer,
)

from .services_new1 import (
    process_wallet_payment,
    create_online_payment,
    complete_wallet_charge_payment,
    complete_online_payment,
)

from .gateways.factory import PaymentGatewayFactory


# =====================================================
# Create Payment
# =====================================================

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

        order_id = serializer.validated_data["order_id"]

        method = serializer.validated_data["method"]

        gateway_code = serializer.validated_data.get(
            "gateway"
        )

        try:

            order = Order.objects.get(

                id=order_id,

                user=request.user,

                status="pending_payment"

            )

        except Order.DoesNotExist:

            return Response(
                {
                    "success": False,
                    "error": "Invalid order"
                },
                status=400
            )

        # ==========================================
        # Wallet Payment
        # ==========================================

        if method == "wallet":

            try:

                payment = process_wallet_payment(
                    order
                )

            except ValueError as e:

                return Response(
                    {
                        "success": False,
                        "error": str(e)
                    },
                    status=400
                )

            return Response({

                "success": True,

                "message": "Wallet payment successful",

                "data": {

                    "payment_id": payment.id,

                    "payment_number": payment.payment_number,

                    "order_id": order.id,

                    "status": payment.status,

                }

            })

        # ==========================================
        # Online Payment
        # ==========================================

        payment, gateway_response = create_online_payment(

            order,

            gateway_code

        )

        return Response({

            "success": True,

            "message": "Online payment created",

            "data": {

                "payment_id": payment.id,

                "payment_number": payment.payment_number,

                "gateway": payment.gateway_name,

                "gateway_response": gateway_response,

                "status": payment.status,

            }

        })

# =====================================================
# Available Gateways
# =====================================================

class PaymentGatewayListAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        gateways = PaymentGatewayFactory.get_available_gateways()

        return Response({

            "success": True,

            "data": gateways

        })
        
        
#part 2
# =====================================================
# Payment Callback
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

        payment_number = serializer.validated_data[
            "payment_number"
        ]

        transaction_id = serializer.validated_data[
            "transaction_id"
        ]

        gateway_response = serializer.validated_data.get(
            "gateway_response"
        )

        try:

            payment = Payment.objects.get(

                payment_number=payment_number,

                user=request.user

            )

        except Payment.DoesNotExist:

            return Response(
                {
                    "success": False,
                    "error": "Payment not found"
                },
                status=404
            )

        # جلوگیری از دوباره پردازش شدن Callback

        if payment.status == "success":

            return Response(
                {
                    "success": False,
                    "message": "Payment already completed",
                    "data": {
                        "payment_number": payment.payment_number,
                        "status": payment.status,
                    }
                },
                status=400
            )

        # ==========================================
        # Wallet Charge
        # ==========================================

        if payment.order is None:

            try:

                payment = complete_wallet_charge_payment(

                    payment,

                    transaction_id,

                    gateway_response

                )

            except ValueError as e:

                return Response(
                    {
                        "success": False,
                        "error": str(e)
                    },
                    status=400
                )

            return Response({

                "success": True,

                "message": "Wallet charged successfully",

                "data": {

                    "payment_number": payment.payment_number,

                    "status": payment.status,

                    "wallet_amount": payment.online_amount,

                }

            })

        # ==========================================
        # Order Payment
        # ==========================================

        try:

            payment = complete_online_payment(

                payment,

                transaction_id,

                gateway_response

            )

        except ValueError as e:

            return Response(
                {
                    "success": False,
                    "error": str(e)
                },
                status=400
            )

        order = payment.order

        return Response({

            "success": True,

            "message": "Order payment completed successfully",

            "data": {

                "payment_number": payment.payment_number,

                "order_id": order.id,

                "payment_status": payment.status,

                "order_status": order.status,

            }

        })
        
