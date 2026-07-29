from .models import (
    MealRecommendationRule,
    NutritionRule,
)


from health.models import HealthProfile

from nutrition.services import calculate_meal_nutrition

from restaurants.models import RestaurantMeal





def recommend_meals(user):

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



    try:

        profile = HealthProfile.objects.get(
            user=user
        )


    except HealthProfile.DoesNotExist:

        return []



    goals = set(
        profile.goals.all()
    )


    diseases = set(
        profile.diseases.all()
    )



    rules = MealRecommendationRule.objects.filter(
        meal__is_active=True
    ).select_related(
        "meal",
        "goal",
        "disease"
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

            reasons.append(
                f"Goal: {rule.goal.name}"
            )



        # =========================
        # Disease Matching
        # =========================

        if (
            rule.disease
            and rule.disease in diseases
        ):

            score += 50

            reasons.append(
                f"Disease: {rule.disease.name}"
            )



        if score == 0:

            continue



        meal_id = rule.meal.id



        if meal_id not in recommendations:


            recommendations[meal_id] = {


                "meal_id":
                    meal_id,


                "meal":
                    rule.meal.name,


                "score":
                    score,


                "reason":
                    reasons,


                "restaurants":
                    []

            }


        else:


            recommendations[meal_id]["score"] += score


            recommendations[meal_id]["reason"].extend(
                reasons
            )



        # =========================
        # Nutrition Rules
        # =========================

        nutrition_rules = NutritionRule.objects.filter(
            meal=rule.meal
        )


        for nutrition_rule in nutrition_rules:


            nutrition_score = 0


            nutrition = calculate_meal_nutrition(
                rule.meal
            )



            if (
                nutrition_rule.max_calories
                and
                nutrition["calories"]
                <= nutrition_rule.max_calories
            ):

                nutrition_score += nutrition_rule.score

                recommendations[meal_id]["reason"].append(
                    "Low calories"
                )



            if (
                nutrition_rule.min_protein
                and
                nutrition["protein"]
                >= nutrition_rule.min_protein
            ):

                nutrition_score += nutrition_rule.score

                recommendations[meal_id]["reason"].append(
                    "High protein"
                )



            if (
                nutrition_rule.max_fat
                and
                nutrition["fat"]
                <= nutrition_rule.max_fat
            ):

                nutrition_score += nutrition_rule.score

                recommendations[meal_id]["reason"].append(
                    "Low fat"
                )



            recommendations[meal_id]["score"] += nutrition_score





    # =====================================
    # اضافه کردن Restaurant ها
    # =====================================


    for item in recommendations.values():


        restaurant_meals = RestaurantMeal.objects.filter(

            meal_id=item["meal_id"],

            is_available=True,

            restaurant__is_active=True

        ).select_related(
            "restaurant"
        )



        item["restaurants"] = [


            {

                "restaurant_id":
                    rm.restaurant.id,


                "restaurant_name":
                    rm.restaurant.name,


                "price":
                    rm.price,


                "estimated_preparation_time":
                    rm.estimated_preparation_time

            }


            for rm in restaurant_meals

        ]





    result = list(
        recommendations.values()
    )



    result.sort(

        key=lambda x: x["score"],

        reverse=True

    )



    return result[:10]