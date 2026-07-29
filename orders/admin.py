from django.contrib import admin

from .models import Order, OrderItem



class OrderItemInline(admin.TabularInline):

    model = OrderItem

    extra = 0

    readonly_fields = (
        'restaurant_meal',
        'quantity',
        'price',
        'consumed_by'
    )



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'restaurant',
        'status',
        'total_price',
        'delivery_address',
        'created_at',
    )


    list_filter = (
        'restaurant',
        'status',
        'created_at',
    )


    search_fields = (
        'user__username',
        'user__email',
        'restaurant__name',
    )


    readonly_fields = (
        'created_at',
        'updated_at',
    )


    inlines = [
        OrderItemInline,
    ]



@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):

    list_display = (
        'order',
        'restaurant_meal',
        'quantity',
        'price',
        'consumed_by',
    )


    list_filter = (
        'consumed_by',
    )


    search_fields = (
        'restaurant_meal__meal__name',
        'restaurant_meal__restaurant__name',
        'order__user__username',
    )