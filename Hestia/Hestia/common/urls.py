from django.urls import path

from Hestia.common.views import index

urlpatterns = [
    path('', index, name='index')
]