from .base import BaseNotificationProvider



class SMSNotificationProvider(
    BaseNotificationProvider
):


    """
    SMS Provider

    Example:
    Kavenegar
    Twilio
    """



    def send(
        self,
        notification
    ):

        # TODO:
        # Implement SMS gateway

        return {
            "success": True,
            "message": "SMS sent"
        }