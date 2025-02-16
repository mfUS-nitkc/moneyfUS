from rest_framework import serializers
from ...models.loan.loan import Loan
from ...selializers.user.user_serializer import UserSerializer

class LoanSerializer(serializers.ModelSerializer):
  class Meta:
      model = Loan
      fields = ["loan_id", "lender", "borrower", "amount", "due_date", "is_paid"]
      read_only_fields = ["loan_id", "is_paid"]
      
  def to_representation(self, instance):
      representation = super().to_representation(instance)
      representation["lender"] = UserSerializer(instance.lender).data
      representation["borrower"] = UserSerializer(instance.borrower).data
      return representation
    
       