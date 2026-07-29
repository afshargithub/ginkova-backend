from django.db import models
from django.conf import settings
import uuid
from orders.models import Order


class Payment(models.Model):

    PAYMENT_STATUS = (
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
        ('refunded', 'Refunded'),
    )


    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='payments'
    )


    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
        related_name='payments',
        null=True,
        blank=True
    )


    # مبلغ پرداخت آنلاین
    online_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )


    # مبلغ برداشت شده از Wallet
    wallet_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )


    # برای آینده (پرداخت نقدی)
    cash_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )


    status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='pending'
    )


    # اطلاعات درگاه پرداخت

    gateway_name = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )


    transaction_id = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )


    gateway_reference = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )


    gateway_response = models.TextField(
        blank=True,
        null=True
    )


    payment_number = models.CharField(
        max_length=50,
        unique=True,  #             بعدا درست کنم , درست کردم
        editable=False
    )
        # blank=True,
        # null=True


    paid_at = models.DateTimeField(
        blank=True,
        null=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )


    def total_paid(self):

        return (
            self.online_amount +
            self.wallet_amount +
            self.cash_amount
        )

    
    def save(self, *args, **kwargs):
        if not self.payment_number:
            self.payment_number = (
                f"PAY-{uuid.uuid4().hex[:10].upper()}"
            )
        super().save(*args, **kwargs)    
    
    def is_successful(self):
        return self.status == 'success'
    
    
    def __str__(self):
        if self.order:
            return f"Payment {self.id} - Order {self.order.id}"
        else:
            return f"Payment {self.id} - Wallet Charge"