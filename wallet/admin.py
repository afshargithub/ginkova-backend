from django.contrib import admin
from .models import Wallet, WalletTransaction


class WalletTransactionInline(admin.TabularInline):

    model = WalletTransaction

    extra = 0

    readonly_fields = (
        'payment',
        'transaction_type',
        'amount',
        'description',
        'created_at',
    )
    
    
    
@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'balance',
        'created_at',
        'updated_at',
    )

    search_fields = (
        'user__username',
        'user__email',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )
    
    inlines = [WalletTransactionInline]


@admin.register(WalletTransaction)
class WalletTransactionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'wallet',
        'payment',
        'transaction_type',
        'amount',
        'created_at',
    )

    list_filter = (
        'transaction_type',
        'created_at',
    )

    search_fields = (
        'wallet__user__username',
        'payment__payment_number',
    )
        # 'payment__id',

    readonly_fields = (
        'created_at',
    )

    fieldsets = (

        (
            'Transaction Information',
            {
                'fields': (
                    'wallet',
                    'payment',
                    'transaction_type',
                    'amount',
                    'description',
                )
            }
        ),

        (
            'Date',
            {
                'fields': (
                    'created_at',
                )
            }
        ),

    )