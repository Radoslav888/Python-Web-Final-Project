from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Hestia import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin site'),
    path('', include('Hestia.common.urls')),
    path('accounts/', include('Hestia.accounts.urls')),
    path('listings/', include('Hestia.listings.urls')),
    path('news/', include('Hestia.news.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
