from django.urls import path

from .api import HealthGoalListAPIView

urlpatterns = [

    path(
        "health-goals/",
        HealthGoalListAPIView.as_view(),
        name="health-goals",
    ),

]