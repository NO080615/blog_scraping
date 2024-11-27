from django.urls import path
from .views import index, scraping

urlpatterns = [
    path("", index, name="index"),
    path("scraping/", scraping, name="scraping"),
]