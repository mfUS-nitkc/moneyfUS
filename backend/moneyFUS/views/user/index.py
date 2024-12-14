from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from ...models.user.user import UserManager
from ...backends.user.cookie_authentication import CookieTokenBackend


class UserView(APIView):
    def get_authenticators(self):
        if self.request.method in ["DELETE", "PATCH"]:
            return [CookieTokenBackend()]
        return []

    def get_permissions(self):
        if self.request.method in ["DELETE", "PATCH"]:
            return [IsAuthenticated()]
        return [AllowAny()]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        username = request.data.get("username")
        created_user = UserManager().create_user(
            email=email, password=password, username=username
        )
        if created_user:
            return Response(
                {
                    "success": True,
                    "email": created_user.email,
                    "user_id": created_user.user_id,
                    "username": created_user.username,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"success": False, "reason": "Invalid credentials"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request):
        user = request.user
        user.is_active = False
        user.save()
        res = Response({"success": True}, status=status.HTTP_204_NO_CONTENT)
        res.delete_cookie("token")
        return res

