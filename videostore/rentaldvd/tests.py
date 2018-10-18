from django.test import TestCase
from .models import Dvd


class DvdTestCase(TestCase):
    def setUp(self):
        Dvd.objects.create(title="lion")
        Dvd.objects.create(title="cat")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Dvd.objects.get(title="lion")
        cat = Dvd.objects.get(title="cat")
        self.assertEqual(lion.get_absolute_url(), '/rentaldvd/dvd/1/')
        self.assertEqual(cat.get_absolute_url(), '/rentaldvd/dvd/2/')
