from django.contrib import admin

from Hestia.listings.models import Listing, Photo


# Register your models here.


@admin.register(Listing)
class Listing(admin.ModelAdmin):
    pass


@admin.register(Photo)
class Photo(admin.ModelAdmin):
    pass
