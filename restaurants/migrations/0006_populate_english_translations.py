from django.db import migrations


def populate_english_translations(
    apps,
    schema_editor,
):
    Restaurant = apps.get_model(
        "restaurants",
        "Restaurant",
    )

    RestaurantTranslation = apps.get_model(
        "restaurants",
        "RestaurantTranslation",
    )

    for restaurant in Restaurant.objects.all():
        RestaurantTranslation.objects.get_or_create(
            restaurant=restaurant,
            language="en",
            defaults={
                "name": restaurant.name,
                "address": restaurant.address,
            },
        )


def reverse_noop(
    apps,
    schema_editor,
):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_restauranttranslation_and_more'),
    ]

    operations = [
        migrations.RunPython(
            populate_english_translations,
            reverse_noop,
        ),
    ]
