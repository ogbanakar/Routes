from rest_framework.decorators import api_view
from rest_framework.response import Response

BUS_CAPACITY = 45
COMPANY_COORDINATES = [76.66501949986178, 12.136039536554538]

@api_view(['POST'])
def calculate_routes(request):
    # Get the coordinates from the request
    coordinates = request.data.get('coordinates', [])

    routes = []
    for i in range(0, len(coordinates), BUS_CAPACITY):
        # Each route starts from the employee location and ends at the company
        route = [coordinates[j] for j in range(i, min(i + BUS_CAPACITY, len(coordinates)))]
        route.append(COMPANY_COORDINATES)
        routes.append(route)

    return Response({"routes": routes})
