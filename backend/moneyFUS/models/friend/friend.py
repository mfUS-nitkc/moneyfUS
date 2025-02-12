from django.db import models
from ..user.user import User

class Friend(models.Model):
  user_id_1 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="friend_1")
  user_id_2 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="friend_2")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    constraints = [
      models.UniqueConstraint(
        fields=["user_id_1", "user_id_2"], name="unique_friendship"
      )
    ]
    
  def save(self, *args, **kwargs):
    if self.user_id_1.user_id > self.user_id_2.user_id:
      self.user_id_1, self.user_id_2 = self.user_id_2, self.user_id_1
    super().save(*args, **kwargs)