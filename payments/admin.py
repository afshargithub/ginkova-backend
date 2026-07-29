from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'order',
        'user',
        'online_amount',
        'wallet_amount',
        'payment_number',
        'cash_amount',
        'status',
        'gateway_name',
        'created_at',
    )


    list_filter = (
        'status',
        'gateway_name',
        'created_at',
    )


    search_fields = (
        'user__username',
        'user__email',
        'order__id',
        'transaction_id',
        'gateway_reference',
    )


    readonly_fields = (
        'created_at',
        'updated_at',
        'paid_at',
    )


    fieldsets = (

        (
            'Basic Information',
            {
                'fields': (
                    'user',
                    'order',
                    'status',
                )
            }
        ),


        (
            'Payment Amounts',
            {
                'fields': (
                    'online_amount',
                    'wallet_amount',
                    'cash_amount',
                    'payment_number',
                )
            }
        ),


        (
            'Gateway Information',
            {
                'fields': (
                    'gateway_name',
                    'transaction_id',
                    'gateway_reference',
                    'gateway_response',
                    'paid_at',
                )
            }
        ),


        (
            'Dates',
            {
                'fields': (
                    'created_at',
                    'updated_at',
                )
            }
        ),

    )