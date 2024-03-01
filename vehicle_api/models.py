from django.db import models

class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=200)
    vehicle_regNo = models.IntegerField()
    vehicle_owner = models.CharField()
    
    
    
    def __str__(self):
        return self.vehicle_type
    
