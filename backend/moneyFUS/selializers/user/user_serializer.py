from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from ...models import User, UserAuth


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user_id", "email", "username", "is_active"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        UserAuth.objects.create(user=user, password=make_password(password))
        return user
