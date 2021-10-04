from django.test import TestCase
from .models import Shortener


class URLTests(TestCase):
    def test_homepage(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code, 200)

class ModelTests(TestCase):
    def setUp(self):
        Shortener.objects.create(long_url="http://google.com", short_url='p2BBUV3')

    def test_correct_shorturl(self):
        """Long links have correct short links"""
        link = Shortener.objects.get(long_url="http://google.com")
        self.assertEqual(link.short_url, 'p2BBUV3')