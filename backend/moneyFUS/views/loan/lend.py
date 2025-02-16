from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ...serializers.loan.loan import LoanSerializer
from ...models.loan.loan import Loan
from ...utils.Response import create_response
from ...backends.user.cookie_authentication import CookieTokenBackend

class LendView(APIView):
  authentication_classes = [CookieTokenBackend]
  permission_classes = [IsAuthenticated]
  
  def get(self, request):
    lends = Loan.objects.filter(lender=request.user)  # ユーザーが貸し手になっている貸し借りログ
    serializer = LoanSerializer(lends, many=True)
    response = create_response({'items': serializer.data}, status=status.HTTP_200_OK)
    return response
  
  def post(self, request):
    req =  {}
    req["borrower"] = request.data.get("lend_to_user_id")
    req["lender"] = request.user.user_id
    req["amount"] = int(request.data.get("amount", 0))
    req["due_date"] = request.data.get("due_date")
    serializer = LoanSerializer(data=req)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
