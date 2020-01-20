from django.shortcuts import render
from .models import Car
from .models import Car_detail
# Create your views here.
def cars(request):
    cars = Car.objects.all()
    return render(request, "carlist.html", {"cars": cars})
    

def details(request):
    details = Car_detail.objects.all()
    return render(request, "cardetails.html", {"details": details})