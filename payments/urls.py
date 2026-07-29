from django.urls import path

from .api import (
    PaymentCreateAPIView,
    PaymentCallbackAPIView,
    PaymentGatewayListAPIView,
)

urlpatterns = [

    path('create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('callback/', PaymentCallbackAPIView.as_view(), name='payment_callback'),
    path('gateways/', PaymentGatewayListAPIView.as_view(), name='payment_gateways'),

]

