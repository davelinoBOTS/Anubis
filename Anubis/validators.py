import os
from django.core.exceptions import ValidationError


def validate_images_extension(value):
    ext = os.path.splitext(value.name)[1][1:]
    valid_extensions = ['ico', 'jpg', 'jpeg', 'png', 'bpm', 'gif', 'tiff', 'psd']

    if not ext.lower() in valid_extensions:
        raise ValidationError("A extensão ." + ext.lower() + " não é permitida")


def validate_files_extension(value):
    ext = os.path.splitext(value.name)[1][1:]
    valid_extensions = ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'odt', 'odf', 'jpg', 'jpeg', 'png', 'bpm', 'txt']

    if not ext.lower() in valid_extensions:
        raise ValidationError("A extensão ." + ext.lower() + " não é permitida")
