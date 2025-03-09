# Create your API endpoints here

# from django.http import HttpResponse, JsonResponse
# from .models import Drink
# from .serializers import DrinkSerializer

# def drink_list(request):
#     return HttpResponse("List of drinks")

# def get_drinks(request):
#     # get all the drinks
#     drinks = Drink.objects.all()
#     # serialize them
#     serializer = DrinkSerializer(drinks, many=True)
#     # return them as a JSON response
#     return JsonResponse(serializer.data, safe=False)
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drink_list(request):
    # Get all the drinks
    drinks = Drink.objects.all()
    # Serialize them
    serializer = DrinkSerializer(drinks, many=True)
    # Return them as a JSON response
    return JsonResponse(serializer.data, safe=False)