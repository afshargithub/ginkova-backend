from rest_framework import serializers
from django.conf import settings

class PaymentCreateSerializer(serializers.Serializer):

    order_id = serializers.IntegerField()

    method = serializers.ChoiceField(
        choices=[
            'wallet',
            'online'
        ]
    )

    gateway = serializers.ChoiceField(

        choices=settings.ACTIVE_PAYMENT_GATEWAYS,
        required=False,
        allow_null=True

    )



class WalletChargeSerializer(serializers.Serializer):

    amount = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        min_value=1
    )



class WalletPaymentSerializer(serializers.Serializer):

    order_id = serializers.IntegerField()



class OnlinePaymentCallbackSerializer(serializers.Serializer):

    payment_id = serializers.IntegerField()

    transaction_id = serializers.CharField(
        max_length=200
    )

    gateway_response = serializers.CharField(
        required=False,
        allow_blank=True
    )
