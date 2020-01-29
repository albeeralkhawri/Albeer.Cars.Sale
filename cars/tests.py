from django.test import TestCase
from .models import Car

# Create your tests here.
class CarTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Car model
    """

    def test_str(self):
        test_name = Car(model='A cars', base_price=10, engine_size=10, year=2020)
        test_name.save()
        self.assertEqual(test_name.model, 'A cars')