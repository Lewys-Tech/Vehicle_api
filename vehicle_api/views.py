from django.shortcuts import render 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from vehicle_api.models import vehicle

# Create your views here.
@api_view (['GET'])
def vehicle_list(requests):
    vehicles = vehicle.objects.all()
    serializer = VehicleSerializer(vehicles, many= True)
    return Response(serializer.data) 