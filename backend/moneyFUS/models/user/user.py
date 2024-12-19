from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.db import models
from ...utils.hash_password import hash_password
import uuid


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **fields):
        if not email:
            raise ValueError("Email field must be set")
        email = self.normalize_email(email)
        user = User(email=email, username=username, **fields)
        user.save(using=self._db)
        if password:
            user.set_password(plain_password=password)
        return user

    def create_superuser(self, email, username, password=None, **fields):
        fields.setdefault("is_staff", True)
        fields.setdefault("is_superuser", True)
        return self.create_user(email, username, password, fields=fields)


class User(AbstractBaseUser):
    user_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField()
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "user_id"
    REQUIRED_FIELDS = ["username"]

    def clean(self):
        if self.is_active:
            if (
                User.objects.filter(email=self.email, is_active=True)
                .exclude(pk=self.pk)
                .exists()
            ):
                raise ValidationError("既に登録されているユーザーです。")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def set_password(self, plain_password):
        if not plain_password:
            raise ValueError("plain_passwordが不足しています。")

        if not hasattr(self, "auth"):
            self.auth = UserAuth.objects.create(user=self)

        self.auth.set_password(plain_password)

    def check_password(self, plain_password):
        if not self.password:
            return False
        return self.auth.check_password(plain_password)

    def __str__(self):
        return self.email


class UserAuthManager(models.Manager):
    def create_auth(self, user, plain_password):
        if not user or not plain_password:
            raise ValueError("User, plain_passwordの両方かどちらかが不足しています。")

        hashed_password = hash_password(user.email, plain_password)

        return self.create(user=user, password=hashed_password)


class UserAuth(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="auth")
    password = models.CharField(max_length=255, blank=True)

    objects = UserAuthManager()

    def __str__(self):
        return f"Auth for {self.user.email}"

    def set_password(self, plain_password: str):
        if not plain_password:
            raise ValueError("plain_passwordが不足しています。")
        self.password = hash_password(self.user.email, plain_password)
        self.save()

    def check_password(self, plain_password: str):
        if not plain_password:
            raise ValueError("plain_passwordが不足しています。")
        return self.password == hash_password(self.user.email, plain_password)
