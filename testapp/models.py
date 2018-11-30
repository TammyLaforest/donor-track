from django.db import models

#models.py
class VehicleBrand(models.Model):
    description = models.CharField(max_length=100)
    code = models.SlugField(primary_key=True)

class VehicleModel(models.Model):
    description = models.CharField(max_length=100)
    code = models.SlugField(primary_key=True)
    brand = models.ForeignKey(VehicleBrand, on_delete=models.CASCADE)
