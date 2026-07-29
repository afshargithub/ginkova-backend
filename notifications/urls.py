from django.urls import path

from .api import (
    NotificationListAPIView,
    NotificationUnreadCountAPIView,
    NotificationReadAPIView,
    NotificationReadAllAPIView,
)


urlpatterns = [

    # لیست Notification های کاربر
    path(
        "",
        NotificationListAPIView.as_view(),
        name="notification-list"
    ),


    # تعداد Notification های خوانده نشده
    path(
        "unread-count/",
        NotificationUnreadCountAPIView.as_view(),
        name="notification-unread-count"
    ),


    # خواندن یک Notification
    path(
        "<int:notification_id>/read/",
        NotificationReadAPIView.as_view(),
        name="notification-read"
    ),


    # خواندن همه Notification ها
    path(
        "read-all/",
        NotificationReadAllAPIView.as_view(),
        name="notification-read-all"
    ),

]