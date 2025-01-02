from rest_framework import serializers
from ...models.asset.asset_log import AssetLog


class AssetLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetLog
        fields = "__all__"
