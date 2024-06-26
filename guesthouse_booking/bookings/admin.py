# bookings/admin.py

from django.contrib import admin
from .models import Guest, Room, Booking, Payment, Review, Amenity

class AmenityInline(admin.TabularInline):
    model = Room.amenities.through  

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type', 'price_per_night', 'max_occupancy')
    list_filter = ('room_type',)
    search_fields = ('room_number', 'room_type')
    inlines = [AmenityInline]

    @admin.display(description='Amenities')
    def display_amenities(self, obj):
        return ", ".join([amenity.name for amenity in obj.amenities.all()])

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('guest', 'room', 'check_in', 'check_out', 'total_price')
    list_filter = ('check_in', 'check_out')
    date_hierarchy = 'check_in'
    raw_id_fields = ('guest', 'room')
    search_fields = ('guest__first_name', 'guest__last_name', 'room__room_number')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking', 'amount', 'payment_date')
    list_filter = ('payment_date',)
    date_hierarchy = 'payment_date'
    search_fields = ('booking__guest__first_name', 'booking__guest__last_name')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('room', 'rating', 'comment', 'review_date')
    list_filter = ('rating', 'review_date')
    search_fields = ('guest__first_name', 'guest__last_name', 'room__room_number')

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name',)
