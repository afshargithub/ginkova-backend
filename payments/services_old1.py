from django.db import transaction
from django.utils import timezone

from .models import Payment
from wallet.models import Wallet, WalletTransaction



@transaction.atomic
def process_wallet_payment(order, wallet):
    """
    پرداخت کامل سفارش از کیف پول
    """

    amount = order.total_price


    # بررسی موجودی Wallet

    if wallet.balance < amount:

        raise ValueError(
            "Insufficient wallet balance"
        )


    # کم کردن موجودی کیف پول

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



    # تغییر وضعیت Order

    order.status = 'paid'

    order.save()



    return payment





@transaction.atomic
def create_online_payment(order, amount=None):
    """
    ایجاد Payment اولیه برای پرداخت آنلاین
    """

    if amount is None:

        amount = order.total_price



    payment = Payment.objects.create(

        user=order.user,

        order=order,

        online_amount=amount,

        status='pending'

    )


    return payment





@transaction.atomic
def process_mixed_payment(order, wallet):

    """
    پرداخت ترکیبی Wallet + Online
    """

    total_amount = order.total_price


    wallet_amount = min(
        wallet.balance,
        total_amount
    )

    online_amount = total_amount - wallet_amount

    if wallet_amount > 0:

        wallet.balance -= wallet_amount

        wallet.save()


    payment = Payment.objects.create(

        user=order.user,

        order=order,

        wallet_amount=wallet_amount,

        online_amount=online_amount,

        status='pending'

    )



    if wallet_amount > 0:

        WalletTransaction.objects.create(

            wallet=wallet,

            payment=payment,

            transaction_type='payment',

            amount=-wallet_amount,

            description=f"Wallet payment for Order {order.id}"

        )



    return payment




@transaction.atomic
def complete_online_payment(
        payment,
        transaction_id,
        gateway_response=None
):
    """
    تایید پرداخت آنلاین بعد از Callback بانک
    """

    # جلوگیری از ثبت دوباره Callback
    if payment.status == 'success':

        raise ValueError(
            "Payment already completed"
        )

    payment.status = 'success'

    payment.transaction_id = transaction_id

    payment.gateway_response = gateway_response

    payment.paid_at = timezone.now()

    payment.save()

    order = payment.order

    # محاسبه مجموع پرداخت‌های موفق برای این سفارش

    paid_amount = sum(

        p.total_paid()

        for p in order.payments.filter(
            status='success'
        )

    )

    # اگر کل مبلغ سفارش پرداخت شده باشد
    if paid_amount >= order.total_price:

        order.status = 'paid'

        order.save()

    return payment




@transaction.atomic
def refund_wallet_payment(payment):
    """
    برگشت مبلغ برداشت شده از Wallet
    در صورت شکست پرداخت آنلاین
    """
    if payment.wallet_amount <= 0:

        return payment

    wallet = Wallet.objects.get(
        user=payment.user
    )

    refund_amount = payment.wallet_amount

    # برگشت موجودی کیف پول

    wallet.balance += refund_amount

    wallet.save()

    # ثبت تراکنش Refund

    WalletTransaction.objects.create(

        wallet=wallet,

        payment=payment,

        transaction_type='refund',

        amount=refund_amount,

        description=f"Refund for Order {payment.order.id}"

    )

    # صفر کردن مبلغ Wallet در Payment
    # چون دیگر پرداخت نشده است

    payment.wallet_amount = 0

    payment.status = 'failed'

    payment.save()

    return payment

