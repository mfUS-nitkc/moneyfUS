from django.db import models
from ..user.user import User
from .usage_category import UsageCategory
import uuid

class AssetLog(models.Model):
    asset_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    usage_category = models.ForeignKey(UsageCategory, on_delete=models.PROTECT)
    amount = models.IntegerField()
    issued_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

