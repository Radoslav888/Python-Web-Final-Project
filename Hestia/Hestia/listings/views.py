from django.contrib.auth.decorators import login_required
from django.core import exceptions
from django.forms import modelformset_factory
from django.shortcuts import render, redirect

from Hestia.listings.forms import ListingCreateForm, PhotoForm
from Hestia.listings.models import Photo, Listing


# Create your views here.

@login_required
def add_listing(request):
    ImageFormSet = modelformset_factory(Photo,
                                        form=PhotoForm, extra=5)
    if request.method == 'POST':
        ListingForm = ListingCreateForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Photo.objects.none())

        if ListingForm.is_valid() and formset.is_valid():
            listing_form = ListingForm.save(commit=False)
            listing_form.user = request.user
            listing_form.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = Photo(post=listing_form, image=image)
                    photo.save()
            redirect('index')
        else:
            print(ListingForm.errors, formset.errors)
    else:
        ListingForm = ListingCreateForm()
        formset = ImageFormSet(queryset=Photo.objects.none())
    context = {
        'listing_form': ListingForm,
        'formset': formset,
    }
    return render(request, 'listings/add-listing.html', context)

