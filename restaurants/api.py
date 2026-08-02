from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
    Restaurant,
    RestaurantMeal,
)
from .serializers import (
    RestaurantMealSerializer,
    RestaurantSerializer,
)


class RestaurantListAPIView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        restaurants = (
            Restaurant.objects
            .filter(
                is_active=True,
            )
            .prefetch_related(
                "translations",
            )
            .order_by(
                "name",
            )
        )

        serializer = RestaurantSerializer(
            restaurants,
            many=True,
            context={
                "request": request,
            },
        )

        return Response(serializer.data)


class RestaurantMealListAPIView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        restaurant_meals = (
            RestaurantMeal.objects
            .filter(
                is_available=True,
            )
            .select_related(
                "restaurant",
                "meal",
            )
            .prefetch_related(
                "restaurant__translations",
                "meal__translations",
            )
        )

        category = request.query_params.get(
            "category"
        )

        if category:
            restaurant_meals = (
                restaurant_meals
                .filter(
                    meal__categories__name=category,
                )
                .distinct()
            )

        serializer = RestaurantMealSerializer(
            restaurant_meals,
            many=True,
            context={
                "request": request,
            },
        )

        return Response(serializer.data)


class MealRestaurantsAPIView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, meal_id):
        restaurant_meals = (
            RestaurantMeal.objects
            .filter(
                meal_id=meal_id,
                is_available=True,
            )
            .select_related(
                "restaurant",
                "meal",
            )
            .prefetch_related(
                "restaurant__translations",
                "meal__translations",
            )
        )

        serializer = RestaurantMealSerializer(
            restaurant_meals,
            many=True,
            context={
                "request": request,
            },
        )

        return Response(serializer.data)


class RestaurantMealsAPIView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(
        self,
        request,
        restaurant_id,
    ):
        restaurant_meals = (
            RestaurantMeal.objects
            .filter(
                restaurant_id=restaurant_id,
                is_available=True,
            )
            .select_related(
                "restaurant",
                "meal",
            )
            .prefetch_related(
                "restaurant__translations",
                "meal__translations",
            )
        )

        serializer = RestaurantMealSerializer(
            restaurant_meals,
            many=True,
            context={
                "request": request,
            },
        )

        return Response(serializer.data)