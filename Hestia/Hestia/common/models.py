from django.core.validators import MinLengthValidator
from django.db import models


class City(models.Model):
    class Meta:
        verbose_name_plural = "cities"

    MIN_NAME_LENGTH = 3
    MAX_NAME_LENGTH = 50

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_NAME_LENGTH),
        ),
        null=False,
        blank=False,
    )

    pictureURL = models.URLField(
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
    )

    def __str__(self):
        return self.name

    def listings_count(self):
        listings = 0
        for _ in self.listing_set.all():
            listings += 1
        return listings
