from django.contrib import admin

from Hestia.news.models import News


# Register your models here.
@admin.register(News)
class News(admin.ModelAdmin):
    pass
