from django.shortcuts import render
from .models import Wine, Review, Country, Region

# Create your views here.
def index(request):
    return render(request, 'wine/index.html')

def wines(request):
    wine_list=Wine.objects.all()
    return render(request, 'wine/wines.html', {'wine_list' : wine_list})