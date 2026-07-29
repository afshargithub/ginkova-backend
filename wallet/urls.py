from django.urls import path

from .api import (
    WalletAPIView,
    WalletTransactionAPIView,
    WalletChargeAPIView,
    WalletChargeCallbackAPIView,
)


urlpatterns = [

    path(
        "",
        WalletAPIView.as_view(),
        name="wallet"
    ),

    path(
        "transactions/",
        WalletTransactionAPIView.as_view(),
        name="wallet_transactions"
    ),

    path(
        "charge/",
        WalletChargeAPIView.as_view(),
        name="wallet_charge"
    ),
    
    path(
        "charge/callback/",
        WalletChargeCallbackAPIView.as_view(),
        name="wallet_charge_callback"
    ),

]