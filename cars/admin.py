from django.contrib import admin
from .models import Car
from .models import Car_image
from django import forms
from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Car
# Register your models here.
admin.site.register(Car_image)

class CarForm(forms.ModelForm):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }
    class Meta:
        model = Car
        exclude = []
class CarAdmin(admin.ModelAdmin):
    exclude = []
    form = CarForm
admin.site.register(Car,CarAdmin)
