from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ...backends.user.cookie_authentication import CookieTokenBackend


class UserSelfView(APIView):
  authentication_classes = [CookieTokenBackend]
  permission_classes = [IsAuthenticated]
  
  def get(self, request):
    res = {}
    res = dict({'success': True}, **request.user.encode())
    return Response(res, status=status.HTTP_200_OK)
  
  def delete(self, request):
    user = request.user
    user.is_active = False
    user.save()
    res = Response({"success": True}, status=status.HTTP_204_NO_CONTENT)
    res.delete_cookie("token")
    return res

  def patch(self, request):
      user = request.user
      user.email = request.data.get("email")
      user.username = request.data.get("username")
      old_plain_password = request.data.get("old_password")
      new_plain_password = request.data.get("new_password")

      res = Response()

      try:
          user.save()
          res = Response({"success": True})
      except ValidationError:
          res = Response({"sucess": False})
          return res

      if new_plain_password and user.check_password(old_plain_password):
          user.set_password(new_plain_password)
          res = Response({"success": True})

      return res
