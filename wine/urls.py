from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('wine/', views.wines, name='wines'),
   path('wineview/<int:id>', views.wineview, name='wine_details'),
   path('regions/', views.regions, name='regions'),
   path('regionview/<int:id>', views.regionview, name='region_details'),
   path('reviews/', views.reviews, name='reviews'),
   path('reviewview/<int:id>', views.reviewview, name='review_details'),
   path('newwine/', views.newWine, name='new_wine'),
   path('newreview/', views.newReview, name='new_review'),
 
   
   
]