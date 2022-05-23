from django.shortcuts import render, get_object_or_404
from .models import Wine, Review, Country, Region
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'wine/index.html')

def wines(request):
    wine_list=Wine.objects.all()
    return render(request, 'wine/wines.html', {'wine_list' : wine_list})

def wineview(request, id):
    wines=get_object_or_404(Wine, pk=id)
    return render(request, 'wine/wineview.html', {'wines' : wines})