from django.shortcuts import render

from Hestia.common.models import City
from Hestia.listings.models import Listing


# Create your views here.

def get_avg_price_per_m2():
    price_sum = 0
    counter = 0
    for l in Listing.objects.all():
        price_sum += l.price // l.size
        counter += 1
    if counter > 0:
        avg_price = price_sum // counter
        return avg_price
    return 0


def index(request):
    cities = City.objects.all().order_by('name')
    avg_price = get_avg_price_per_m2()
    context = {
        'cities': cities,
        'average_price': avg_price,
        'listings_count': Listing.objects.count()
    }

    return render(request, 'common/index.html', context)
