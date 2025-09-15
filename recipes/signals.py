from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.utils.text import slugify
import os

from recipes.models import Recipe


@receiver(pre_save, sender=Recipe)
def recipe_pre_save_handler(sender, instance, **kwargs):
    if instance.title:
        instance.slug = slugify(instance.title)


@receiver(post_delete, sender=Recipe)
def delete_recipe_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
