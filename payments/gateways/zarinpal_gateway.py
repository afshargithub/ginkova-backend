from .base import BasePaymentGateway


class ZarinpalGateway(BasePaymentGateway):

    code = "zarinpal"

    display_name = "ZarinPal"


    def create_payment(self, payment):

        raise NotImplementedError(
            "ZarinPal gateway not implemented yet"
        )


    def verify_payment(
            self,
            payment,
            transaction_id
    ):

        raise NotImplementedError(
            "ZarinPal verification not implemented yet"
        )


    def refund_payment(self, payment):

        raise NotImplementedError(
            "ZarinPal refund not implemented yet"
        )