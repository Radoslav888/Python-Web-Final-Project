from django.core.validators import MinLengthValidator
from django.db import models
from django.template.defaultfilters import slugify

from Hestia.core.validators import validate_file_less_than_5mb


# Create your models here.

class News(models.Model):
    class Meta:
        verbose_name_plural = "news"
    MIN_TITLE_LENGTH = 5
    MAX_TITLE_LENGTH = 50

    MIN_TEXT_LENGTH = 50

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        validators=(
            MinLengthValidator(MIN_TITLE_LENGTH),
        ),
        null=False,
        blank=False,
    )
    text = models.TextField(
        validators=(
            MinLengthValidator(MIN_TEXT_LENGTH),
        ),
        null=False,
        blank=False,
    )
    image = models.ImageField(
        upload_to='news_photos/',
        null=False,
        blank=True,
        validators=(validate_file_less_than_5mb,),
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.title}')

        return super().save(*args, **kwargs)
