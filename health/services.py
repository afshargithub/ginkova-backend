from .models import HealthGoal

def get_active_health_goals():
    return (
        HealthGoal.objects
        .filter(is_active=True)
        .order_by("display_order")
    )