from django.db import transaction

from cart.models import Cart
from notifications.services import NotificationService
from .models import Order, OrderItem


@transaction.atomic
def create_order_from_cart(
    user,
    delivery_address=None
):

    cart, created = Cart.objects.get_or_create(user=user)   # cart = Cart.objects.get(user=user)

    if not cart.items.exists():

        raise ValueError(
            "Cart is empty"
        )


    restaurants = set(item.restaurant_meal.restaurant_id for item in cart.items.all())
    if len(restaurants) != 1:
        raise ValueError("Cart contains meals from multiple restaurants.")
    # فعلاً MVP:
    # یک Cart فقط یک Restaurant دارد
    restaurant = (cart.items.first().restaurant_meal.restaurant)

    total_price = 0

    for item in cart.items.all():

        total_price += (
            item.quantity *
            item.price
        )

    order = Order.objects.create(

        user=user,

        restaurant=restaurant,

        delivery_address=delivery_address,

        total_price=total_price,

        status='pending_payment'

    )

    for item in cart.items.all():

        OrderItem.objects.create(

            order=order,

            restaurant_meal=item.restaurant_meal,

            quantity=item.quantity,

            price=item.price,

            consumed_by=item.consumed_by

        )

    cart.items.all().delete()

    return order


@transaction.atomic
def update_order_status(
    order,
    new_status
):
    """
    تغییر وضعیت سفارش با رعایت قوانین
    """

    allowed_transitions = {

        'pending_payment': [
            'paid',
            'cancelled'
        ],


        'paid': [
            'confirmed',
            'cancelled'
        ],


        'confirmed': [
            'preparing'
        ],


        'preparing': [
            'ready'
        ],


        'ready': [
            'picked_up'
        ],


        'picked_up': [
            'out_for_delivery'
        ],


        'out_for_delivery': [
            'delivered'
        ],


        'delivered': [],


        'cancelled': [],

    }


    current_status = order.status


    if new_status not in allowed_transitions.get(
        current_status,
        []
    ):

        raise ValueError(

            f"Cannot change order status "
            f"from {current_status} "
            f"to {new_status}"

        )


    order.status = new_status

    order.save(update_fields=["status"])
    
    # ----- start of notification sending -----
    event_map = {
        "confirmed": "order_confirmed",
        "preparing": "order_preparing",
        "ready": "order_ready",
        "out_for_delivery": "order_out_for_delivery",
        "delivered": "order_delivered",
    }
    event_code = event_map.get(new_status)
    if event_code:
        NotificationService.send(
            event_code=event_code,
            user=order.user,
            context={
                "order_id": order.id
            },
            related_object=order
        )
    # ----- end of notification sending -----


    return order