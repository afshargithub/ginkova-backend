from django.urls import path

from .api import (RecipeNutritionAPIView, MealNutritionAPIView)


urlpatterns = [

    path("recipe/<int:recipe_id>/", RecipeNutritionAPIView.as_view(), name="recipe_nutrition"),
    path("meal/<int:meal_id>/", MealNutritionAPIView.as_view(), name="meal_nutrition"),

]