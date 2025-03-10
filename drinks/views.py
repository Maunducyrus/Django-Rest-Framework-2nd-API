# Create your API endpoints here
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Other api endpoint methods 

@api_view(['GET', 'POST'])
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is not valid, return an error message
        return JsonResponse(serializer.errors, status=400)
    
    # drink_detail function
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id): 

    try: 
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Check if the request method is GET
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DrinkSerializer(Drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)       
