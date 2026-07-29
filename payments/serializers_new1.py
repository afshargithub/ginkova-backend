from rest_framework import serializers
from django.conf import settings


# =====================================================
# Create Payment
# =====================================================

class PaymentCreateSerializer(serializers.Serializer):

    order_id = serializers.IntegerField()

    method = serializers.ChoiceField(
        choices=[
            ("wallet", "Wallet"),
            ("online", "Online"),
        ]
    )

    gateway = serializers.ChoiceField(
        choices=settings.ACTIVE_PAYMENT_GATEWAYS,
        required=False,
        allow_null=True
    )


# =====================================================
# Wallet Charge
# =====================================================

class WalletChargeSerializer(serializers.Serializer):

    amount = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        min_value=1
    )


# =====================================================
# Wallet Payment
# =====================================================

class WalletPaymentSerializer(serializers.Serializer):

    order_id = serializers.IntegerField()


# =====================================================
# Online Payment Callback
# =====================================================

class OnlinePaymentCallbackSerializer(serializers.Serializer):

    payment_number = serializers.CharField(
        max_length=50
    )

    transaction_id = serializers.CharField(
        max_length=200
    )

    gateway_response = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True
    )