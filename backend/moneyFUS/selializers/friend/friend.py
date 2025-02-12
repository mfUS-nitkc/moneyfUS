from rest_framework import serializers
from ...models.friend.friend import Friend


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ["user_id_1", "user_id_2"]
