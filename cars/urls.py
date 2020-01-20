from django.conf.urls import url, include
from .views import cars
from .views import details

urlpatterns = [
    url(r'^$', cars, name='cars'),
    url(r'^details/([0-9]+)', details, name='details')
]
