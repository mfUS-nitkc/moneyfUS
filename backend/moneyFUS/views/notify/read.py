from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ...backends.user.cookie_authentication import CookieTokenBackend
from ...models.notify.notify import Notify
from ...selializers.notify.notify_serializer import NotifySerializer

class NotifyReadView(APIView):
  authentication_classes = [CookieTokenBackend]
  permission_classes = [IsAuthenticated]
  
  def get_object(self, notify_id, user):
    notify = get_object_or_404(Notify, notify_id=notify_id, user_id=user.user_id)
    return notify
  
  def post(self, request, notify_id):
    notify = self.get_object(notify_id, request.user)
    notify.is_read = True
    return Response({'success': True}, status=status.HTTP_200_OK)
