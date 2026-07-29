from .base import BaseNotificationProvider



class EmailNotificationProvider(
    BaseNotificationProvider
):


    """
    Email Provider

    Example:
    SMTP
    SendGrid
    """



    def send(
        self,
        notification
    ):

        # TODO:
        # Implement email service

        return {
            "success": True,
            "message": "Email sent"
        }