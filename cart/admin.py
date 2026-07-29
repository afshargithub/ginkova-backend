from django.contrib import admin

from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):

    model = CartItem

    extra = 1



@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'created_at',
        'updated_at',
    )


    search_fields = (
        'user__username',
        'user__email',
    )


    inlines = [
        CartItemInline,
    ]



@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):

    list_display = (
        'cart',
        'restaurant_meal',
        'quantity',
        'price',
        'created_at',
    )


    list_filter = (
        'created_at',
    )


    search_fields = (
        'restaurant_meal__meal__name',
        'restaurant_meal__restaurant__name',
    )