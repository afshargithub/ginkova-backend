from django.db import migrations


def populate_english_translations(
    apps,
    schema_editor,
):
    database_alias = schema_editor.connection.alias

    Ingredient = apps.get_model(
        "ingradients",
        "Ingredient",
    )

    IngredientTranslation = apps.get_model(
        "ingradients",
        "IngredientTranslation",
    )

    ingredients = (
        Ingredient.objects
        .using(database_alias)
        .all()
        .iterator()
    )

    for ingredient in ingredients:
        (
            IngredientTranslation.objects
            .using(database_alias)
            .get_or_create(
                ingredient_id=ingredient.id,
                language="en",
                defaults={
                    "name": ingredient.name,
                    "description": (
                        ingredient.description or ""
                    ),
                },
            )
        )


class Migration(migrations.Migration):

    dependencies = [
        ('ingradients', '0002_ingredienttranslation'),
    ]

    operations = [
        migrations.RunPython(
            populate_english_translations,
            migrations.RunPython.noop,
        ),
    ]