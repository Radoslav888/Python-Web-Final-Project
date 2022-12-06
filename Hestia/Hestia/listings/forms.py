from django import forms

from Hestia.listings.models import Listing, Photo


class ListingBaseForm(forms.ModelForm):
    class Meta:
        model = Listing
        exclude = ('publication_date', 'user')


class ListingCreateForm(ListingBaseForm):
    class Meta:
        model = Listing
        exclude = ('publication_date', 'user', 'slug')
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'cols': 40,
                    'rows': 10,
                },
            ),
        }


class PhotoForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Photo
        fields = ('image', )

