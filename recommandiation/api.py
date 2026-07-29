from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .services import recommend_meals

from .serializers import (
    MealRecommendationSerializer,
)



class RecommendationAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def get(self, request):

        meals = recommend_meals(
            request.user
        )


        serializer = MealRecommendationSerializer(
            meals,
            many=True
        )


        return Response(
            serializer.data
        )