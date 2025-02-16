from django.db import models
from ..user.user import User
import uuid

class Split(models.Model):
    split_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    payer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    total_amount = models.IntegerField()
    description = models.CharField(max_length=255, blank=True)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SplitDetail(models.Model):
    split_detail_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    split_id = models.ForeignKey(Split, on_delete=models.CASCADE, related_name="splits")
    participant_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="participants")
    amount = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
      constraints = [
        models.UniqueConstraint(fields=['split_id', 'participant_id'], name='unique_split_participant')
      ]
