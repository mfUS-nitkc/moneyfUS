from rest_framework import serializers
from ...models.asset.asset_log import AssetLog
from ..asset.usage_category_serializer import UsageCategorySerializer


class AssetLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetLog
        exclude = ('created_at', 'updated_at')
        
    def to_representation(self, instance):
      representation = super().to_representation(instance)
      representation["usage_category"] = UsageCategorySerializer(instance.usage_category).data
      return representation
    