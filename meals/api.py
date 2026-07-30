from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Meal, MealCategory
from .serializers import (MealSerializer, MealDetailSerializer, MealCategorySerializer,)


class MealListAPIView(APIView):

    def get(self, request):

        meals = Meal.objects.filter(
            is_active=True)

        category_id = request.query_params.get(
            "category")

        if category_id:

            meals = meals.filter(
                categories__id=category_id)

        serializer = MealSerializer(
            meals,
            many=True)

        return Response(
            serializer.data
        )
        
        

class MealDetailAPIView(APIView):

    def get(self, request, pk):

        try:

            meal = Meal.objects.get(
                id=pk,
                is_active=True
            )

        except Meal.DoesNotExist:

            return Response(
                {
                    "error": "Meal not found"
                },
                status=404
            )


        serializer = MealDetailSerializer(
            meal
        )


        return Response(
            serializer.data
        )
        

class MealCategoryListAPIView(APIView):

    def get(self, request):

        categories = MealCategory.objects.all()

        serializer = MealCategorySerializer(
            categories,
            many=True
        )

        return Response(
            serializer.data
        )    
        
        


class MealByCategoryAPIView(APIView):

    def get(self, request, category):

        meals = Meal.objects.filter(
            is_active=True,
            categories__name__iexact=category
        )

        serializer = MealSerializer(
            meals,
            many=True
        )

        return Response(
            serializer.data
        )