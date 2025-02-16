from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ...models.asset.usage_category import UsageCategory
from ...selializers.loan.loan import LoanSerializer
from ...selializers.asset.asset_log_serializer import AssetLogSerializer
from ...models.loan.loan import Loan
from ...backends.user.cookie_authentication import CookieTokenBackend

import datetime

class LoanCheckoutView(APIView):
  authentication_classes = [CookieTokenBackend]
  permission_classes = [IsAuthenticated]
  
  def get_object(self, loan_id, user):
    return get_object_or_404(Loan, loan_id=loan_id, lender=user)
  
  def post(self, request, loan_id, *args, **kwargs):
    lend = self.get_object(loan_id, request.user)
    if lend.is_paid:
      return Response({'success': False, 'detail': 'The lend is already checked out.'}, status=status.HTTP_400_BAD_REQUEST)
    lend.is_paid = True
    checkout_lend_asset_log, checkout_borrowed_asset_log = self.create_checkout_asset_log(lend)
    
    asset_lend_serializer = AssetLogSerializer(data=checkout_lend_asset_log)
    asset_borrowed_serializer = AssetLogSerializer(data=checkout_borrowed_asset_log)
    asset_lend_serializer.is_valid()
    asset_borrowed_serializer.is_valid()
    if asset_lend_serializer.is_valid() and asset_borrowed_serializer.is_valid():
      asset_lend_serializer.save()
      asset_borrowed_serializer.save()
      print('Saved!')
    else:
      return Response({"success":False, "detail": {"lend": asset_lend_serializer.errors, "borrowed":asset_borrowed_serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
    print('serializer Saved!')
    lend_serializer = LoanSerializer(lend)
    lend.save()
    return Response(lend_serializer.data, status=status.HTTP_200_OK)
  
  def create_checkout_asset_log(self, lend: Loan):
    checkout_lend_usage_category, _ = UsageCategory.objects.get_or_create(usage_category_code='CHECKOUT_LEND', defaults={'usage_category_name': '借り清算(返済)'})
    checkout_borrowed_usage_category, _ = UsageCategory.objects.get_or_create(usage_category_code='CHECKOUT_BORROWED', defaults={'usage_category_name': '貸し清算(返済)'})
    
    checkout_lend_asset_log = {
      "usage_category": checkout_lend_usage_category.usage_category_id,
      "amount": lend.amount,
      "issued_at": datetime.date.today(),
      "user": lend.lender.user_id
    }
    checkout_borrowed_asset_log = {
      "usage_category": checkout_borrowed_usage_category.usage_category_id,
      "amount": lend.amount,
      "issued_at": datetime.date.today(),
      "user": lend.borrower.user_id
    }
    
    return checkout_borrowed_asset_log, checkout_lend_asset_log
  