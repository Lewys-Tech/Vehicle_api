from rest_framework import serializers
from vehicle_api.models import Vehicle

class VehicleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    vehicle_type = serializers.CharField(max_length=200)
    vehicle_regNo = serializers.IntegerField()
    vehicle_owner = serializers.CharField()
    
    
    
    def create(self,data):
        return Vehicle.objects.create(**data)