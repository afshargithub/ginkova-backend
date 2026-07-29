from django.db import models
from django.conf import settings

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType



# =====================================================
# Notification Channel
# =====================================================

class NotificationChannel(models.Model):

    """
    کانال‌های ارسال Notification

    Examples:
    push
    sms
    email
    whatsapp
    """

    code = models.CharField(
        max_length=30,
        unique=True
    )


    display_name = models.CharField(
        max_length=100
    )


    provider = models.CharField(
        max_length=100
    )


    is_enabled = models.BooleanField(
        default=True
    )


    priority = models.PositiveIntegerField(
        default=1
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return self.display_name





# =====================================================
# Notification Template
# =====================================================

class NotificationTemplate(models.Model):

    """
    Template پیام‌ها

    Example:

    event_code:
        order_delivered

    message:
        Hello {{first_name}}
        Your order {{order_id}} delivered
    """


    event_code = models.CharField(
        max_length=100
    )


    language = models.CharField(
        max_length=10,
        default="en"
    )


    title = models.CharField(
        max_length=200
    )


    message = models.TextField()


    is_active = models.BooleanField(
        default=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )


    class Meta:

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "event_code",
                    "language"
                ],
                name="unique_notification_template"
            )

        ]


    def __str__(self):

        return self.event_code





# =====================================================
# Notification
# =====================================================

class Notification(models.Model):

    """
    Notification واقعی ارسال شده برای User
    """


    STATUS_CHOICES = (

        ("pending", "Pending"),

        ("sent", "Sent"),

        ("failed", "Failed"),

    )


    user = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.CASCADE,

        related_name="notifications"

    )


    channel = models.ForeignKey(

        NotificationChannel,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="notifications"

    )


    template = models.ForeignKey(

        NotificationTemplate,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="notifications"

    )


    title = models.CharField(

        max_length=200

    )


    message = models.TextField()



    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default="pending"

    )



    is_read = models.BooleanField(

        default=False

    )



    read_at = models.DateTimeField(

        null=True,

        blank=True

    )



    # =================================================
    # Generic Relation
    # ارتباط با هر Object در سیستم
    # =================================================


    content_type = models.ForeignKey(

        ContentType,

        on_delete=models.CASCADE,

        null=True,

        blank=True

    )


    object_id = models.PositiveIntegerField(

        null=True,

        blank=True

    )


    content_object = GenericForeignKey(

        "content_type",

        "object_id"

    )



    # اطلاعات زمان تولید Notification

    context_json = models.JSONField(

        default=dict,

        blank=True

    )



    sent_at = models.DateTimeField(

        null=True,

        blank=True

    )


    created_at = models.DateTimeField(

        auto_now_add=True

    )



    class Meta:

        indexes = [

            models.Index(
                fields=[
                    "user",
                    "is_read"
                ]
            ),

            models.Index(
                fields=[
                    "user",
                    "created_at"
                ]
            ),

            models.Index(
                fields=[
                    "status"
                ]
            ),

        ]



    def __str__(self):

        return f"{self.user} - {self.title}"