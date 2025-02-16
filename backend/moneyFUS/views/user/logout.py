from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from ...backends.user.cookie_authentication import CookieTokenBackend


class LogoutView(APIView):
    authentication_classes = [CookieTokenBackend]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        res = Response(status=status.HTTP_204_NO_CONTENT)
        res.delete_cookie("token")
        return res
