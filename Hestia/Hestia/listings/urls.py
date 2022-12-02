from django.urls import path

from Hestia.listings.views import add_listing, city_listings, ListingDetailsView

urlpatterns = [
    path('add/', add_listing, name='add listing'),
    path('<str:slug>/', ListingDetailsView.as_view(), name='listing details'),
    path('city/<str:slug>/', city_listings, name='city listings'),
]