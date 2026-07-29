from django.conf import settings
from .fake import FakeGateway
from .mellat_gateway import MellatGateway
from .melli_gateway import MelliGateway
from .zarinpal_gateway import ZarinpalGateway
from django.conf import settings



class PaymentGatewayFactory:


    @staticmethod
    def get_gateway(
            gateway_code=None
    ):


        if gateway_code is None:

            gateway_code = getattr(
                settings,
                "PAYMENT_GATEWAY",
                "fake"
            )


        gateways = {

            "fake": FakeGateway(),

            "mellat": MellatGateway(),

            "melli": MelliGateway(),

            "zarinpal": ZarinpalGateway(),

        }


        gateway = gateways.get(
            gateway_code
        )


        if gateway is None:

            raise ValueError(
                "Invalid payment gateway"
            )


        return gateway




    @staticmethod
    def get_available_gateways():

        active_gateways = getattr(
            settings,
            "ACTIVE_PAYMENT_GATEWAYS",
            []
        )


        gateways = [

            FakeGateway(),

            MellatGateway(),

            MelliGateway(),

            ZarinpalGateway(),

        ]


        return [

            {
                "code": gateway.code,
                "name": gateway.display_name,
            }

            for gateway in gateways

            if gateway.code in active_gateways

        ]