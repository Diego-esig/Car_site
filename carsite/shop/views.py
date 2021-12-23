from django.shortcuts import render
from .models import Produit


# Create your views here.


def index(request):
    produits = Produit.objects.all()
    return render(request, "shop/index.html", {"produits": produits})


def home(request):
    produits = Produit.objects.all()
    return render(request, 'shop/home.html', {"produits": produits})
