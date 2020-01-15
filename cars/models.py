from django.db import models

# Create your models here.
class Car(models.Model):
    model = models.TextField()
    brand = models.TextField()
    base_price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.model + ' - ' + self.brand
