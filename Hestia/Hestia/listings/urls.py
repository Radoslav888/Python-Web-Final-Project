from django.urls import path

from Hestia.listings.views import add_listing, add_photos

urlpatterns = [
    path('add/', add_listing, name='add listing'),
    path('add_photos/<int:pk>', add_photos, name='add photos'),
]