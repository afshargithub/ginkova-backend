from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.i18n import get_request_language
from common.localization import (
    get_localized_name,
)
from meals.models import Meal
from recipes.models import Recipe

from .services import (
    calculate_meal_nutrition,
    calculate_recipe_nutrition,
)


ERROR_MESSAGES = {
    "en": {
        "recipe_not_found": (
            "Recipe not found."
        ),
        "meal_not_found": (
            "Meal not found."
        ),
    },

    "fa": {
        "recipe_not_found": (
            "دستور غذا یافت نشد."
        ),
        "meal_not_found": (
            "غذا یافت نشد."
        ),
    },

    "hy": {
        "recipe_not_found": (
            "Բաղադրատոմսը չի գտնվել։"
        ),
        "meal_not_found": (
            "Ուտեստը չի գտնվել։"
        ),
    },

    "ru": {
        "recipe_not_found": (
            "Рецепт не найден."
        ),
        "meal_not_found": (
            "Блюдо не найдено."
        ),
    },
}


def get_error_message(
    language,
    message_key,
):
    language_messages = ERROR_MESSAGES.get(
        language,
        ERROR_MESSAGES["en"],
    )

    return language_messages[message_key]


class RecipeNutritionAPIView(APIView):

    def get(
        self,
        request,
        recipe_id,
    ):
        language = get_request_language(
            request
        )

        try:
            recipe = (
                Recipe.objects
                .prefetch_related(
                    "translations",
                    "ingredients",
                    "ingredients__ingredient",
                    "ingredients__unit",
                )
                .get(
                    id=recipe_id,
                )
            )

        except Recipe.DoesNotExist:
            return Response(
                {
                    "error": get_error_message(
                        language,
                        "recipe_not_found",
                    ),
                },
                status=(
                    status.HTTP_404_NOT_FOUND
                ),
            )

        nutrition = (
            calculate_recipe_nutrition(
                recipe
            )
        )

        return Response(
            {
                "recipe": get_localized_name(
                    recipe,
                    language,
                ),
                "nutrition": nutrition,
            }
        )


class MealNutritionAPIView(APIView):

    def get(
        self,
        request,
        meal_id,
    ):
        language = get_request_language(
            request
        )

        try:
            meal = (
                Meal.objects
                .prefetch_related(
                    "translations",
                    "recipes",
                    "recipes__ingredients",
                    (
                        "recipes__ingredients"
                        "__ingredient"
                    ),
                    (
                        "recipes__ingredients"
                        "__unit"
                    ),
                )
                .get(
                    id=meal_id,
                )
            )

        except Meal.DoesNotExist:
            return Response(
                {
                    "error": get_error_message(
                        language,
                        "meal_not_found",
                    ),
                },
                status=(
                    status.HTTP_404_NOT_FOUND
                ),
            )

        nutrition = calculate_meal_nutrition(
            meal
        )

        return Response(
            {
                "meal": get_localized_name(
                    meal,
                    language,
                ),
                "nutrition": nutrition,
            }
        )