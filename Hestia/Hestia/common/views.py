from django.shortcuts import render

from Hestia.common.models import City
from Hestia.listings.models import Listing


# Create your views here.


def index(request):
    price_sum = 0
    counter = 0
    for l in Listing.objects.all():
        price_sum += l.price // l.size
        counter += 1
    avg_price = price_sum // counter
    context = {
        'cities': City.objects.all(),
        'average_price': avg_price,
    }

    return render(request, 'common/index.html', context)
