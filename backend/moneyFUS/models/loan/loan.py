from django.db import models
from ..user.user import User
import uuid

class Loan(models.Model):
  loan_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
  lender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="lend_to_user")
  borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="borrow_to_user")
  amount = models.PositiveIntegerField()
  due_date = models.DateField()
  is_paid = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)