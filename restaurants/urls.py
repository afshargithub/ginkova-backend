from django.urls import path

from .api import (
    RestaurantListAPIView,
    RestaurantMealListAPIView,
    MealRestaurantsAPIView,
    RestaurantMealsAPIView,
)


urlpatterns = [

    path(
        "",
        RestaurantListAPIView.as_view(),
        name="restaurant_list"
    ),

    path(
        "meals/",
        RestaurantMealListAPIView.as_view(),
        name="restaurant_meals"
    ),

    path(
        "meal/<int:meal_id>/restaurants/",
        MealRestaurantsAPIView.as_view(),
        name="meal_restaurants"
    ),

    path(
        "<int:restaurant_id>/meals/",
        RestaurantMealsAPIView.as_view(),
        name="restaurant_meals_by_restaurant"
    ),
]