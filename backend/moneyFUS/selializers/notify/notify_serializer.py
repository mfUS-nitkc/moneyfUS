from rest_framework import serializers
from ...models.notify.notify import Notify


class NotifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Notify
        fields = "__all__"
