from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ...models.asset.usage_category import UsageCategory
from ...selializers.lend.lend import LendSerializer
from ...selializers.asset.asset_log_serializer import AssetLogSerializer
from ...models.lend.lend import Lend
from ...backends.user.cookie_authentication import CookieTokenBackend

import datetime

class LendView(APIView):
  authentication_classes = [CookieTokenBackend]
  permission_classes = [IsAuthenticated]
  
  def get(self, request):
    lends = Lend.objects.filter(borrower=request.user)
    serializer = LendSerializer(lends, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request):
    req =  {}
    req["borrower"] = request.data.get("lend_to_user_id")
    req["lender"] = request.user.user_id
    req["amount"] = int(request.data.get("amount", 0))
    req["due_date"] = request.data.get("due_date")
    serializer = LendSerializer(data=req)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LendCheckoutView(APIView):
  def get_object(self, lend_id, user):
    return get_object_or_404(Lend, lend_id=lend_id, lender=user)
  
  def post(self, request, lend_id, *args, **kwargs):
    lend = self.get_object(lend_id, request.user)
    if lend.is_paid:
      return Response({'success': False, 'detail': 'The lend is already checked out.'}, status=status.HTTP_400_BAD_REQUEST)
    lend.is_paid = True
    checkout_lend_asset_log, checkout_borrowed_asset_log = self.create_checkout_asset_log(lend)
    
    asset_lend_serializer = AssetLogSerializer(data=checkout_lend_asset_log)
    asset_borrowed_serializer = AssetLogSerializer(data=checkout_borrowed_asset_log)
    if asset_lend_serializer.is_valid() and asset_borrowed_serializer.is_valid():
      asset_lend_serializer.save()
      asset_borrowed_serializer.save()
      print('Saved!')
    else:
      return Response({"success":False, "detail": {"lend": asset_lend_serializer.errors, "borrowed":asset_borrowed_serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
    print('serializer Saved!')
    lend_serializer = LendSerializer(lend)
    lend.save()
    return Response(lend_serializer.data, status=status.HTTP_200_OK)
  
  def create_checkout_asset_log(self, lend: Lend):
    checkout_lend_usage_category, _ = UsageCategory.objects.get_or_create(category_code='CHECKOUT_LEND', defaults={'category_name': '借り清算(返済)'})
    checkout_borrowed_usage_category, _ = UsageCategory.objects.get_or_create(category_code='CHECKOUT_BORROWED', defaults={'category_name': '貸し清算(返済)'})
    
    checkout_lend_asset_log = {
      "usage_category": checkout_lend_usage_category.category_id,
      "amount": lend.amount,
      "issued_at": datetime.date.today(),
      "user": lend.lender
    }
    checkout_borrowed_asset_log = {
      "usage_category": checkout_borrowed_usage_category.category_id,
      "amount": lend.amount,
      "issued_at": datetime.date.today(),
      "user": lend.borrower
    }
    
    return checkout_borrowed_asset_log, checkout_lend_asset_log
  