from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Meal, MealCategory
from .serializers import (
    MealCategorySerializer,
    MealDetailSerializer,
    MealSerializer,
)


class MealListAPIView(APIView):

    def get(self, request):
        meals = (
            Meal.objects
            .filter(is_active=True)
            .prefetch_related(
                "categories",
                "translations",
                "recipes",
                "recipes__ingredients",
                "recipes__ingredients__ingredient",
                "recipes__ingredients__unit",
            )
            .order_by("name")
        )

        category_id = request.query_params.get(
            "category"
        )

        if category_id:
            meals = (
                meals
                .filter(
                    categories__id=category_id
                )
                .distinct()
            )

        serializer = MealSerializer(
            meals,
            many=True,
            context={
                "request": request,
            },
        )

        return Response(serializer.data)


class MealDetailAPIView(APIView):

    def get(self, request, pk):
        try:
            meal = (
                Meal.objects
                .prefetch_related(
                    "categories",
                    "translations",
                    "recipes",
                    "recipes__translations",
                    "recipes__ingredients",
                    (
                        "recipes__ingredients"
                        "__ingredient"
                    ),
                    (
                        "recipes__ingredients"
                        "__ingredient__translations"
                    ),
                    (
                        "recipes__ingredients"
                        "__unit"
                    ),
                )
                .get(
                    id=pk,
                    is_active=True,
                )
            )

        except Meal.DoesNotExist:
            return Response(
                {
                    "error": "Meal not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = MealDetailSerializer(
            meal,
            context={
                "request": request,
            },
        )

        return Response(serializer.data)


class MealCategoryListAPIView(APIView):

    def get(self, request):
        categories = (
            MealCategory.objects
            .prefetch_related(
                "translations"
            )
            .order_by("name")
        )

        serializer = MealCategorySerializer(
            categories,
            many=True,
            context={
                "request": request,
            },
        )

        return Response(serializer.data)


class MealByCategoryAPIView(APIView):

    def get(self, request, category):
        meals = (
            Meal.objects
            .filter(
                is_active=True,
                categories__name__iexact=category,
            )
            .prefetch_related(
                "categories",
                "translations",
                "recipes",
                "recipes__ingredients",
                "recipes__ingredients__ingredient",
                "recipes__ingredients__unit",
            )
            .distinct()
            .order_by("name")
        )

        serializer = MealSerializer(
            meals,
            many=True,
            context={
                "request": request,
            },
        )

        return Response(serializer.data)