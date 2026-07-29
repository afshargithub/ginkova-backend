from django.db import models
from django.conf import settings


class Wallet(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="wallet"
    )

    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return f"{self.user.username} Wallet"



class WalletTransaction(models.Model):

    TRANSACTION_TYPE = (
        ('charge', 'Charge'),
        ('payment', 'Payment'),
        ('refund', 'Refund'),
    )


    wallet = models.ForeignKey(
        Wallet,
        related_name='transactions',
        on_delete=models.CASCADE
    )


    payment = models.OneToOneField(
        'payments.Payment',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='wallet_transaction'
    )


    transaction_type = models.CharField(
        max_length=20,
        choices=TRANSACTION_TYPE,
        db_index=True
    )


    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )


    description = models.CharField(
        max_length=255,
        blank=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f"{self.wallet.user.username} - {self.amount}"
    
        