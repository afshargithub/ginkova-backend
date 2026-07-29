
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def test_meals(request):

    return Response(

        [
            {
                "id": 1,
                "name": "Chicken Salad",
                "price": 3500
            },

            {
                "id": 2,
                "name": "Grilled Fish",
                "price": 4200
            }

        ]

    )