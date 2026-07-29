from .base import BasePaymentGateway


class MellatGateway(BasePaymentGateway):

    code = "mellat"

    display_name = "Bank Mellat"


    def create_payment(self, payment):

        raise NotImplementedError(
            "Mellat gateway not implemented yet"
        )


    def verify_payment(
            self,
            payment,
            transaction_id
    ):

        raise NotImplementedError(
            "Mellat verification not implemented yet"
        )


    def refund_payment(self, payment):

        raise NotImplementedError(
            "Mellat refund not implemented yet"
        )