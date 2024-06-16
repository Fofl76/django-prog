from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import add_room, edit_room

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='bookings/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('book_room/<int:room_id>/', views.book_room, name='book_room'),
    path('add_review/', views.add_review, name='add_review'),
    path('reviews/', views.review_list, name='review_list'),
    path('add_room/', views.add_room, name='add_room'),  
    path('edit_room/<int:pk>/', views.edit_room, name='edit_room'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
