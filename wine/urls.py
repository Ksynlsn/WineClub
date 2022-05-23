from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('wine/', views.wines, name='wines'),
   path('wineview/<int:id>', views.wineview, name='details'),
   
]