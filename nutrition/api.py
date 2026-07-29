from rest_framework.views import APIView
from rest_framework.response import Response

from recipes.models import Recipe
from .services import (calculate_recipe_nutrition, calculate_meal_nutrition)
from meals.models import Meal


class RecipeNutritionAPIView(APIView):

    def get(self, request, recipe_id):

        try:
            recipe = Recipe.objects.get(
                id=recipe_id
            )

        except Recipe.DoesNotExist:

            return Response(
                {
                    "error": "Recipe not found"
                },
                status=404
            )


        nutrition = calculate_recipe_nutrition(
            recipe
        )


        return Response(
            {
                "recipe": recipe.name,
                "nutrition": nutrition
            }
        )
        
        

class MealNutritionAPIView(APIView):

    def get(self, request, meal_id):

        try:

            meal = Meal.objects.get(
                id=meal_id
            )

        except Meal.DoesNotExist:

            return Response(
                {
                    "error": "Meal not found"
                },
                status=404
            )

        nutrition = calculate_meal_nutrition(
            meal
        )

        return Response(
            {
                "meal": meal.name,
                "nutrition": nutrition
            }
        )