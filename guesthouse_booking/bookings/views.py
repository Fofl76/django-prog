# bookings/views.py
from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Room
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Review, Room
from .forms import ReviewForm
from .forms import RoomForm

def index(request):
    rooms = Room.objects.all()
    return render(request, 'bookings/index.html', {'rooms': rooms})

def book_room(request, room_id):
    room = Room.objects.get(id=room_id)
    return render(request, 'bookings/book_room.html', {'room': room})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Неверные логин или пароль')
    return redirect('index')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Пользователь с таким логином уже существует')
    return redirect('index')

def logout_view(request):
    logout(request)
    return redirect('index')
    
def index(request):
    rooms = Room.objects.all()
    return render(request, 'bookings/index.html', {'rooms': rooms})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'bookings/register.html', {'form': form})

@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']
            total_price = room.price_per_night * (check_out - check_in).days
            booking = Booking.objects.create(
                guest=request.user.guest,  
                room=room,
                check_in=check_in,
                check_out=check_out,
                total_price=total_price
            )
            booking.save()
            return redirect('index')  
    else:
        form = BookingForm(initial={'room': room.name})
    return render(request, 'bookings/book_room.html', {'room': room, 'form': form})

@login_required
def review_list(request):
    reviews = Review.objects.all()
    rooms = Room.objects.all()
    return render(request, 'bookings/review_list.html', {'reviews': reviews, 'rooms': rooms})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'bookings/add_review.html', {'form': form})

@login_required
def add_room(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = RoomForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = RoomForm()
        return render(request, 'bookings/add_room.html', {'form': form})
    else:
        return redirect('index')

@login_required
def edit_room(request, room_id):
    if request.user.is_superuser:
        room = get_object_or_404(Room, id=room_id)
        if request.method == 'POST':
            form = RoomForm(request.POST, request.FILES, instance=room)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = RoomForm(instance=room)
        return render(request, 'bookings/edit_room.html', {'form': form, 'room': room})
    else:
        return redirect('index')