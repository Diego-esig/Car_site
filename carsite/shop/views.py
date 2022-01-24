from django.shortcuts import render
from django.shortcuts import redirect
from .models import Produit
from .forms import ProduitForm


# Create your views here.

def home(request):
    produits = Produit.objects.all()
    return render(request, 'shop/home.html', {"produits": produits})

# def home()
def ajout_voiture(request):
    form = ProduitForm()
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        context = {'form': form}
        return render(request, 'shop/ModelForm.html', context)


