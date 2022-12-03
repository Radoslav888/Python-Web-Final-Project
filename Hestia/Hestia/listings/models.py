from enum import Enum

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

from Hestia.common.models import City
from Hestia.core.validators import validate_file_less_than_5mb, validate_image_size

UserModel = get_user_model()


class ChoicesEnumMixin(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class Type(ChoicesEnumMixin):
    apartment = 'Apartment'
    house = 'House'
    field = 'Field'
    business = 'Business'


class Listing(models.Model):
    MIN_NAME_LENGTH = 5
    MAX_NAME_LENGTH = 50

    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 600

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_NAME_LENGTH),
        ),
        null=False,
        blank=False,
        verbose_name='Listing name'
    )
    price = models.FloatField(
        null=False,
        blank=False,
        verbose_name='Price in EUR'
    )

    size = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name='Size(km2)'
    )
    type = models.CharField(
        choices=Type.choices(),
        max_length=Type.max_len(),
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=False,
        blank=False,
    )

    publication_date = models.DateField(
        blank=True,
        null=False,
        auto_now=True,
    )

    location = models.ForeignKey(
        City,
        on_delete=models.RESTRICT,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')

        return super().save(*args, **kwargs)


class Photo(models.Model):
    image = models.ImageField(
        upload_to='listing_photos/',
        null=False,
        blank=True,
        validators=(validate_file_less_than_5mb, validate_image_size),
    )

    listing = models.ForeignKey(
        Listing,
        on_delete=models.RESTRICT,
    )
