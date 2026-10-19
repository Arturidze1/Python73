from django.http import HttpResponse
from django.shortcuts import render

services_list = [
    {"id": 1, "name": "Haircut", "duration": 60, "price": 30, "category": "Hair"},
    {"id": 2, "name": "Beard Trim", "duration": 30, "price": 15, "category": "Hair"},
    {"id": 3, "name": "Manicure", "duration": 45, "price": 25, "category": "Nails"},
    {"id": 4, "name": "Massage", "duration": 90, "price": 50, "category": "Wellness"},
    {"id": 5, "name": "Consultation", "duration": 30, "price": 20, "category": "Other"}
]

specialists_list = [
    {"id": 1, "name": "Alice Brown", "speciality": "Hair Stylist", "experience": 5},
    {"id": 2, "name": "Bob Smith", "speciality": "Barber", "experience": 7},
    {"id": 3, "name": "Diana Green", "speciality": "Nail Artist", "experience": 3},
    {"id": 4, "name": "Charlie White", "speciality": "Massage Therapist", "experience": 6}
]

bookings_list = [
    {"client": "John", "service": "Haircut", "date": "20.09.2026", "time": "12:00", "status": "confirmed"},
    {"client": "Anna", "service": "Manicure", "date": "20.09.2026", "time": "14:30", "status": "pending"},
    {"client": "Mike", "service": "Massage", "date": "21.09.2026", "time": "10:00", "status": "confirmed"},
    {"client": "Kate", "service": "Consultation", "date": "22.09.2026", "time": "16:00", "status": "cancelled"}
]

def index(request):
    return HttpResponse("Hello, world. You're at the booking_manager index.")

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html', context={'services' : services_list})

def specialists(request):
    return render(request, 'specialists.html', context={'specialists' : specialists_list})

def bookings(request):
    return render(request, 'bookings.html', context={'bookings' : bookings_list})

def new_booking(request):
    return render(request, 'new_booking.html')
