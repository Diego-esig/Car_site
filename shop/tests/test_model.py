from django.core.exceptions import ValidationError
from django.test import TestCase
from shop.models import *


class TestModelsProduit(TestCase):

    def test_adding_retrieving_models_object(self):
        produit_first = Produit()
        produit_first.marque = 'Toyota'
        produit_first.modele = 'supra'
        produit_first.categorie = 'race'
        produit_first.description = 'Toyota supra is a good race car'
        produit_first.prix = 100000.00
        produit_first.image = 'image web link'

        produit_sec = Produit()
        produit_sec.marque = 'Nissan'
        produit_sec.modele = 'skyline'
        produit_sec.categorie = 'race'
        produit_sec.description = 'Godzilla forever'
        produit_sec.prix = 75000.00
        produit_sec.image = 'image web link'

        produit_first.save()
        produit_sec.save()

        self.assertEqual(Produit.objects.count(), 2)

    def test_hasattr_modele(self):
        self.assertTrue(hasattr(Produit(), 'modele'))

    def test_attribute_modele_saved(self):
        a = Produit.objects.create(marque='toyota', modele = 'supra', categorie = 'race',
                               description = 'Toyota supra is a good race car',prix = 100000.00,
                               image = 'image web link')
        self.assertEqual(a.modele, 'supra')

    def test_attr_modele_is_too_long(self):
        a = Produit.objects.create(marque='toyota', modele='a' * 1000, categorie='race',
                                   description='Toyota supra is a good race car', prix=100000.00,
                                   image='image web link')
        with self.assertRaises(ValidationError):
            a.full_clean()
