from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.db import models
import hashlib
import uuid


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **fields):
        if not email:
            raise ValueError("Email field must be set")
        email = self.normalize_email(email)
        user = User(email=email, username=username, **fields)
        user.save(using=self._db)
        if password:
            userauth = UserAuth(
                user=user,
                password=self.make_password(email=email, raw_password=password),
            )
            userauth.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **fields):
        fields.setdefault("is_staff", True)
        fields.setdefault("is_superuser", True)
        return self.create_user(email, username, password, fields=fields)

    def make_password(self, email, raw_password):
        msg = email + raw_password
        return hashlib.sha256(msg.encode("utf-8")).hexdigest()


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

    def __str__(self):
        return self.email


class UserAuth(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=255, blank=True)
