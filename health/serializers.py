from rest_framework import serializers
from .models import HealthGoal


class HealthGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthGoal
        fields = [
            "id",
            "name",
            "description",
            "icon",
            "display_order",
        ]