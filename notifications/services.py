from django.utils import timezone

from .models import (
    Notification,
    NotificationTemplate,
    NotificationChannel,
)

from .manager import NotificationManager



class NotificationService:


    @staticmethod
    def send(
        event_code,
        user,
        context=None,
        language="en",
        related_object=None
    ):
        """
        ایجاد و ارسال Notification
        """


        if context is None:
            context = {}


        template = NotificationTemplate.objects.filter(
            event_code=event_code,
            language=language,
            is_active=True
        ).first()


        if not template:

            raise ValueError(
                f"Notification template not found: {event_code}"
            )


        channel = NotificationChannel.objects.filter(
            is_enabled=True
        ).order_by(
            "priority"
        ).first()


        if not channel:

            raise ValueError(
                "No active notification channel"
            )


        message = template.message


        for key, value in context.items():

            message = message.replace(
                "{{" + key + "}}",
                str(value)
            )


        notification = Notification.objects.create(

            user=user,

            channel=channel,

            template=template,

            title=template.title,

            message=message,

            context_json=context

        )


        if related_object:

            notification.content_object = (
                related_object
            )

            notification.save()


        try:
            response = NotificationManager.send(notification)
            notification.status="sent"
            notification.sent_at=timezone.now()
        except Exception as e:
            notification.status="failed"
            response=str(e)
        notification.save()


        return notification, response