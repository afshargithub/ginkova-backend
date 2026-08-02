from rest_framework import generics

from .models import Disease
from .serializers import (
    DiseaseSerializer,
    HealthGoalSerializer,
)
from .services import get_active_health_goals


class HealthGoalListAPIView(
    generics.ListAPIView
):
    serializer_class = HealthGoalSerializer

    def get_queryset(self):
        return (
            get_active_health_goals()
            .prefetch_related(
                "translations",
            )
        )


class DiseaseListAPIView(
    generics.ListAPIView
):
    serializer_class = DiseaseSerializer

    def get_queryset(self):
        return (
            Disease.objects
            .prefetch_related(
                "translations",
            )
            .order_by(
                "name",
            )
        )