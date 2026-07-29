from django.urls import path
from .views import test_meals
from .api import (MealDetailAPIView, MealListAPIView, MealCategoryListAPIView, MealByCategoryAPIView,)


urlpatterns = [

    path("", MealListAPIView.as_view(), name="meal_list"),
    path("<int:pk>/", MealDetailAPIView.as_view(), name="meal_detail"),
    path("categories/", MealCategoryListAPIView.as_view()),
    path("categories/<str:category>/", MealByCategoryAPIView.as_view(), name="meal_by_category"),
    path("test_meals/", test_meals, name="test_meals"),

]