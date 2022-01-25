from django.urls import resolve
from django.urls import reverse
from django.test import TestCase
from shop.views import home, ajout_voiture

class TestUrl(TestCase):




    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_ajout_voiture_url_resolves_to_ajout_voiture_view(self):
        found = resolve('/ajout_voiture/')
        self.assertEqual(found.func, ajout_voiture)


    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/ajout_voiture/')
        self.assertEqual(response.status_code, 200)


    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('ajout_voiture'))
        self.assertEqual(response.status_code, 200)