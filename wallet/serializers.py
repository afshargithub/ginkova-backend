from rest_framework import serializers

from .models import (
    Wallet,
    WalletTransaction,
)


class WalletSerializer(serializers.ModelSerializer):

    class Meta:

        model = Wallet

        fields = (
            "id",
            "balance",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "balance",
            "created_at",
            "updated_at",
        )



class WalletTransactionSerializer(serializers.ModelSerializer):

    transaction_type_display = serializers.CharField(
        source="get_transaction_type_display",
        read_only=True
    )
    
    payment_number = serializers.CharField(
        source="payment.payment_number",
        read_only=True
    )    

    class Meta:

        model = WalletTransaction

        fields = (
            "id",
            "payment_number",
            "transaction_type",
            "transaction_type_display",
            "amount",
            "description",
            "created_at",
        )

        read_only_fields = (
            "id",
            "payment_number",
            "created_at",
        )



class WalletChargeSerializer(serializers.Serializer):

    amount = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        min_value=1
    )
    
    
    
class WalletChargeCallbackSerializer(serializers.Serializer):

    payment_id = serializers.IntegerField()

    transaction_id = serializers.CharField(
        max_length=200
    )