# Create your API endpoints here
# serialize them
# return them as a JSON response

from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def get_drinks(request):
    # get all the drinks
    drinks = Drink.objects.all()
