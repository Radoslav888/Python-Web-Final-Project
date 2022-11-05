from django.urls import path

from bulgarian_real_estate.common.views import index

urlpatterns = [
    path('', index, name='index'),
]