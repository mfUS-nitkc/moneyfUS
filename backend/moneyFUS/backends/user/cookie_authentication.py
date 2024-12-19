from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token


class CookieTokenBackend(BaseAuthentication):
    def authenticate(self, request):
        if "token" not in request.COOKIES:
            return None
        token_key = request.COOKIES["token"]
        if not token_key:
            return None

        try:
            token = Token.objects.get(key=token_key)
        except Token.DoesNotExist:
            raise AuthenticationFailed("Invalid token.")

        return (token.user, token)

    def authenticate_header(self, request):
        return "token"
