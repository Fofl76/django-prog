# guesthouse_booking/urls.py

from django.contrib import admin
from django.urls import path, include
from bookings import views as booking_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', booking_views.index, name='index'),
    path('', include('bookings.urls')),
    path('login/', booking_views.login_view, name='login'),
    path('logout/', booking_views.logout_view, name='logout'),
    path('register/', booking_views.register_view, name='register'),
    path('book_room/<int:room_id>/', booking_views.book_room, name='book_room'),
]
