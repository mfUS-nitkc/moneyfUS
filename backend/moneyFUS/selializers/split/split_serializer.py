from rest_framework import serializers
from ...models.split.split import Split, SplitDetail


class SplitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Split
        fields = "__all__"

class SplitDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SplitDetail
        fields = "__all__"
