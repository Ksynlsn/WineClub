from django.test import TestCase
from django.contrib.auth.models import User
from .models import Country, Region, Wine, Review
import datetime
from .forms import WineForm, ReviewForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class WineTest(TestCase):
    def setUp(self):
        self.name=Wine(wine_name='Example Name')
        self.type=Wine(wine_type='Cabernet')
        self.vintage=Wine(vintage='1989') 

    def test_string(self):
        self.assertEqual(str(self.name), 'Example Name')

    def test_tablename(self):
        self.assertEqual(str(Wine._meta.db_table), 'wine')


class ReviewTest(TestCase):
    def setUp(self):
        self.review=Review(review='Example Review Here')
        self.user=User(username='exampleUser')
        self.date=Review(date_entered=datetime.date(2021,4,13))
        self.name=Wine(wine_name='Example Name')

    def test_string(self):
         self.assertEqual(str(self.review), 'Example Review Here')

    def test_tablename(self):
        self.assertEqual(str(Review._meta.db_table), 'review')


class CountryTest(TestCase):
    def setUp(self):
        self.country=Country(country_name='Italy', description='This is a description')

    def test_string(self):
        self.assertEqual(str(self.country), 'Italy')

    def test_tablename(self):
        self.assertEqual(str(Country._meta.db_table), 'country')


class RegionTest(TestCase):
    def setUp(self):
        self.region=Region(region_name='Burgundy', description='This is a description')
        self.country=Country(country_name='Italy')

    def test_string(self):
        self.assertEqual(str(self.region), 'Burgundy')

    def test_tablename(self):
        self.assertEqual(str(Region._meta.db_table), 'region')


# form tests
class NewWineForm(TestCase):
    def test_wineForm(self):
        data={
            'wine_name': 'Vouvray', 
            'wine_type': 'Chenin Blanc', 
            'country': 'France', 
            'region': 'Loire Valley', 
            'vintage': '03-22-22'
            }
        form=WineForm (data)
        self.assertTrue(form.is_valid)


class NewReviewForm(TestCase):
    def test_reviewForm(self):
        data={
            'wine': 'Vouvray', 
            'wine': 'Vouray', 
            'date_entered': '03-22-22',
            'user': 'exampleUser2', 
            'review': 'This is an example review'
            }
        form=ReviewForm (data)
        self.assertTrue(form.is_valid)



