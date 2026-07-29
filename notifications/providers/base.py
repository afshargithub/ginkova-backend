from abc import ABC, abstractmethod


class BaseNotificationProvider(ABC):

    """
    Base class for all notification providers
    """


    @abstractmethod
    def send(
        self,
        notification
    ):
        pass