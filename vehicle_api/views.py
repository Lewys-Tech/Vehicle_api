from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from vehicle_api.models import Vehicle
from vehicle_api.serializer import VehicleSerializer

@api_view(['GET'])
def vehicle_list(request):
    vehicles = Vehicle.objects.all()  # Corrected variable name
    serializer = VehicleSerializer(vehicles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def vehicle_create(request):
    serializer = VehicleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)