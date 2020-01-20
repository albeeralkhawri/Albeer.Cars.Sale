from django.shortcuts import render
from .models import Car
from .models import Car_image
# Create your views here.
def cars(request):
    cars = Car.objects.all()
    return render(request, "carlist.html", {"cars": cars})
    

def details(request, id):
    details = Car_image.objects.filter(car_id = id)
    car= Car.objects.get(id=id)
    return render(request, "cardetails.html", {'details': details, 'car': car})