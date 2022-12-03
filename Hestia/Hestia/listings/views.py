from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import generic as views
from django.contrib.auth.decorators import login_required
from django.core import exceptions
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from Hestia.common.models import City
from Hestia.listings.forms import ListingCreateForm, PhotoForm
from Hestia.listings.models import Photo, Listing

UserModel = get_user_model()

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
                    photo = Photo(listing=listing_form, image=image)
                    photo.save()
            return redirect('index')
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


def city_listings(request, slug):
    city = City.objects.filter(slug=slug).get()
    listings = city.listing_set.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(listings, 3)

    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        listings = paginator.page(1)
    except EmptyPage:
        listings = paginator.page(paginator.num_pages)

    context = {
        'listings': listings,
        'city': city,
    }
    return render(request, 'listings/city-listing.html', context)


class ListingDetailsView(views.DetailView):
    template_name = 'listings/listing-details.html'
    model = Listing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        context['user_profile'] = UserModel.objects.filter(pk=self.object.user_id).get()
        return context
