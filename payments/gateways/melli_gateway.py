from .base import BasePaymentGateway


class MelliGateway(BasePaymentGateway):

    code = "melli"

    display_name = "Bank Melli Iran"


    def create_payment(self, payment):

        raise NotImplementedError(
            "Melli gateway not implemented yet"
        )


    def verify_payment(
            self,
            payment,
            transaction_id
    ):

        raise NotImplementedError(
            "Melli verification not implemented yet"
        )


    def refund_payment(self, payment):

        raise NotImplementedError(
            "Melli refund not implemented yet"
        )