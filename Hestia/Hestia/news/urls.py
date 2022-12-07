from django.urls import path

from Hestia.news.views import ListNewsView, DetailsNewsView, news_listings

urlpatterns = [
    path('', news_listings, name='list news'),
    path('<str:slug>', DetailsNewsView.as_view(), name='details news'),
]