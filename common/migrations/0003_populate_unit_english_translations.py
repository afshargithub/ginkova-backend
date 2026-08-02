from django.db import migrations


def populate_unit_english_translations(
    apps,
    schema_editor,
):
    Unit = apps.get_model(
        "common",
        "Unit",
    )

    UnitTranslation = apps.get_model(
        "common",
        "UnitTranslation",
    )

    for unit in Unit.objects.all():
        UnitTranslation.objects.get_or_create(
            unit=unit,
            language="en",
            defaults={
                "name": unit.name,
            },
        )


def reverse_noop(
    apps,
    schema_editor,
):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_unittranslation'),
    ]

    operations = [
        migrations.RunPython(
            populate_unit_english_translations,
            reverse_noop,
        ),
    ]
