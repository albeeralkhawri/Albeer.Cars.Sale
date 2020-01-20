from django.contrib import admin
from .models import Car
from .models import Car_detail

# Register your models here.
admin.site.register(Car),
admin.site.register(Car_detail)
