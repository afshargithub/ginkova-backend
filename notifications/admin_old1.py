from django.contrib import admin

from .models import (
    NotificationChannel,
    NotificationTemplate,
    Notification,
)



@admin.register(NotificationChannel)
class NotificationChannelAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "display_name",
        "provider",
        "is_enabled",
        "priority",
    )

    list_filter = (
        "is_enabled",
    )

    search_fields = (
        "code",
        "display_name",
    )



@admin.register(NotificationTemplate)
class NotificationTemplateAdmin(admin.ModelAdmin):

    list_display = (
        "event_code",
        "language",
        "title",
        "is_active",
    )

    list_filter = (
        "language",
        "is_active",
    )

    search_fields = (
        "event_code",
        "title",
    )



@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "channel",
        "status",
        "is_read",
        "created_at",
    )

    list_filter = (
        "status",
        "channel",
        "is_read",
    )

    search_fields = (
        "user__username",
        "title",
        "message",
    )

    readonly_fields = (
        "created_at",
        "sent_at",
        "read_at",
        "content_type",
        "object_id",
    )