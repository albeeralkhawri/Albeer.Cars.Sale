from django.db import models

# Create your models here.
class Car(models.Model):
    model = models.TextField()
    brand = models.TextField()
    base_price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.model + ' - ' + self.brand

class Car_detail(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    name = models.TextField()
    extra_price = models.DecimalField(max_digits=5, decimal_places=2)
    image1 = models.ImageField(upload_to='images', null=True)
    image2 = models.ImageField(upload_to='images', null=True)
    image3 = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.name