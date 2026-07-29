from django.db import models
from django.conf import settings

from orders.models import Order


class Payment(models.Model):

    PAYMENT_METHODS = (
        ('online', 'Online Gateway'),
        ('wallet', 'Wallet'),
        ('bank', 'Bank Transfer'),
    )


    PAYMENT_STATUS = (
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
        ('refunded', 'Refunded'),
    )


    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='payments'
    )


    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )


    method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS
    )


    status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='pending'
    )


    transaction_id = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )


    gateway_response = models.TextField(
        blank=True,
        null=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )

    wallet_transaction = models.OneToOneField(
        'wallet.WalletTransaction',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Payment {self.id} - {self.order.id}"