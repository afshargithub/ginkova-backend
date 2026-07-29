from django.utils import timezone

from .base import BasePaymentGateway


class FakeGateway(BasePaymentGateway):

    code = "fake"

    display_name = "Fake Gateway"


    def create_payment(
        self,
        payment
    ):

        return {

            "success": True,

            "payment_id": payment.id,

            "redirect_url":
            "/fake-bank-page/"

        }


    def verify_payment(
        self,
        payment,
        transaction_id
    ):

        return {

            "success": True,

            "transaction_id":
            transaction_id,

            "paid_at":
            timezone.now()

        }


    def refund_payment(
        self,
        payment
    ):

        return {

            "success": True,

            "message":
            "Fake refund completed"

        }