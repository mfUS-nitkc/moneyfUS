from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from ...models.user.user import User, UserAuth
import hashlib


class PasswordUserBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
            auth = UserAuth.objects.get(user=user)
            user_password = hashlib.sha256((email+password).encode("utf-8")).hexdigest()
            print(auth.password)
            print(user_password)
            if auth.password == user_password:
                return user
        except (User.DoesNotExist, UserAuth.DoesNotExist):
            print("user does not found")
            return None
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
