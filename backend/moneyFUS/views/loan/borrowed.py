from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ...selializers.loan.loan import LoanSerializer
from ...models.loan.loan import Loan
from ...utils.Response import create_response
from ...backends.user.cookie_authentication import CookieTokenBackend

class BorrowedView(APIView):
  authentication_classes = [CookieTokenBackend]
  permission_classes = [IsAuthenticated]
  
  def get(self, request):
    borroweds = Loan.objects.filter(borrower=request.user)  # Userが借り手となっている貸し借りレコード 
    serializer = LoanSerializer(borroweds, many=True)
    response = create_response({'items': serializer.data}, status=status.HTTP_200_OK)
    return response
  
  def post(self, request):
    req =  {}
    req["borrower"] = request.user.user_id
    req["lender"] = request.data.get("borrowed_by_user_id")
    req["amount"] = int(request.data.get("amount", 0))
    req["due_date"] = request.data.get("due_date")
    serializer = LoanSerializer(data=req)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
