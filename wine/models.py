from django.db import models
from django.contrib.auth.models import User

# Country
class Country(models.Model):
    country_name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.country_name
    
    class Meta:
        db_table='country'


# Region
class Region(models.Model):
    region_name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.region_name
    
    class Meta:
        db_table='region'


# Wine
class Wine(models.Model):
    wine_name = models.CharField(max_length=255)
    wine_type = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING)
    description = models.TextField(null=True, blank=True)
    vintage = models.CharField(max_length=255)

    def __str__(self):
        return self.wine_name
    
    class Meta:
        db_table='wine'


# Review
class Review(models.Model):
    wine = models.ForeignKey(Wine, on_delete=models.DO_NOTHING)
    name = models.ForeignKey(Wine, related_name='review_name', on_delete=models.DO_NOTHING)
    date_entered = models.DateField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    review = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.review
    
    class Meta:
        db_table='review'
