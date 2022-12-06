from django.contrib import admin

from Hestia.common.models import City


# Register your models here.
@admin.register(City)
class City(admin.ModelAdmin):
    ordering = ('name',)



