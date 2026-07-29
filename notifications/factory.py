from .providers.push import (
    PushNotificationProvider
)

from .providers.sms import (
    SMSNotificationProvider
)

from .providers.email import (
    EmailNotificationProvider
)

from .providers.whatsapp import (
    WhatsAppNotificationProvider
)



class NotificationProviderFactory:


    PROVIDERS = {

        "push":
            PushNotificationProvider,

        "sms":
            SMSNotificationProvider,

        "email":
            EmailNotificationProvider,

        "whatsapp":
            WhatsAppNotificationProvider,

    }



    @staticmethod
    def get_provider(
        channel_code
    ):

        provider_class = (
            NotificationProviderFactory.PROVIDERS.get(
                channel_code
            )
        )


        if not provider_class:

            raise ValueError(
                f"Unsupported notification channel: {channel_code}"
            )


        return provider_class()