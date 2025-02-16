from django.db import models
import uuid

class UsageCategory(models.Model):
    usage_category_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    usage_category_name = models.CharField(max_length=255)
    usage_category_code = models.CharField(max_length=50, unique=True, null=True, blank=True)
