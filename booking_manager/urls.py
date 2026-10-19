from django.urls import path

from booking_manager import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('specialists/', views.specialists, name='specialists'),
    path('bookings/', views.bookings, name='bookings'),
    path('bookings/new_booking', views.new_booking, name='new_booking')
]