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
