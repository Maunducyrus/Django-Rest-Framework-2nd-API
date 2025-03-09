# Create your API endpoints here

from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def get_drinks(request):
    # get all the drinks
    drinks = Drink.objects.all()
    # serialize them
    serializer = DrinkSerializer(drinks, many=True)
    # return them as a JSON response
    return JsonResponse(serializer.data)
