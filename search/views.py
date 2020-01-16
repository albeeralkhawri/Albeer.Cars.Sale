from django.shortcuts import render
from cars.models import Car

# Create your views here.
def do_search(request):
    cars = Car.objects.filter(model__icontains=request.GET['q'])
    return render(request, "carlist.html", {"cars": cars})