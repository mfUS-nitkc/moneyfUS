from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ...backends.user.cookie_authentication import CookieTokenBackend
from ...models.notify.notify import Notify
from ...serializers.notify.notify_serializer import NotifySerializer

class NotifyView(APIView):
  authentication_classes = [CookieTokenBackend]
  permission_classes = [IsAuthenticated]
  
  def get(self, request):
    notifies = Notify.objects.filter(user_id=request.user, is_read=False) 
    serializer = NotifySerializer(notifies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
