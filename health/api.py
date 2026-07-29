from rest_framework import generics

from .serializers import HealthGoalSerializer
from .services import get_active_health_goals


class HealthGoalListAPIView(generics.ListAPIView):

    serializer_class = HealthGoalSerializer

    def get_queryset(self):
        return get_active_health_goals()