from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Restaurant, RestaurantMeal
from .serializers import (
    RestaurantSerializer,
    RestaurantMealSerializer,
)




class RestaurantListAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        restaurants = Restaurant.objects.filter(
            is_active=True
        ).order_by("name")

        serializer = RestaurantSerializer(
            restaurants,
            many=True
        )

        return Response(serializer.data)




class RestaurantMealListAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        meals = RestaurantMeal.objects.filter(
            is_available=True
        )

        category = request.query_params.get("category")

        if category:

            meals = meals.filter(
                meal__categories__name=category
            )

        serializer = RestaurantMealSerializer(
            meals,
            many=True
        )

        return Response(serializer.data)




class MealRestaurantsAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request, meal_id):

        restaurant_meals = RestaurantMeal.objects.filter(
            meal_id=meal_id,
            is_available=True
        )

        serializer = RestaurantMealSerializer(
            restaurant_meals,
            many=True
        )

        return Response(serializer.data)
    
    
    
    
class RestaurantMealsAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def get(self, request, restaurant_id):

        restaurant_meals = RestaurantMeal.objects.filter(
            restaurant_id=restaurant_id,
            is_available=True
        )


        serializer = RestaurantMealSerializer(
            restaurant_meals,
            many=True
        )


        return Response(
            serializer.data
        )