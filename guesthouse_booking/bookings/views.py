# bookings/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Room
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Review, Room
from .forms import ReviewForm

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

def book_room(request, room_id):
    # Реализуйте вашу логику бронирования здесь
    return redirect('index')

@login_required
def add_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.guest = request.user
            review.review_date = timezone.now()
            review.save()
            return redirect('index')
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})