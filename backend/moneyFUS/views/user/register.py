from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from ...models.user.user import UserManager


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        username = request.data.get("username")
        created_user = UserManager().create_user(email=email, password=password, username=username)
        if created_user:
            return Response({"success": True, "email": created_user.email, "user_id": created_user.user_id, "username": created_user.username}, status=status.HTTP_201_CREATED)
        return Response(
            {"success": False, "reason": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
        )
