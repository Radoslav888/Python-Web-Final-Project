from django.core import exceptions
from django.core.files.images import get_image_dimensions


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Only letters are allowed')


def validate_file_less_than_5mb(fileobj):
    filesize = fileobj.file.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit*1024*1024:
        raise exceptions.ValidationError(f'Max file size is {megabyte_limit}MB')


def validate_image_size(value):
    w, h = get_image_dimensions(value)
    if w > 4000 or w < 500:
        raise exceptions.ValidationError(f"The image is {w} pixels wide. It's supposed to be between 500px and 4000px!")
    if h > 2000 or h < 300:
        raise exceptions.ValidationError(f"The image is {h} pixels high. It's supposed to be between 300px and 2000px!")
    return value


