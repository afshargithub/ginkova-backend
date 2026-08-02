from django.urls import path

from .api import (
    DiseaseListAPIView,
    HealthGoalListAPIView,
)


urlpatterns = [
    path(
        "health-goals/",
        HealthGoalListAPIView.as_view(),
        name="health-goals",
    ),

    path(
        "diseases/",
        DiseaseListAPIView.as_view(),
        name="diseases",
    ),
]