# Create your API endpoints here
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view

# Other api endpoint methods 

@api_view('GET', 'POST')
# GET method
def drink_list(request):

    # Check if the request method is GET
    if request.method == 'GET':
        # Get all the drinks
        drinks = Drink.objects.all()
        # Serialize them
        serializer = DrinkSerializer(drinks, many=True)
        # Return them as a JSON response
        return JsonResponse({'drinks': serializer.data})
    
    # Check if the request method is POST
    if request.method == 'POST':
        # Serialize the data
        serializer = DrinkSerializer(data=request.data)
        # Check if the data is valid
        if serializer.is_valid():
            # Save the data
            serializer.save()
            # Return the data as a JSON response
            return JsonResponse(serializer.data, status=201)
        # If the data is not valid, return an error message
        return JsonResponse(serializer.errors, status=400)
