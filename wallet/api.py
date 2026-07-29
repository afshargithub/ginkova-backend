from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from payments.models import Payment
from .services import complete_wallet_charge_payment

from .models import Wallet
from .serializers import (
    WalletSerializer,
    WalletTransactionSerializer,
    WalletChargeSerializer,
    WalletChargeCallbackSerializer,
)

from payments.services import (
    create_wallet_charge_payment,
)


class WalletAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        wallet, created = Wallet.objects.get_or_create(
            user=request.user
        )

        serializer = WalletSerializer(wallet)

        return Response(serializer.data)


class WalletTransactionAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        wallet, created = Wallet.objects.get_or_create(
            user=request.user
        )

        transactions = wallet.transactions.all().order_by(
            '-created_at'
        )

        serializer = WalletTransactionSerializer(
            transactions,
            many=True
        )

        return Response(serializer.data)


class WalletChargeAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        serializer = WalletChargeSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        amount = serializer.validated_data[
            'amount'
        ]

        payment = create_wallet_charge_payment(
            user=request.user,
            amount=amount
        )

        return Response({

            "message": "Wallet charge payment created",

            "payment_id": payment.id,

            "payment_number": payment.payment_number,
            
            "gateway": payment.gateway_name,

            "amount": payment.online_amount,

            "status": payment.status

        })
        
  
        
class WalletChargeCallbackAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        serializer = WalletChargeCallbackSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        payment_id = serializer.validated_data[
            "payment_id"
        ]

        transaction_id = serializer.validated_data[
            "transaction_id"
        ]

        try:

            payment = Payment.objects.get(
                id=payment_id,
                user=request.user,
                order=None
            )

        except Payment.DoesNotExist:

            return Response(
                {
                    "error":
                    "Payment not found"
                },
                status=404
            )

        payment = complete_wallet_charge_payment(
            payment=payment,
            transaction_id=transaction_id
        )

        return Response({

            "message":
            "Wallet charged successfully",

            "payment_id":
            payment.id,

            "wallet_amount":
            payment.online_amount,

            "status":
            payment.status

        })