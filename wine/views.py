from django.shortcuts import render, get_object_or_404
from .models import Wine, Review, Country, Region
from django.urls import reverse_lazy
from .forms import WineForm, ReviewForm

# Create your views here.
def index(request):
    return render(request, 'wine/index.html')

def wines(request):
    wine_list=Wine.objects.all()
    return render(request, 'wine/wines.html', {'wine_list' : wine_list})

def wineview(request, id):
    wines=get_object_or_404(Wine, pk=id)
    return render(request, 'wine/wineview.html', {'wines' : wines})

def regions(request):
    region_list=Region.objects.all()
    return render(request, 'wine/regions.html', {'region_list' : region_list})

def regionview(request, id):
    regions=get_object_or_404(Region, pk=id)
    return render(request, 'wine/regionview.html', {'regions' : regions})

def reviews(request):
    review_list=Review.objects.all()
    return render(request, 'wine/reviews.html', {'review_list' : review_list})

def reviewview(request, id):
    reviews=get_object_or_404(Review, pk=id)
    return render(request, 'wine/reviewview.html', {'reviews' : reviews})

# form views
def newWine(request):
    form=WineForm

    if request.method=='POST':
        form=WineForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=WineForm()

    else:
        form=WineForm()

    return render(request, 'wine/newwine.html', {'form': form}) 


def newReview(request):
    form=ReviewForm

    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ReviewForm()

    else:
        form=ReviewForm()

    return render(request, 'wine/newreview.html', {'form': form}) 