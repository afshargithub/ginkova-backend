from django.urls import path

from .api import (CartAPIView, CartAddAPIView, CartUpdateAPIView, CartRemoveAPIView)



urlpatterns = [

    path('',     CartAPIView.as_view(), name='cart'),
    path('add/', CartAddAPIView.as_view(), name='cart-add'),
    path('update/', CartUpdateAPIView.as_view(), name='cart-update'),
    path('remove/', CartRemoveAPIView.as_view(), name='cart-remove'),

]
