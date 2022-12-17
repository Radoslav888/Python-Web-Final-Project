from django.urls import path

from Hestia.listings.views import add_listing, city_listings, ListingDetailsView, search, edit_listing, \
    edit_listing_photos, DeleteListingView, DeletePhotoView, add_photo

urlpatterns = [
    path('add/', add_listing, name='add listing'),
    path('edit/<str:slug>', edit_listing, name='edit listing'),
    path('delete/<str:slug>', DeleteListingView.as_view(), name='delete listing'),
    path('photo/delete/<int:pk>', DeletePhotoView.as_view(), name='delete photo'),
    path('photo/add/<str:slug>', add_photo, name='add photo'),
    path('edit-listing-photos/<str:slug>', edit_listing_photos, name='edit listing photos'),
    path('city/<str:slug>/', city_listings, name='city listings'),
    path('search/', search, name='search'),
    path('<str:slug>/', ListingDetailsView.as_view(), name='listing details'),

]