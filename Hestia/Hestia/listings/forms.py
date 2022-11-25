from django import forms

from Hestia.listings.models import Listing, Photo


class ListingBaseForm(forms.ModelForm):
    class Meta:
        model = Listing
        exclude = ('publication_date', 'user')


class ListingCreateForm(ListingBaseForm):
    pass

