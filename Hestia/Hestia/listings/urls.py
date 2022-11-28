from django.urls import path

from Hestia.listings.views import add_listing

urlpatterns = [
    path('add/', add_listing, name='add listing'),
]