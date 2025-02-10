from rest_framework import serializers
from ...models.lend.lend import Lend

class LendSerializer(serializers.ModelSerializer):
  class Meta:
      model = Lend
      fields = ["lend_id", "lender", "borrower", "amount", "due_date", "is_paid"]
      read_only_fields = ["lend_id", "is_paid"]