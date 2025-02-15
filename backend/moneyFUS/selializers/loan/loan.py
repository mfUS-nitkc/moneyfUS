from rest_framework import serializers
from ...models.loan.loan import Loan

class LoanSerializer(serializers.ModelSerializer):
  class Meta:
      model = Loan
      fields = ["loan_id", "lender", "borrower", "amount", "due_date", "is_paid"]
      read_only_fields = ["loan_id", "is_paid"]