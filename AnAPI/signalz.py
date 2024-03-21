from django.db.models.signals import pre_save
from django.dispatch import receiver
from AnAPI.models import Story
from django.utils.text import slugify

@receiver(pre_save, sender=Story)
def slugster(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        instance.slug = slug