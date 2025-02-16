from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from ...serializers.friend.friend import FriendSerializer
from ...models.friend.friend import Friend
from ...models.user.user import User
from ...serializers.user.user_serializer import UserSerializer
from ...backends.user.cookie_authentication import CookieTokenBackend

class FriendView(APIView):
  authentication_classes = [CookieTokenBackend]
  permission_classes = [IsAuthenticated]
  
  def get_friends_id(self, user):
    friendships = Friend.objects.filter(Q(user_id_1=user) | Q(user_id_2=user))
    
    friend_ids = []
    for friendship in friendships:
      if friendship.user_id_1 == user:
        friend_ids.append(friendship.user_id_2.user_id)
      else:
        friend_ids.append(friendship.user_id_1.user_id)
    
    return friend_ids
  
  def get(self, request):
    friend_ids = self.get_friends_id(request.user)
    friends = [UserSerializer(User.objects.get(user_id=friend_id)).data for friend_id in friend_ids]
    return Response(dict({"success": True},**{'friends': friends}), status=status.HTTP_200_OK)
  
  def post(self, request):
    add_user_id = request.data.get("user_id")
    add_user = get_object_or_404(User, user_id=add_user_id)
    if add_user is None:
      print('None')
      return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)
    
    new_friendship = self.create_friendship(request.user, add_user)
    friendship_serializer = FriendSerializer(data=new_friendship)
    if friendship_serializer.is_valid():
      friendship_serializer.save()
      return Response(dict({"success": True}, **{'friend_ids': self.get_friends_id(request.user)}), status=status.HTTP_200_OK)
    
    print(new_friendship)
    return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)
    
  def create_friendship(self, me: User, friend: User):
    new_friendship_dirty = {'user_id_1': me.user_id, 'user_id_2': friend.user_id}
    friendship_serializer = FriendSerializer(data=new_friendship_dirty)
    if friendship_serializer.is_valid():
      return new_friendship_dirty
    return None
