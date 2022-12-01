from django.shortcuts import render

from Hestia.common.models import City


# Create your views here.


def index(request):
    context = {
        'cities': City.objects.all()
    }

    return render(request, 'common/index.html', context)
