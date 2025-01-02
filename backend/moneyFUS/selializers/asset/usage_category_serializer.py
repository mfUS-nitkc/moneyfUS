from rest_framework import serializers
from ...models import UsageCategory


class UsageCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UsageCategory
        fields = "__all__"
