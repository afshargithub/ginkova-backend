from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Notification
from .serializers import NotificationSerializer



# =====================================================
# لیست Notification های کاربر
# =====================================================

class NotificationListAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def get(self, request):

        notifications = Notification.objects.filter(
            user=request.user
        ).select_related(
            "channel",
            "template",
            "content_type"
        ).order_by(
            "-created_at"
        )


        serializer = NotificationSerializer(
            notifications,
            many=True
        )


        return Response(
            serializer.data
        )





# =====================================================
# تعداد Notification های خوانده نشده
# =====================================================

class NotificationUnreadCountAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def get(self, request):

        count = Notification.objects.filter(
            user=request.user,
            is_read=False
        ).count()


        return Response({

            "unread_count":
            count

        })





# =====================================================
# خواندن یک Notification
# =====================================================

class NotificationReadAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def patch(self, request, notification_id):

        try:

            notification = Notification.objects.get(
                id=notification_id,
                user=request.user
            )


        except Notification.DoesNotExist:

            return Response(
                {
                    "error":
                    "Notification not found"
                },
                status=404
            )


        if not notification.is_read:

            notification.is_read = True

            notification.read_at = timezone.now()

            notification.save(
                update_fields=[
                    "is_read",
                    "read_at"
                ]
            )


        return Response({

            "message":
            "Notification marked as read",

            "notification_id":
            notification.id

        })





# =====================================================
# خواندن همه Notification ها
# =====================================================

class NotificationReadAllAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def patch(self, request):

        updated = Notification.objects.filter(
            user=request.user,
            is_read=False
        ).update(

            is_read=True,

            read_at=timezone.now()

        )


        return Response({

            "message":
            "All notifications marked as read",

            "updated_count":
            updated

        })