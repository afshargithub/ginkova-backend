from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from common.i18n import get_request_language

from .serializers import (
    MealRecommendationSerializer,
)
from .services import recommend_meals


class RecommendationAPIView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        language = get_request_language(
            request
        )

        meals = recommend_meals(
            request.user,
            language_code=language,
        )

        serializer = (
            MealRecommendationSerializer(
                meals,
                many=True,
            )
        )

        return Response(
            serializer.data
        )