from django.db import migrations


def populate_english_translations(
    apps,
    schema_editor,
):
    database_alias = schema_editor.connection.alias

    Recipe = apps.get_model(
        "recipes",
        "Recipe",
    )

    RecipeTranslation = apps.get_model(
        "recipes",
        "RecipeTranslation",
    )

    recipes = (
        Recipe.objects
        .using(database_alias)
        .all()
        .iterator()
    )

    for recipe in recipes:
        (
            RecipeTranslation.objects
            .using(database_alias)
            .get_or_create(
                recipe_id=recipe.id,
                language="en",
                defaults={
                    "name": recipe.name,
                    "description": (
                        recipe.description or ""
                    ),
                },
            )
        )


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipetranslation'),
    ]

    operations = [
        migrations.RunPython(
            populate_english_translations,
            migrations.RunPython.noop,
        ),
    ]
