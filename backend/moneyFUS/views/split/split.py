from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ...backends.user.cookie_authentication import CookieTokenBackend
from ...models.split.split import Split, SplitDetail
from ...models.loan.loan import Loan
from ...models.user.user import User
from ...serializers.split.split_serializer import SplitSerializer
from ...utils.Response import create_error_response, create_response

from django.db import transaction

class SplitView(APIView):
    authentication_classes = [CookieTokenBackend]
    permission_classes = [IsAuthenticated]

    def post(self, request):
      with transaction.atomic():
        split_request = request.data
        split_request["payer"] = request.user.user_id
        split_serializer = SplitSerializer(data=split_request)
        if split_serializer.is_valid():
          split = split_serializer.save()
          
          participants = request.data.get("participants", [])
          split_details = []
          loans = []
          
          print(participants)
          
          for participant in participants:
            participant_id = participant.get("participant_id")
            amount = participant.get("amount")
            
            if not participant_id or not amount:
              error_response = create_error_response({"detail": "participant_id and amount are required for each participant"}, status=status.HTTP_400_BAD_REQUEST)
              return error_response
            
            split_detail = SplitDetail(
              split_id=split,
              participant_id=User.objects.get(user_id=participant_id),
              amount=amount
            )
            split_details.append(split_detail)
            
            loan = Loan(
              lender=split.payer,
              borrower=User.objects.get(user_id=participant_id),
              amount=amount,
              due_date=split.due_date
            )
            
            loans.append(loan)
          
          Loan.objects.bulk_create(loans)
          SplitDetail.objects.bulk_create(split_details)
          
          return create_response(split_serializer.data, status=status.HTTP_201_CREATED)
      error_response = create_error_response({"detail":"Error has occured."}, status=status.HTTP_400_BAD_REQUEST)
      return error_response
