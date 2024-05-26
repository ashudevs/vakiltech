# webscraper/urls.py
from django.urls import path
from .views import scrape_data

urlpatterns = [
    path('scrape_data/', scrape_data, name='scrape_data'),
]
