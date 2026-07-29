from django.contrib import admin

from .models import (
    NotificationChannel,
    NotificationTemplate,
    Notification,
)



# =====================================================
# Notification Channel Admin
# =====================================================

@admin.register(NotificationChannel)
class NotificationChannelAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "code",
        "display_name",
        "provider",
        "is_enabled",
        "priority",
        "created_at",
    )


    list_filter = (
        "is_enabled",
        "provider",
    )


    search_fields = (
        "code",
        "display_name",
        "provider",
    )


    ordering = (
        "priority",
        "code",
    )



# =====================================================
# Notification Template Admin
# =====================================================

@admin.register(NotificationTemplate)
class NotificationTemplateAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "event_code",
        "language",
        "title",
        "is_active",
        "created_at",
    )


    list_filter = (
        "language",
        "is_active",
        "event_code",
    )


    search_fields = (
        "event_code",
        "title",
        "message",
    )


    ordering = (
        "event_code",
        "language",
    )



# =====================================================
# Notification Admin
# =====================================================

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):


    list_display = (
        "id",
        "user",
        "title",
        "channel",
        "status",
        "is_read",
        "sent_at",
        "created_at",
    )


    list_filter = (
        "status",
        "channel",
        "is_read",
        "created_at",
    )


    search_fields = (
        "user__username",
        "user__email",
        "title",
        "message",
    )


    readonly_fields = (
        "created_at",
        "sent_at",
        "read_at",
        "content_type",
        "object_id",
        "content_object",
    )


    date_hierarchy = (
        "created_at"
    )


    ordering = (
        "-created_at",
    )


    fieldsets = (

        (
            "Notification Information",
            {
                "fields": (
                    "user",
                    "channel",
                    "template",
                    "title",
                    "message",
                    "status",
                    "is_read",
                    "read_at",
                )
            }
        ),


        (
            "Related Object",
            {
                "fields": (
                    "content_type",
                    "object_id",
                    "content_object",
                    "context_json",
                )
            }
        ),


        (
            "Dates",
            {
                "fields": (
                    "sent_at",
                    "created_at",
                )
            }
        ),

    )