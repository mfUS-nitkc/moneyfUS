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
    
