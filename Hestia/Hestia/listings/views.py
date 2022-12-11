from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, redirect


from Hestia.common.models import City
from Hestia.listings.forms import ListingCreateForm, PhotoForm, SearchListingForm
from Hestia.listings.models import Photo, Listing

UserModel = get_user_model()

# Create your views here.


@login_required
def add_listing(request):
    if request.method == 'POST':
        ListingForm = ListingCreateForm(request.POST)

        if ListingForm.is_valid():
            listing_form = ListingForm.save(commit=False)
            listing_form.user = request.user
            listing_form.save()

            return redirect('edit listing photos', slug=listing_form.slug)
        else:
            print(ListingForm.errors)
    else:
        ListingForm = ListingCreateForm()
    context = {
        'listing_form': ListingForm,
    }
    return render(request, 'listings/add-listing.html', context)


@login_required
def edit_listing(request, slug):
    listing = Listing.objects.filter(slug=slug).get()
    if request.method == 'POST':
        listing_form = ListingCreateForm(request.POST, instance=listing)

        if listing_form.is_valid():
            listing_form = listing_form.save(commit=False)
            listing_form.user = request.user
            listing_form.save()

            return redirect('listing details', slug=slug)
        else:
            print(listing_form.errors,)
    else:
        listing_form = ListingCreateForm(instance=listing)

    context = {
        'listing_form': listing_form,
        'listing': listing,

    }
    return render(request, 'listings/edit-listing.html', context)


@login_required
def edit_listing_photos(request, slug):
    listing = Listing.objects.filter(slug=slug).get()
    photos = listing.photo_set.all()
    extra_photos_count = 5 - len(photos)
    context = {
        'photos': photos,
        'listing': listing,
        'extra': range(extra_photos_count),

    }
    return render(request, 'listings/edit-listing-photos.html', context)


def city_listings(request, slug):
    city = City.objects.filter(slug=slug).get()
    listings = city.listing_set.order_by('price')
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
        owner = UserModel.objects.filter(pk=self.object.user_id).get()
        context['is_owner'] = self.request.user == owner
        context['user_profile'] = owner
        return context


class DeleteListingView(views.DeleteView):
    template_name = 'listings/listing-delete.html'
    model = Listing
    success_url = reverse_lazy('index')


def search(request):
    search_form = SearchListingForm(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['listing_name']
    listings = Listing.objects.all()
    if search_pattern:
        listings = listings.filter(name__icontains=search_pattern)
    page = request.GET.get('page', 1)
    paginator = Paginator(listings, 4)

    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        listings = paginator.page(1)
    except EmptyPage:
        listings = paginator.page(paginator.num_pages)

    context = {
        'listings': listings,
        'search_form': search_form,
    }

    return render(request, 'listings/search-listing.html', context)


@login_required
def add_photo(request, slug):
    listing = Listing.objects.filter(slug=slug).get()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.listing_id = listing.id
            photo.save()
            return redirect('edit listing photos', slug=slug)
    else:
        form = PhotoForm()
    context = {
        'form': form,
        'slug': slug,
    }
    return render(request, 'listings/add-photo.html', context)


class EditPhotoView(views.UpdateView):
    template_name = 'listings/edit-photo.html'
    model = Photo

    def get_success_url(self, **kwargs):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class DeletePhotoView(views.DeleteView):
    template_name = 'listings/delete-photo.html'
    model = Photo

    def get_success_url(self, **kwargs):
        return reverse_lazy('edit listing photos', kwargs={
            'slug': self.object.listing.slug,
        })