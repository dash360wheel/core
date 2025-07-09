from django.db import models

# Create your models here.
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class AuditLog(models.Model):
    action = models.CharField(max_length=20)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
