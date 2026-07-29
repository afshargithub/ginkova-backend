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
# Wallet Payment
# =====================================================

@transaction.atomic
def process_wallet_payment(order):

    """
    پرداخت کامل سفارش از Wallet

    شرط:
    موجودی Wallet باید >= مبلغ سفارش باشد

    """

    wallet, created = Wallet.objects.get_or_create(
        user=order.user
    )


    amount = order.total_price


    if wallet.balance < amount:

        raise ValueError(
            "Insufficient wallet balance. Please charge your wallet first."
        )


    wallet.balance -= amount

    wallet.save()



    payment = Payment.objects.create(

        user=order.user,

        order=order,

        wallet_amount=amount,

        status="success",

        paid_at=timezone.now()

    )



    WalletTransaction.objects.create(

        wallet=wallet,

        payment=payment,

        transaction_type="payment",

        amount=-amount,

        description=f"Payment for Order {order.id}"

    )



    order.status = "paid"

    order.save(
        update_fields=["status"]
    )



    NotificationService.send(

        event_code="payment_success",

        user=order.user,

        context={
            "order_id": order.id,
            "amount": amount,
        },

        related_object=payment

    )



    return payment





# =====================================================
# Create Online Payment
# =====================================================

@transaction.atomic
def create_online_payment(
        order,
        gateway_code=None
):

    """
    ایجاد پرداخت آنلاین کامل سفارش
    """

    amount = order.total_price



    payment = Payment.objects.create(

        user=order.user,

        order=order,

        online_amount=amount,

        status="pending"

    )



    gateway = PaymentGatewayFactory.get_gateway(
        gateway_code
    )



    payment.gateway_name = gateway.code

    payment.save(
        update_fields=[
            "gateway_name"
        ]
    )



    gateway_response = gateway.create_payment(
        payment
    )


    return payment, gateway_response





# =====================================================
# Complete Online Payment Callback
# =====================================================

@transaction.atomic
def complete_online_payment(
        payment,
        transaction_id,
        gateway_response=None
):


    if payment.status == "success":

        raise ValueError(
            "Payment already completed"
        )



    payment.status = "success"

    payment.transaction_id = transaction_id

    payment.gateway_reference = transaction_id

    payment.gateway_response = gateway_response

    payment.paid_at = timezone.now()


    payment.save()



    if payment.order:

        order = payment.order

        order.status = "paid"

        order.save(
            update_fields=[
                "status"
            ]
        )



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
# Wallet Charge Completion
# =====================================================

@transaction.atomic
def complete_wallet_charge_payment(
        payment,
        transaction_id,
        gateway_response=None
):


    if payment.status == "success":

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

        transaction_type="charge",

        amount=amount,

        description="Wallet charge"

    )



    payment.status = "success"

    payment.transaction_id = transaction_id

    payment.gateway_response = gateway_response

    payment.paid_at = timezone.now()


    payment.save()



    return payment