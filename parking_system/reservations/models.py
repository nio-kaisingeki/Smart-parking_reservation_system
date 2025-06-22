"""Reservation app models placeholder."""

from django.db import models

class ParkingSpot(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    daily_rate = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    user_email = models.EmailField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_email} @ {self.parking_spot}"  
