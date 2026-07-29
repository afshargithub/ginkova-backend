from abc import ABC, abstractmethod


class BasePaymentGateway(ABC):


    @abstractmethod
    def create_payment(
        self,
        payment
    ):
        pass


    @abstractmethod
    def verify_payment(
        self,
        payment,
        transaction_id
    ):
        pass


    @abstractmethod
    def refund_payment(
        self,
        payment
    ):
        pass