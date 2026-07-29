from .base import BaseNotificationProvider



class PushNotificationProvider(
    BaseNotificationProvider
):

    """
    Firebase Push Notification Provider
    """


    def send(
        self,
        notification
    ):

        # TODO:
        # Implement Firebase Cloud Messaging

        return {
            "success": True,
            "message": "Push notification sent"
        }