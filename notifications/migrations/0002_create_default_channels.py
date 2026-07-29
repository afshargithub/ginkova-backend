from django.db import migrations


def create_default_channels(apps, schema_editor):

    NotificationChannel = apps.get_model(
        "notifications",
        "NotificationChannel"
    )


    channels = [

        {
            "code": "push",
            "display_name": "Push Notification",
            "provider": "firebase",
            "is_enabled": True,
            "priority": 1,
        },

        {
            "code": "sms",
            "display_name": "SMS",
            "provider": "kavenegar",
            "is_enabled": False,
            "priority": 2,
        },

        {
            "code": "email",
            "display_name": "Email",
            "provider": "smtp",
            "is_enabled": False,
            "priority": 3,
        },

        {
            "code": "whatsapp",
            "display_name": "WhatsApp",
            "provider": "twilio",
            "is_enabled": False,
            "priority": 4,
        },

    ]


    for channel in channels:

        NotificationChannel.objects.get_or_create(
            code=channel["code"],
            defaults=channel
        )



def remove_default_channels(apps, schema_editor):

    NotificationChannel = apps.get_model(
        "notifications",
        "NotificationChannel"
    )


    NotificationChannel.objects.filter(
        code__in=[
            "push",
            "sms",
            "email",
            "whatsapp",
        ]
    ).delete()



class Migration(migrations.Migration):

    dependencies = [
        (
            "notifications",
            "0001_initial"
        ),
    ]


    operations = [

        migrations.RunPython(
            create_default_channels,
            remove_default_channels
        ),

    ]