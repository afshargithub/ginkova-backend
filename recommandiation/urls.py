from django.urls import path

from .api import RecommendationAPIView


urlpatterns = [

    path('', RecommendationAPIView.as_view(), name='recommendations'),

]