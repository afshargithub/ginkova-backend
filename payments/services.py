from django.db import transaction
from django.utils import timezone

from .models import Payment

from wallet.models import (
    Wallet,
    WalletTransaction,
)

from .gateways.factory import PaymentGatewayFactory
from notifications.services import NotificationService




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


    wallet.balance -= amount
    wallet.save()


    payment = Payment.objects.create(

        user=order.user,

        order=order,

        wallet_amount=amount,

        status='success',

        paid_at=timezone.now()

    )


    WalletTransaction.objects.create(

        wallet=wallet,

        payment=payment,

        transaction_type='payment',

        amount=-amount,

        description=f"Payment for Order {order.id}"

    )


    order.status = 'paid'
    order.save(update_fields=["status"])


    return payment





# =====================================================
# ایجاد پرداخت آنلاین سفارش
# =====================================================

@transaction.atomic
def create_online_payment(
        order,
        gateway_code=None,
        amount=None
):
    """
    ایجاد Payment و ارسال درخواست به Gateway
    """

    if amount is None:

        amount = order.total_price



    payment = Payment.objects.create(

        user=order.user,

        order=order,

        online_amount=amount,

        status='pending'

    )


    gateway = PaymentGatewayFactory.get_gateway(gateway_code)

    payment.gateway_name = gateway.code
    payment.save(update_fields=["gateway_name"])
    gateway_response = gateway.create_payment(
        payment
    )
    
    return payment, gateway_response




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
    gateway = PaymentGatewayFactory.get_gateway()
    payment = Payment.objects.create(
        user=user,
        order=None,
        online_amount=amount,
        gateway_name=gateway.code,
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

    wallet.balance += amount
    wallet.save()



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
# تکمیل پرداخت آنلاین سفارش بعد از Callback بانک
# =====================================================
@transaction.atomic
def complete_online_payment(
        payment,
        transaction_id,
        gateway_response=None
):

    if payment.status == "success":
        raise ValueError("Payment already completed")

    payment.status = "success"
    payment.transaction_id = transaction_id
    payment.gateway_reference = transaction_id
    payment.gateway_response = gateway_response
    payment.paid_at = timezone.now()
    payment.save()

    
    if payment.order:
        order = payment.order
        order.status = "paid"
        order.save(update_fields=["status"]) # just update the status field to avoid unnecessary updates)
    
    
    NotificationService.send(
        event_code="payment_success",
        user=payment.user,
        context={
            "order_id": order.id,
            "amount": payment.online_amount,
        },

        related_object=payment
    )


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
    payment.save(update_fields=["status"])


    return payment