from django.urls import reverse
from django.test import TestCase
from shop.views import *

class TestViews(TestCase):

    def test_view_home_uses_correct_template(self):
        response = self.client.get(reverse(home))
        self.assertTemplateUsed(response, 'shop/home.html')

    def test_view_ajout_voiture_uses_correct_template(self):
        response = self.client.get(reverse(ajout_voiture))
        self.assertTemplateUsed(response, 'shop/ModelForm.html')

    def test_view_ajout_voiture_create_objet_produit(self):
        self.client.post('/ajout_voiture/', data={
            'marque' : 'toyota', 'modele' : 'supra', 'categorie' : 'race',
            'description' : 'is a good race car', 'prix' : 1000.00, 'image' : 'link image'})
        self.assertEqual(Produit.objects.count(),1)
        self.assertEqual(Produit.objects.first().modele, 'supra')

    def test_view_ajout_voiture_missing_field(self):
        self.client.post('/ajout_voiture/', data={
            'modele': 'supra', 'categorie': 'race',
            'description': 'is a good race car', 'prix': 1000.00, 'image': 'link image'})

        self.assertEqual(Produit.objects.count(),0)


    def test_view_ajout_voiture_redirect_to_home(self):

         response = self.client.post('/ajout_voiture/', data={
            'marque' :'toyota','modele': 'supra', 'categorie': 'race',
            'description': 'is a good race car', 'prix': 1000.00, 'image': 'link image'})

         self.assertRedirects(response, '/')


