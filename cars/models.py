from django.db import models

# Create your models here.
class Car(models.Model):
    model = models.TextField()
    brand = models.TextField()
    base_price = models.DecimalField(max_digits=12, decimal_places=2)
    year = models.IntegerField()
    fuel_type = models.TextField()
    body_type = models.TextField()
    colour = models.TextField()
    engine_size = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.model + ' - ' + self.brand

class Car_image(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images', null=True)
    

    def __str__(self):
        return self.car.model + ': ' + str(self.id)