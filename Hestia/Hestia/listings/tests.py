from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from Hestia.common.models import City
from Hestia.core.validators import validate_image_size
from Hestia.listings.models import Listing
from Hestia.settings import BASE_DIR
from django.core.exceptions import ValidationError

UserModel = get_user_model()


class ValidatorsTests(TestCase):
    def test_validate_image_size__when_file_size_valid__expect_ok(self):
        image = BASE_DIR / 'staticfiles/images/no-image.jpg'
        validate_image_size(image)

    def test_validate_image_size__when_image_size_bigger__expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            image = BASE_DIR / 'staticfiles/images/banner.jpg'
            validate_image_size(image)

        self.assertIsNotNone(context.exception)

    def test_validate_image_size__when_image_size_smaller__expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            image = BASE_DIR / 'staticfiles/images/search.png'
            validate_image_size(image)

        self.assertIsNotNone(context.exception)


class ListingViewsTests(TestCase):
    def test_listings_list_view__when_no_listings__expect_empty_list(self):
        response = self.client.get(reverse('search'))

        return self.assertEqual(0, len(response.context['listings']))

    def test_listing_list_view__when_anonymous_user__username_to_be_anonymous(self):
        response = self.client.get(reverse('search'))

        self.assertEqual('Anonymous', response.context['username'])


