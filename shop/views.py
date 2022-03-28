from django.shortcuts import render
from django.shortcuts import redirect
from .models import Produit
from .forms import ProduitForm
import json
from django.http import JsonResponse
# Create your views here.

def home(request):
    produits = Produit.objects.all()
    return render(request, 'shop/home.html', {"produits": produits})

# def home()
def ajout_voiture(request):
    form = ProduitForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'shop/ModelForm.html', {'form' : form})

def search_car(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')

        produits = Produit.filter(
            marque__starts_with = search_str) | Produit.filter(
            modele__starts_with = search_str) | Produit.filter(
            description__icontains = search_str) | Produit.filter(
            categorie__starts_with = search_str)

        data = produits.values()

        return JsonResponse(list(data),safe=False)

