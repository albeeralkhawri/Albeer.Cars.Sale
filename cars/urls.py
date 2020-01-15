from django.conf.urls import url, include
from .views import cars


urlpatterns = [
    url(r'^$', cars, name='cars')
]