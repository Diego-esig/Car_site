from django.shortcuts import render

from .models import Produit


def index(request):
   produits = Produit.objects.all()
   return render(request, "shop/index.html",{"produits" : produits})

# Create your views here.
