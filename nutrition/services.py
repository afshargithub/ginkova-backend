from decimal import Decimal



def convert_to_gram(quantity, unit):

    """
    Convert recipe ingredient quantity
    into gram for nutrition calculation
    """


    if unit.unit_type == "weight":

        return quantity * unit.unit_factor



    elif unit.unit_type == "volume":

        # فعلاً بر اساس استاندارد آب
        # در آینده density برای هر Ingredient اضافه می‌شود

        return quantity * unit.unit_factor



    elif unit.unit_type == "count":

        raise ValueError(
            "Count unit needs ingredient weight definition"
        )



    raise ValueError(
        "Unsupported unit type"
    )



def calculate_recipe_nutrition(recipe):

    nutrition = {
        "calories": Decimal("0"),
        "protein": Decimal("0"),
        "carbohydrate": Decimal("0"),
        "fat": Decimal("0"),
        "fiber": Decimal("0"),
        "sugar": Decimal("0"),
        "sodium": Decimal("0"),
    }


    for item in recipe.ingredients.all():

        ingredient = item.ingredient


        gram_quantity = convert_to_gram(
            item.quantity,
            item.unit
        )


        factor = gram_quantity / Decimal("100")


        nutrition["calories"] += (
            ingredient.calories * factor
        )

        nutrition["protein"] += (
            ingredient.protein * factor
        )

        nutrition["carbohydrate"] += (
            ingredient.carbohydrate * factor
        )

        nutrition["fat"] += (
            ingredient.fat * factor
        )

        nutrition["fiber"] += (
            ingredient.fiber * factor
        )

        nutrition["sugar"] += (
            ingredient.sugar * factor
        )

        nutrition["sodium"] += (
            ingredient.sodium * factor
        )


    return nutrition



def calculate_meal_nutrition(meal):

    nutrition = {
        "calories": Decimal("0"),
        "protein": Decimal("0"),
        "carbohydrate": Decimal("0"),
        "fat": Decimal("0"),
        "fiber": Decimal("0"),
        "sugar": Decimal("0"),
        "sodium": Decimal("0"),
    }


    for recipe in meal.recipes.all():

        recipe_nutrition = calculate_recipe_nutrition(
            recipe
        )


        for key in nutrition:

            nutrition[key] += recipe_nutrition[key]


    return nutrition