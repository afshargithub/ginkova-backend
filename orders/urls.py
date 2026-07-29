from django.urls import path

from .api import (CheckoutAPIView, OrderListAPIView, OrderStatusAPIView, OrderDetailAPIView)

urlpatterns = [

    path('', OrderListAPIView.as_view(), name='order_list'),
    path('checkout/', CheckoutAPIView.as_view(), name='checkout'),
    path('status/', OrderStatusAPIView.as_view(), name='order_status'),
    path('<int:order_id>/', OrderDetailAPIView.as_view(), name='order_detail'),

]