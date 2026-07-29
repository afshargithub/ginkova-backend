from rest_framework.views import APIView
from rest_framework.response import Response

from .models import RestaurantMeal
from .serializers import RestaurantMealSerializer


class RestaurantMealListAPIView(APIView):

    def get(self, request):

        meals = RestaurantMeal.objects.filter(is_available=True)

        category = request.query_params.get("category")

        if category:
            meals = meals.filter(meal__categories__name=category)

        serializer = RestaurantMealSerializer(meals, many=True)

        return Response(
            serializer.data
        )
        
        
        
    

class MealRestaurantsAPIView(APIView):

    def get(self, request, meal_id):

        restaurant_meals = RestaurantMeal.objects.filter(
            meal_id=meal_id,
            is_available=True
        )

        serializer = RestaurantMealSerializer(
            restaurant_meals,
            many=True
        )

        return Response(
            serializer.data
        )