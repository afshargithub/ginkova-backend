from django.utils import timezone

from .factory import NotificationProviderFactory



class NotificationManager:


    @staticmethod
    def send(notification):

        try:

            channel_code = notification.channel.code


            provider = NotificationProviderFactory.get_provider(
                channel_code
            )


            response = provider.send(
                notification
            )


            if response.get("success"):

                notification.status = "sent"

                notification.sent_at = timezone.now()

            else:

                notification.status = "failed"


            notification.save(
                update_fields=[
                    "status",
                    "sent_at"
                ]
            )


            return response



        except Exception as e:


            notification.status = "failed"

            notification.save(
                update_fields=[
                    "status"
                ]
            )


            return {
                "success": False,
                "error": str(e)
            }