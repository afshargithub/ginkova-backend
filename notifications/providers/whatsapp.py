from .base import BaseNotificationProvider



class WhatsAppNotificationProvider(
    BaseNotificationProvider
):


    """
    WhatsApp Provider

    Example:
    Twilio WhatsApp API
    """



    def send(
        self,
        notification
    ):

        # TODO:
        # Implement WhatsApp API

        return {
            "success": True,
            "message": "WhatsApp sent"
        }