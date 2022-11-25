from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models

from Hestia.core.validators import validate_only_letters


# Create your models here.


class AppUser(AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MAX_LEN_LAST_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        )
    )

    email = models.EmailField(
        unique=True,
    )

