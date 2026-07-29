from rest_framework import serializers

from .models import Notification



class NotificationSerializer(serializers.ModelSerializer):

    channel_name = serializers.CharField(
        source="channel.display_name",
        read_only=True
    )


    template_event = serializers.CharField(
        source="template.event_code",
        read_only=True
    )


    related_object_type = serializers.SerializerMethodField()

    related_object_id = serializers.IntegerField(
        source="object_id",
        read_only=True
    )


    class Meta:

        model = Notification

        fields = (
            "id",

            "title",

            "message",

            "channel",
            "channel_name",

            "template_event",

            "status",

            "is_read",

            "read_at",

            "related_object_type",
            "related_object_id",

            "context_json",

            "sent_at",

            "created_at",
        )


        read_only_fields = (
            "id",
            "status",
            "created_at",
            "sent_at",
            "read_at",
        )



    def get_related_object_type(self, obj):

        if obj.content_type:

            return obj.content_type.model

        return None