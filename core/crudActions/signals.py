from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from .models import AuditLog  # See model below

@receiver(post_save)
def log_save(sender, instance, created, **kwargs):
    if sender.__module__.startswith('django.'):
        return
    AuditLog.objects.create(
        action='Created' if created else 'Updated',
        content_type=ContentType.objects.get_for_model(instance),
        object_id=instance.pk,
        description=str(instance)
    )

@receiver(post_delete)
def log_delete(sender, instance, **kwargs):
    if sender.__module__.startswith('django.'):
        return
    AuditLog.objects.create(
        action='Deleted',
        content_type=ContentType.objects.get_for_model(instance),
        object_id=instance.pk,
        description=str(instance)
    )
