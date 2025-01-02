from django.db import models
import uuid

class UsageCategory(models.Model):
    category_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    category_name = models.CharField(max_length=255)
