from django.db import transaction
from django.utils import timezone

from .models import Payment

from wallet.models import (
    Wallet,
    WalletTransaction,
)



# =====================================================
# پرداخت سفارش از کیف پول
# =====================================================

@transaction.atomic
def process_wallet_payment(order):
    """
    پرداخت کامل سفارش از Wallet
    """

    wallet = Wallet.objects.get(
        user=order.user
    )


    amount = order.total_price


    if wallet.balance < amount:

        raise ValueError(
            "Insufficient wallet balance"
        )


    # کم کردن موجودی Wallet

    wallet.balance -= amount

    wallet.save()



    # ثبت Payment

    payment = Payment.objects.create(

        user=order.user,

        order=order,

        wallet_amount=amount,

        status='success',

        paid_at=timezone.now()

    )



    # ثبت گردش Wallet

    WalletTransaction.objects.create(

        wallet=wallet,

        payment=payment,

        transaction_type='payment',

        amount=-amount,

        description=f"Payment for Order {order.id}"

    )



    # تغییر وضعیت سفارش

    order.status = 'paid'

    order.save()



    return payment





# =====================================================
# ایجاد Payment برای شارژ Wallet از بانک
# =====================================================

@transaction.atomic
def create_wallet_charge_payment(
        user,
        amount
):
    """
    ایجاد پرداخت آنلاین برای شارژ Wallet
    """

    payment = Payment.objects.create(

        user=user,

        order=None,

        online_amount=amount,

        status='pending'

    )


    return payment





# =====================================================
# تکمیل شارژ Wallet بعد از Callback بانک
# =====================================================

@transaction.atomic
def complete_wallet_charge_payment(
        payment,
        transaction_id,
        gateway_response=None
):
    """
    بعد از تایید بانک، Wallet شارژ می‌شود
    """

    if payment.status == 'success':

        raise ValueError(
            "Payment already completed"
        )



    wallet, created = Wallet.objects.get_or_create(
        user=payment.user
    )



    amount = payment.online_amount



    # افزایش موجودی Wallet

    wallet.balance += amount

    wallet.save()



    # ثبت تراکنش شارژ Wallet

    WalletTransaction.objects.create(

        wallet=wallet,

        payment=payment,

        transaction_type='charge',

        amount=amount,

        description="Wallet charge from online payment"

    )



    payment.status = 'success'

    payment.transaction_id = transaction_id

    payment.gateway_response = gateway_response

    payment.paid_at = timezone.now()

    payment.save()



    return payment





# =====================================================
# Refund به Wallet
# =====================================================

@transaction.atomic
def refund_wallet_payment(payment):
    """
    برگشت مبلغ پرداخت شده از Wallet
    """

    if payment.wallet_amount <= 0:

        raise ValueError(
            "No wallet payment to refund"
        )



    wallet = Wallet.objects.get(
        user=payment.user
    )


    amount = payment.wallet_amount



    wallet.balance += amount

    wallet.save()



    WalletTransaction.objects.create(

        wallet=wallet,

        payment=payment,

        transaction_type='refund',

        amount=amount,

        description=f"Refund for Order {payment.order.id}"

    )



    payment.status = 'refunded'

    payment.save()



    return payment