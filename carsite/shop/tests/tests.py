from django.test import TestCase
from carsite.shop.models import Produit


class TestModelsProduit(TestCase):

    def test_ajout_et_recuperation_produits(self):
        produit_1 = Produit()
        produit_1.marque = 'Toyota'
        produit_1.save()

        produits_creer = Produit.objects.all()
        self.assertEqual(Produit.objects.count(), 1)
