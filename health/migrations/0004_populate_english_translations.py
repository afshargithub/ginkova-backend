from django.db import migrations


def populate_english_translations(
    apps,
    schema_editor,
):
    HealthGoal = apps.get_model(
        "health",
        "HealthGoal",
    )

    HealthGoalTranslation = apps.get_model(
        "health",
        "HealthGoalTranslation",
    )

    Disease = apps.get_model(
        "health",
        "Disease",
    )

    DiseaseTranslation = apps.get_model(
        "health",
        "DiseaseTranslation",
    )

    for health_goal in HealthGoal.objects.all():
        HealthGoalTranslation.objects.get_or_create(
            health_goal=health_goal,
            language="en",
            defaults={
                "name": health_goal.name,
                "description": (
                    health_goal.description
                ),
            },
        )

    for disease in Disease.objects.all():
        DiseaseTranslation.objects.get_or_create(
            disease=disease,
            language="en",
            defaults={
                "name": disease.name,
                "description": disease.description,
            },
        )


def reverse_noop(
    apps,
    schema_editor,
):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_diseasetranslation_healthgoaltranslation'),
    ]

    operations = [
        migrations.RunPython(
            populate_english_translations,
            reverse_noop,
        ),
    ]