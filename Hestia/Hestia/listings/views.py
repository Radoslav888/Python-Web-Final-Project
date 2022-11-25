from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Hestia.listings.forms import ListingCreateForm
from Hestia.listings.models import Photo, Listing


# Create your views here.

@login_required
def add_listing(request):
    if request.method == 'GET':
        form = ListingCreateForm()
    else:
        form = ListingCreateForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user
            listing.save()
            return redirect('add photos', pk=listing.pk)
    context = {
        'listing_form': form,
    }
    return render(request, 'listings/add-listing.html', context)

@login_required
def add_photos(request, pk):
    listing = Listing.objects.filter(pk=pk).get()
    if request.method == "POST":
        images = request.FILES.getlist('images')
        for image in images:
            Photo.objects.create(image=image, listing=listing)
    images = Photo.objects.filter(listing=listing)
    context = {
        'images': images,
    }
    return render(request, 'listings/add-photo.html', context)