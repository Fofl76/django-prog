# bookings/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Amenity(models.Model):
    name = models.CharField(max_length=100)

class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    max_occupancy = models.IntegerField()
    amenities = models.ManyToManyField('Amenity', blank=True)

class Guest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateField()

class Review(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE, editable=True)
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField(default=timezone.now)  

    def __str__(self):
        return f"Review {self.id} - {self.room}"
