from common.i18n import (
    normalize_language_code,
)
from common.localization import (
    get_localized_name,
)
from health.models import HealthProfile
from nutrition.services import (
    calculate_meal_nutrition,
)
from restaurants.models import RestaurantMeal

from .models import MealRecommendationRule


REASON_MESSAGES = {
    "en": {
        "goal": "Health goal: {name}",
        "disease": "Disease: {name}",
        "low_calories": "Low calories",
        "high_protein": "High protein",
        "low_fat": "Low fat",
    },

    "fa": {
        "goal": "هدف سلامتی: {name}",
        "disease": "بیماری: {name}",
        "low_calories": "کالری پایین",
        "high_protein": "پروتئین بالا",
        "low_fat": "چربی پایین",
    },

    "hy": {
        "goal": "Առողջական նպատակ՝ {name}",
        "disease": "Հիվանդություն՝ {name}",
        "low_calories":
            "Ցածր կալորիականություն",
        "high_protein":
            "Բարձր սպիտակուցային պարունակություն",
        "low_fat": "Ցածր յուղայնություն",
    },

    "ru": {
        "goal": "Цель здоровья: {name}",
        "disease": "Заболевание: {name}",
        "low_calories": "Низкая калорийность",
        "high_protein":
            "Высокое содержание белка",
        "low_fat":
            "Низкое содержание жира",
    },
}


def get_reason_messages(language_code):
    language = normalize_language_code(
        language_code
    )

    return REASON_MESSAGES.get(
        language,
        REASON_MESSAGES["en"],
    )


def recommend_meals(
    user,
    language_code="en",
):
    """
    Recommendation Engine

    Score:
        Goal        +50
        Disease     +50
        Nutrition   based on rules

    Output:
        Meal
        Score
        Reasons
        Restaurants
    """

    language = normalize_language_code(
        language_code
    )

    reason_messages = get_reason_messages(
        language
    )

    try:
        profile = (
            HealthProfile.objects
            .prefetch_related(
                "goals",
                "goals__translations",
                "diseases",
                "diseases__translations",
            )
            .get(
                user=user,
            )
        )

    except HealthProfile.DoesNotExist:
        return []

    goals = set(
        profile.goals.all()
    )

    diseases = set(
        profile.diseases.all()
    )

    rules = (
        MealRecommendationRule.objects
        .filter(
            meal__is_active=True,
        )
        .select_related(
            "meal",
            "goal",
            "disease",
        )
        .prefetch_related(
            "meal__translations",
            "meal__nutrition_rules",
            "goal__translations",
            "disease__translations",
        )
    )

    recommendations = {}

    for rule in rules:
        score = 0
        reasons = []

        # =========================
        # Goal Matching
        # =========================

        if (
            rule.goal
            and rule.goal in goals
        ):
            score += 50

            localized_goal_name = (
                get_localized_name(
                    rule.goal,
                    language,
                )
            )

            reasons.append(
                reason_messages["goal"].format(
                    name=localized_goal_name,
                )
            )

        # =========================
        # Disease Matching
        # =========================

        if (
            rule.disease
            and rule.disease in diseases
        ):
            score += 50

            localized_disease_name = (
                get_localized_name(
                    rule.disease,
                    language,
                )
            )

            reasons.append(
                reason_messages[
                    "disease"
                ].format(
                    name=localized_disease_name,
                )
            )

        if score == 0:
            continue

        meal_id = rule.meal.id

        if meal_id not in recommendations:
            recommendations[meal_id] = {
                "meal_id": meal_id,

                "meal": get_localized_name(
                    rule.meal,
                    language,
                ),

                "score": score,

                "reason": reasons,

                "restaurants": [],
            }

        else:
            recommendations[
                meal_id
            ]["score"] += score

            recommendations[
                meal_id
            ]["reason"].extend(
                reasons
            )

        # =========================
        # Nutrition Rules
        # =========================

        nutrition_rules = (
            rule.meal
            .nutrition_rules
            .all()
        )

        for nutrition_rule in nutrition_rules:
            nutrition_score = 0

            nutrition = (
                calculate_meal_nutrition(
                    rule.meal
                )
            )

            if (
                nutrition_rule.max_calories
                is not None
                and nutrition["calories"]
                <= nutrition_rule.max_calories
            ):
                nutrition_score += (
                    nutrition_rule.score
                )

                recommendations[
                    meal_id
                ]["reason"].append(
                    reason_messages[
                        "low_calories"
                    ]
                )

            if (
                nutrition_rule.min_protein
                is not None
                and nutrition["protein"]
                >= nutrition_rule.min_protein
            ):
                nutrition_score += (
                    nutrition_rule.score
                )

                recommendations[
                    meal_id
                ]["reason"].append(
                    reason_messages[
                        "high_protein"
                    ]
                )

            if (
                nutrition_rule.max_fat
                is not None
                and nutrition["fat"]
                <= nutrition_rule.max_fat
            ):
                nutrition_score += (
                    nutrition_rule.score
                )

                recommendations[
                    meal_id
                ]["reason"].append(
                    reason_messages[
                        "low_fat"
                    ]
                )

            recommendations[
                meal_id
            ]["score"] += nutrition_score

    # =========================
    # Add Restaurants
    # =========================

    for item in recommendations.values():
        restaurant_meals = (
            RestaurantMeal.objects
            .filter(
                meal_id=item["meal_id"],
                is_available=True,
                restaurant__is_active=True,
            )
            .select_related(
                "restaurant",
            )
            .prefetch_related(
                "restaurant__translations",
            )
        )

        item["restaurants"] = [
            {
                "restaurant_id":
                    restaurant_meal.restaurant.id,

                "restaurant_name":
                    get_localized_name(
                        restaurant_meal.restaurant,
                        language,
                    ),

                "price":
                    restaurant_meal.price,

                "estimated_preparation_time":
                    restaurant_meal
                    .estimated_preparation_time,
            }
            for restaurant_meal
            in restaurant_meals
        ]

    result = list(
        recommendations.values()
    )

    result.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    return result[:10]