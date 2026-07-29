from rest_framework import serializers



class RestaurantRecommendationSerializer(serializers.Serializer):

    restaurant_id = serializers.IntegerField()


    restaurant_name = serializers.CharField()


    price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2
    )


    estimated_preparation_time = serializers.IntegerField()





class MealRecommendationSerializer(serializers.Serializer):

    meal_id = serializers.IntegerField()


    meal = serializers.CharField()


    score = serializers.IntegerField()


    reason = serializers.ListField(
        child=serializers.CharField()
    )


    restaurants = RestaurantRecommendationSerializer(
        many=True
    )