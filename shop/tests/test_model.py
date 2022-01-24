from django.core.exceptions import ValidationError
from django.test import TestCase
from shop.models import *


class TestModelsProduit(TestCase):

    def test_adding_retrieving_models_object(self):
        produit_first = Produit()
        produit_first.marque = 'Toyota'
        produit_first.save()

        self.assertEqual(Produit.objects.count(), 1)

    def test_hasattr_modele(self):
        self.assertTrue(hasattr(Produit(), 'modele'))

    def test_attribute_modele_saved(self):
        Produit.objects.create(modele = 'supra')
        self.assertEqual(Produit.modele, 'supra')

    # def test_empty_modele_should_be_accepted(self):
    #     a = Produit(marque='toyota', modele=None)
    #     try:
    #         a.full_clean()
    #     except ValidationError:
    #         self.fail("modele should accept blank values.")