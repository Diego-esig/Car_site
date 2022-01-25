from unittest import TestCase
from shop.views import *
from django.urls import reverse
from django.test import TestCase

class TestViews(TestCase):

    def test_view_home_uses_correct_template(self):
        response = self.client.get(reverse(home))
        self.assertTemplateUsed(response, 'shop/home.html')

    def test_view_ajout_voiture_uses_correct_template(self):
        response= self.client.get(reverse(ajout_voiture))
        self.assertTemplateUsed(response, 'shop/ModelForm.html')

    def test_redirect_in_ajout_voiture_views(self):
