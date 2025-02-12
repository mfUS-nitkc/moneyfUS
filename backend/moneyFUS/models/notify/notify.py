from django.db import models
from ..user.user import User
import uuid

class Notify(models.Model):
  notify_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  is_read = models.BooleanField(default=False)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
