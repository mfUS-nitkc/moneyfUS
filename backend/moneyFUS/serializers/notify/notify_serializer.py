from rest_framework import serializers
from ...models.notify.notify import Notify


class NotifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Notify
        exclude = ('created_at', 'updated_at', 'user_id')
