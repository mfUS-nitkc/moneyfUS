from rest_framework import serializers
from ...models.asset.usage_category import UsageCategory


class UsageCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UsageCategory
        fields = "__all__"
