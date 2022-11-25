from django.core.validators import MinLengthValidator
from django.db import models


class City(models.Model):
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

