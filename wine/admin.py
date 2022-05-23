from django.contrib import admin
from .models import Wine, Region, Country, Review

# Register your models here.
admin.site.register(Wine)
admin.site.register(Region)
admin.site.register(Country)
admin.site.register(Review)