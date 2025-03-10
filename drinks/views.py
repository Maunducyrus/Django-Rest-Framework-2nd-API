# Create your API endpoints here

from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drink_list(request):
    # Get all the drinks
    drinks = Drink.objects.all()
    # Serialize them
    serializer = DrinkSerializer(drinks, many=True)
    # Return them as a JSON response
    return JsonResponse({'drinks': serializer.data})