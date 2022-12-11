from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from Hestia.listings.models import Listing, Photo


# Register your models here.


@admin.register(Listing)
class Listing(admin.ModelAdmin):
    list_display = ('name', 'price', 'location', )
    list_filter = ('location', 'user')


@admin.register(Photo)
class Photo(admin.ModelAdmin):
    list_filter = ('listing',)
