
from django.db import migrations


def populate_english_translations(
    apps,
    schema_editor,
):
    database_alias = (
        schema_editor.connection.alias
    )

    Meal = apps.get_model(
        "meals",
        "Meal",
    )

    MealTranslation = apps.get_model(
        "meals",
        "MealTranslation",
    )

    MealCategory = apps.get_model(
        "meals",
        "MealCategory",
    )

    MealCategoryTranslation = (
        apps.get_model(
            "meals",
            "MealCategoryTranslation",
        )
    )

    meal_translations = []

    for meal in (
        Meal.objects
        .using(database_alias)
        .all()
        .iterator()
    ):
        meal_translations.append(
            MealTranslation(
                meal_id=meal.id,
                language="en",
                name=meal.name,
                description=(
                    meal.description or ""
                ),
            )
        )

    MealTranslation.objects.using(
        database_alias
    ).bulk_create(
        meal_translations,
        batch_size=500,
        ignore_conflicts=True,
    )

    category_translations = []

    for category in (
        MealCategory.objects
        .using(database_alias)
        .all()
        .iterator()
    ):
        category_translations.append(
            MealCategoryTranslation(
                meal_category_id=category.id,
                language="en",
                name=category.name,
                description=(
                    category.description or ""
                ),
            )
        )

    MealCategoryTranslation.objects.using(
        database_alias
    ).bulk_create(
        category_translations,
        batch_size=500,
        ignore_conflicts=True,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0005_mealcategorytranslation_mealtranslation'),
    ]

    operations = [
        migrations.RunPython(
            populate_english_translations,
            migrations.RunPython.noop,
        ),
    ]