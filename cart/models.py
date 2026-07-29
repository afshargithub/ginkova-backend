from django.db import models
from django.conf import settings
from common.choices import CONSUMED_BY_CHOICES
from restaurants.models import RestaurantMeal


class Cart(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return f"{self.user.username} Cart"






class CartItem(models.Model):

    cart = models.ForeignKey(
        Cart,
        related_name='items',
        on_delete=models.CASCADE
    )

    restaurant_meal = models.ForeignKey(
        RestaurantMeal,
        on_delete=models.PROTECT,
        related_name="cart_items"
        # default=1 #alaki & temprory for one time running
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

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def subtotal(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.restaurant_meal.meal.name} x {self.quantity}"