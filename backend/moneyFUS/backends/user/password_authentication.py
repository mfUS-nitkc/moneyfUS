from django.contrib.auth.backends import BaseBackend
from ...models.user.user import User, UserAuth
from ...utils.hash_password import hash_password


class PasswordUserBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email, is_active=True)
            auth = user.auth
            user_password = hash_password(email, password)
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
