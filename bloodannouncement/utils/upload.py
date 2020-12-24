from django.utils import timezone
from django.utils.text import slugify

__all__ = ["generate_upload_path"]


def generate_upload_path(instance, filename):
    model_name = slugify("{}".format(instance._meta.model_name))
    image_path = "media/" + model_name + "/" + timezone.now().strftime('%Y-%m-%d') + "/" + filename
    return image_path
