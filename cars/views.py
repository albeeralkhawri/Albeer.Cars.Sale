from django.shortcuts import render
from .models import Car

# Create your views here.
def cars(request):
    cars = Car.objects.all()
    return render(request, "carlist.html", {"cars": cars})