from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    

    email = models.EmailField(
        unique=True,
        null=True,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True
    )

    phone_verified = models.BooleanField(
        default=False
    )

    email_verified = models.BooleanField(
        default=False
    )

    language = models.CharField(
        max_length=5,
        default='fa'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return self.email or self.phone or self.username
    



class UserAddress(models.Model):

    ADDRESS_TYPE = (
        ('home', 'Home'),
        ('work', 'Work'),
        ('other', 'Other'),
    )


    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='addresses',
        on_delete=models.CASCADE
    )


    title = models.CharField(
        max_length=50,
        help_text="Example: Home, Office"
    )


    address_type = models.CharField(
        max_length=10,
        choices=ADDRESS_TYPE,
        default='home'
    )


    country = models.CharField(
        max_length=50,
        default='Armenia'
    )


    city = models.CharField(
        max_length=100,
        default='Yerevan'
    )


    address_line = models.TextField()


    postal_code = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )


    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True
    )


    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True
    )


    receiver_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )


    receiver_phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )


    is_default = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )



    def __str__(self):
        return f"{self.user.username} - {self.title}"