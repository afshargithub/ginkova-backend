from django.db import models
from django.conf import settings
from common.choices import CONSUMED_BY_CHOICES
from restaurants.models import Restaurant, RestaurantMeal


class Order(models.Model):

    STATUS_CHOICES = (
        ('pending_payment', 'Pending Payment'),
        ('paid', 'Paid'),
        ('confirmed', 'Confirmed'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready'),
        ('picked_up', 'Picked Up'),
        ('out_for_delivery', 'Out For Delivery'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )


    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.PROTECT,
        related_name='orders'
        # , default=1 # alaki & temprory for one time running
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending_payment'
    )


    total_price = models.DecimalField(
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


    delivery_address = models.ForeignKey(
        'accounts.UserAddress',
        on_delete=models.PROTECT,
        related_name='orders',
        null=True,
        blank=True  
    )

    def __str__(self):
        return f"Order {self.id} - {self.user}"



class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )

    restaurant_meal = models.ForeignKey(
        RestaurantMeal,
        on_delete=models.PROTECT
        # , default=1 # alaki & temprory for one time running
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    consumed_by = models.CharField(
        max_length=10,
        choices=CONSUMED_BY_CHOICES,
        default='self'
    )

    def subtotal(self):
        return self.quantity * self.price
    
    def __str__(self):
        return f"{self.restaurant_meal.meal.name} x {self.quantity}"