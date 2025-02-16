from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ...models.notify.notify import Notify
from ...serializers.notify.notify_serializer import NotifySerializer
from ...serializers.loan.loan import LoanSerializer
from ...serializers.asset.asset_log_serializer import AssetLogSerializer
from ...models.loan.loan import Loan
from ...backends.user.cookie_authentication import CookieTokenBackend

class LoanRemindView(APIView):
  authentication_classes = [CookieTokenBackend]
  permission_classes = [IsAuthenticated]
  
  def get_object(self, loan_id, user):
    return get_object_or_404(Loan, loan_id=loan_id, lender=user)
  
  def post(self, request, loan_id, *args, **kwargs):
    loan = self.get_object(loan_id, request.user)
    if loan.is_paid:
      return Response({'success': False, 'detail': 'The lend is already checked out.'}, status=status.HTTP_400_BAD_REQUEST)
    remind = self.create_checkout_remind(loan)
    print(remind)
    if remind is None:
      return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)
    
    remind_serializer = NotifySerializer(data=remind)
    
    if remind_serializer.is_valid():
      remind_serializer.save()
      return Response({'success': True}, status=status.HTTP_200_OK)
    
    print(remind_serializer.errors)
    
    return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)
    
  
  def create_checkout_remind(self, loan: Loan):
    remind_dirty = {'user_id': loan.borrower.user_id, 'content': f'{loan.lender.username} さんから借りたお金の清算依頼がとどきました．'}
    remind_serializer = NotifySerializer(data=remind_dirty)
    if remind_serializer.is_valid():
      return remind_dirty
    print(remind_serializer.errors)
    return None
