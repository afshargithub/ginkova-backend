from django.db import transaction
from django.utils import timezone

from .models import Wallet, WalletTransaction
from payments.models import Payment


@transaction.atomic
def complete_wallet_charge_payment(
    payment,
    transaction_id=None,
    gateway_reference=None,
    gateway_response=None,
):
    """
    تایید شارژ کیف پول بعد از Callback بانک
    """

    if payment.status == "success" and hasattr(payment, "wallet_transaction"):
        return payment

    wallet, created = Wallet.objects.get_or_create(
        user=payment.user
    )

    # افزایش موجودی کیف پول
    wallet.balance += payment.online_amount
    wallet.save(update_fields=["balance"])

    # ثبت تراکنش کیف پول
    WalletTransaction.objects.create(
        wallet=wallet,
        payment=payment,
        transaction_type="charge",
        amount=payment.online_amount,
        description="Wallet charged successfully"
    )

    # بروزرسانی Payment
    payment.status = "success"
    payment.transaction_id = transaction_id
    payment.gateway_reference = gateway_reference
    payment.gateway_response = gateway_response
    payment.paid_at = timezone.now()
    payment.save()

    return payment