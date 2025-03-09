# Create your API endpoints here
# get all the drinks
# serialize them
# return them as a JSON response

from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer